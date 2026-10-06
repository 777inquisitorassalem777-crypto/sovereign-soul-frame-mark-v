"""
Hardware ↔ Software Mapping
Sovereign Soul Frame — Mark V
"""

from __future__ import annotations

HARDWARE_MAP = {
    # Mechanical systems from the original steampunk blueprints
    "spectral_reactor": {
        "description": "Three vacuum tubes + stacked alchemical spheres (Analyse Spectrale + multi-level reactor)",
        "software_role": "Primary energy & environmental analysis sensor stream",
        "sensors": ["plasma_density", "spectral_signature", "energy_level"],
        "actuators": ["reactor_throttle", "spectrum_focus"],
    },
    "bobina_da_fe": {
        "description": "Bobina da Fé Reverberante — resonant coil on upper back",
        "software_role": "Resonance / coherence field generator + intention amplifier proxy",
        "sensors": ["field_strength", "resonance_frequency"],
        "actuators": ["coil_current", "phase_alignment"],
    },
    "piston_musculature": {
        "description": "Flexor/Extensor piston system + articulated joints (Mark IV heritage)",
        "software_role": "Locomotion and force application layer",
        "sensors": ["joint_angle", "piston_pressure", "load"],
        "actuators": ["flexor_valve", "extensor_valve", "gear_ratio"],
    },
    "authority_mechanism": {
        "description": "Mechanical ranking wheels, punched-card registry, physical STOP gates",
        "software_role": "Hardware embodiment of AuthorityGate",
        "sensors": ["lever_state", "card_presence"],
        "actuators": ["gate_solenoid"],  # only under human supervision
    },
    "fathom_fist": {
        "description": "Right-hand tentacle gauntlet with ocular sensor",
        "software_role": "Manipulation + close-range sensing",
        "sensors": ["grip_force", "tactile", "green_eye_vision"],
        "actuators": ["tentacle_servos", "compressor"],
    },
    "parabola_discharge": {
        "description": "Left-wrist spring-loaded cutting disc magazine",
        "software_role": "Precision cutting / utility tool (high-risk)",
        "sensors": ["disc_count", "spring_tension"],
        "actuators": ["release_trigger"],  # hard-gated
    },
    "da_vinci_interface": {
        "description": "Notebook-style control panels and dials on arms / helmet",
        "software_role": "Human-readable manual override and diagnostic surface",
        "sensors": ["dial_positions", "notebook_state"],
        "actuators": ["status_indicators"],
    },
    "helmet_casque": {
        "description": "Diving-helmet style head with multi-lens and respiration tubes",
        "software_role": "Primary perception + operator communication",
        "sensors": ["multi_spectrum_vision", "audio", "internal_atmosphere"],
        "actuators": ["lens_focus", "comm_channel"],
    },
}


def get_system_info(system_name: str) -> dict:
    return HARDWARE_MAP.get(system_name, {"error": "unknown system"})


def list_all_systems() -> list[str]:
    return list(HARDWARE_MAP.keys())
