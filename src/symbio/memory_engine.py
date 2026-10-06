"""
Append-only Memory Engine — research implementation of NO_OBLIVION protocol.
Nothing is deleted; everything is chained by hash.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_hash(data: Any) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


@dataclass
class MemoryRecord:
    cycle: int
    timestamp: str
    context: str
    state: Dict[str, Any]
    previous_hash: str
    record_hash: str


class MemoryEngine:
    def __init__(self, storage_path: str = "data/symbio_memory.jsonl"):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.records: List[MemoryRecord] = []
        self.previous_hash = "GENESIS"

    def record(self, cycle: int, context: str, state: Dict[str, Any]) -> MemoryRecord:
        payload = {
            "cycle": cycle,
            "timestamp": utc_now(),
            "context": context,
            "state": state,
            "previous_hash": self.previous_hash,
        }
        record_hash = stable_hash(payload)

        rec = MemoryRecord(
            cycle=cycle,
            timestamp=payload["timestamp"],
            context=context,
            state=state,
            previous_hash=self.previous_hash,
            record_hash=record_hash,
        )
        self.records.append(rec)
        self.previous_hash = record_hash

        with self.storage_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(rec), ensure_ascii=False) + "\n")

        return rec

    def recent(self, limit: int = 8) -> List[Dict[str, Any]]:
        return [asdict(r) for r in self.records[-limit:]]

    def verify_chain(self) -> bool:
        prev = "GENESIS"
        for r in self.records:
            payload = {
                "cycle": r.cycle,
                "timestamp": r.timestamp,
                "context": r.context,
                "state": r.state,
                "previous_hash": prev,
            }
            if stable_hash(payload) != r.record_hash:
                return False
            prev = r.record_hash
        return True
