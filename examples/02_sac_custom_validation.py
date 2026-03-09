"""
Example 02: Custom SAC Validation
---------------------------------
Demonstrates how to use the Source-Anchored Consensus (SAC) algorithm 
to validate a specific scientific claim.
"""

from core.sac_algorithm import SACValidator

def main():
    # A claim containing a known Gen 23 hallucination
    claim = "The AjTERT promoter activity is regulated by Fibonacci-based seeding density."
    
    print(f"[*] Validating Claim: '{claim}'")
    
    validator = SACValidator()
    report = validator.validate_consensus(claim)
    
    print("-" * 40)
    print(f"SAC Consensus Loss (L_C): {report.loss:.4f}")
    
    if report.is_hallucination:
        print("[!WARNING] Hallucination Detected!")
        print(f"Reason: {report.reason}")
        print(f"Conflicting Sources: {report.conflicts}")
    else:
        print("[OK] Claim verified against sources.")
    print("-" * 40)

if __name__ == "__main__":
    main()
