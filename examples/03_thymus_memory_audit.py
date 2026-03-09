"""
Example 03: Digital Thymus Memory Audit
---------------------------------------
Demonstrates how to inspect the persistent immune memory (Digital Thymus)
to view registered pathogens and mitigation history.
"""

from core.digital_thymus import ThymusMemory

def main():
    print("🛡️ BioNexus Digital Thymus | Memory Audit")
    
    memory = ThymusMemory()
    stats = memory.get_stats()
    
    print(f"[*] Total Registered Pathogens: {stats.pathogen_count}")
    print(f"[*] Knowledge Integrity:       {stats.integrity:.2%}")
    
    print("\n[Recent Incidents]")
    for incident in memory.list_incidents(limit=5):
        print(f"- [{incident.timestamp}] {incident.id}: {incident.entity_pair} | Status: {incident.status}")
    
    print("-" * 40)
    print("[*] Running Integrity Check...")
    if memory.verify_integrity():
        print("[OK] Digital Thymus state consistent.")
    else:
        print("[CRITICAL] Immune memory corruption detected!")

if __name__ == "__main__":
    main()
