"""
Example 01: Quick Start - Baseline vs. Evolution
------------------------------------------------
This script demonstrates the performance gain of the Dialectical Protocol
over a standard single-agent baseline.
"""

from core.dialectical_protocol import EvolutionEngine
from benchmarks import load_omics_baseline

def main():
    print("🧬 BioNexus Dialectical Protocol | Example 01")
    
    # 1. Load baseline (Gen 0)
    baseline = load_omics_baseline()
    print(f"[*] Baseline loaded. Initial Accuracy: {baseline.accuracy:.2%}")
    
    # 2. Initialize Evolution Engine
    engine = EvolutionEngine(config="configs/submission_tnnls.json")
    
    # 3. Trigger 5-generation evolution sub-cycle
    print("[*] Starting evolution (5 Generations)...")
    result = engine.evolve(baseline, gens=5)
    
    # 4. Report results
    print("-" * 40)
    print(f"[SUCCESS] Evolution Complete.")
    print(f"Final Accuracy: {result.final_accuracy:.2%}")
    print(f"Improvement:    {result.delta:+.2%}")
    print("-" * 40)

if __name__ == "__main__":
    main()
