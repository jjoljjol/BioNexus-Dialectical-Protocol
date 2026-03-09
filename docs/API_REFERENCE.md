# API Reference

This document covers the primary Python API for the BioNexus Dialectical Protocol.

## `core.dialectical_protocol`

### `EvolutionEngine`
The main orchestrator for AI generation and selection.

- `__init__(config: Dict)`: Initialize the engine with model parameters.
- `evolve(baseline: Payload, gens: int) -> EvolutionResult`: Runs the full evolutionary loop.

## `core.sac_algorithm`

### `SACValidator`
Validates information against grounding sources.

- `validate_consensus(report: str) -> ValidationReport`: Returns a consensus loss score and flags.
- `calculate_entropy(context: List[str]) -> float`: Measures information certainty.

## `core.digital_thymus`

### `ThymusMemory`
Manages immune memory tokens.

- `register_hallucination(incident: Incident)`: Saves binary conflict patterns for future filtering.
- `verify_integrity()`: Checks knowledge consistency.
