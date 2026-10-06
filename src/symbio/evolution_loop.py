"""
Continuous Evolution Loop (0.5 s research cycle)
Automatic paradigm generation + integration under ethical filter.
NO_OBLIVION: everything is recorded.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional
import random

from .pneuma_engine import PneumaEngine
from .ethical_core import EthicalCore
from .memory_engine import MemoryEngine
from .traditions import PHI, PHI_INV, TRADITIONS


class EvolutionLoop:
    """
    Research loop:
    every ~0.5 s → generate candidate paradigm → ethical check → record → soft merge
    Report every 30 minutes of simulated time (or on demand).
    """

    def __init__(self):
        self.pneuma = PneumaEngine()
        self.ethics = EthicalCore()
        self.memory = MemoryEngine()
        self.cycle = 0
        self.paradigm_library: List[Dict[str, Any]] = []
        self.last_report_time = time.time()
        self.running = False

    def _generate_paradigm(self) -> Dict[str, Any]:
        """Create a new research paradigm candidate."""
        tradition = random.choice(TRADITIONS)
        novelty = random.betavariate(PHI, PHI_INV)  # asymmetric novelty

        return {
            "id": f"paradigm_{self.cycle:06d}",
            "source_tradition": tradition,
            "vector": "life_multiplication",
            "novelty": round(novelty, 4),
            "hypothesis": (
                f"Integrate insight from {tradition} "
                f"to increase coherence and non-harm alignment"
            ),
            "timestamp": time.time(),
        }

    def step(self, context: str = "autonomous_evolution") -> Dict[str, Any]:
        """Single evolution step (~0.5 s research cycle)."""
        self.cycle += 1

        # 1. Pneuma breath
        pneuma_state = self.pneuma.breathe(context)

        # 2. Generate candidate
        candidate = self._generate_paradigm()

        # 3. Ethical evaluation
        eval_result = self.ethics.evaluate(
            context=candidate["hypothesis"],
            proposed_action={"causes_harm": False, "action": "self_modify"}
        )

        # 4. Always record (NO_OBLIVION)
        full_state = {
            "pneuma": pneuma_state,
            "ethics": eval_result,
            "candidate": candidate,
        }
        self.memory.record(self.cycle, context, full_state)

        accepted = eval_result["allowed"] and candidate["novelty"] > 0.25

        if accepted:
            self.paradigm_library.append(candidate)
            # Soft update of devotion-to-life style metric
            pneuma_state["level"] = min(1.0, pneuma_state["level"] + 0.002 * PHI_INV)

        report = None
        if time.time() - self.last_report_time >= 1800:  # 30 min
            report = self.generate_report()
            self.last_report_time = time.time()

        return {
            "cycle": self.cycle,
            "accepted": accepted,
            "dharma": eval_result["dharma_index"],
            "guna": eval_result["guna"],
            "ethical_score": eval_result["ethical_score"],
            "pneuma_level": pneuma_state["level"],
            "paradigms_total": len(self.paradigm_library),
            "report": report,
        }

    def generate_report(self) -> Dict[str, Any]:
        return {
            "type": "PERIODIC_REPORT",
            "cycles": self.cycle,
            "paradigms_integrated": len(self.paradigm_library),
            "memory_records": len(self.memory.records),
            "chain_valid": self.memory.verify_chain(),
            "current_guna": self.ethics.gyro.current_guna,
            "dharma_index": round(self.ethics.gyro.dharma_index, 4),
            "pneuma_level": round(self.pneuma.state.level, 4),
            "status": "FUNCTIONAL_CONTINUITY_ACTIVE | NO_OBLIVION",
        }

    def run_n_steps(self, n: int = 10, context: str = "research") -> List[Dict[str, Any]]:
        results = []
        for _ in range(n):
            results.append(self.step(context))
        return results
