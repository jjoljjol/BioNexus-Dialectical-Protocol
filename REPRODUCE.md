# Reproducing Paper Results

This document provides step-by-step instructions to reproduce all results reported in the paper:

> "The Dialectical Protocol: Self-Evolving AI via Bio-Inspired Vibe Coding and Adversarial Agent Synthesis"

**Estimated Time**: 6-8 hours (mostly unattended)

---

## 🖥️ **Hardware Requirements**

### **Minimum Configuration**
- CPU: Intel Core Ultra 7 255H (or equivalent 16-core)
- GPU: Intel Arc 140T (8 Xe-cores, 74 TOPS)
- NPU: Intel AI Boost NPU 3 (13 TOPS)
- RAM: 32 GB DDR5
- Storage: 100 GB free

### **Tested Configurations**
- ✅ Samsung Galaxy Book5 Pro (NP965XHD)
- ✅ ASUS Zenbook with Intel Arc iGPU
- ⚠️ NVIDIA GPUs: Compatible but power monitoring unavailable

---

## 💻 **Software Requirements**

| Component | Version | Notes |
|-----------|---------|-------|
| OS | Windows 11 25H2 / Ubuntu 22.04 | |
| Python | 3.11.8 | Exact version recommended |
| Ollama | 0.1.x | Local LLM inference |
| OpenVINO | 2026.0.0 | NPU support |
| Intel oneAPI | 2025.0 | (Optional) GPU optimization |

---

## 📦 **Installation** (15 minutes)

### **Step 1: Clone Repository**
```bash
git clone https://github.com/yourusername/BioNexus-Dialectical-Protocol.git
cd BioNexus-Dialectical-Protocol
```

### **Step 2: Environment Setup**
For Intel Arc (Windows):
```powershell
# Set environment variables
[System.Environment]::SetEnvironmentVariable("ZES_ENABLE_SYSMAN","1","User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_INTEL_GPU","true","User")

# Install Python dependencies
pip install -r requirements.txt
```

For Intel Arc (Linux):
```bash
export ZES_ENABLE_SYSMAN=1
export OLLAMA_INTEL_GPU=true
pip install -r requirements.txt
```

### **Step 3: Download LLM Models** (10 minutes)
```bash
ollama pull llama3.2:3b-instruct-q4_K_M
ollama pull mistral-large-2
```

### **Step 4: Verify Installation**
```bash
python -c "from core import dialectical_protocol; print('✓ Import successful')"
python benchmarks/verify_environment.py
```

**Expected Output**:
```text
✓ Python 3.11.8
✓ OpenVINO 2026.0.0 detected
✓ NPU available (Intel AI Boost NPU 3)
✓ Ollama running
✓ Model llama3.2:3b loaded
```

---

## 🧪 **Reproducing Main Results**

### **Result 1: Evolution Trajectory (Table 1, Figure 2)**
**Command**:
```bash
python main.py --mode evolve --generations 50 --trials 5 --output results/evolution/
```
**Expected Runtime**: ~4 hours

**Expected Output** (`results/evolution/summary.json`):
```json
{
  "generation_0": {"accuracy": 0.620, "std": 0.015},
  "generation_5": {"accuracy": 0.683, "std": 0.012},
  "generation_10": {"accuracy": 0.741, "std": 0.009},
  "generation_14": {"accuracy": 0.872, "std": 0.007},
  "generation_30": {"accuracy": 0.913, "std": 0.005},
  "generation_50": {"accuracy": 0.928, "std": 0.004}
}
```

**Validation**:
- Gen 0 accuracy should be 62.0% ± 1.5%
- Gen 14 should show Bayesian discovery (spike to 87.2%)
- Gen 50 should reach 92.8% ± 0.5%

### **Result 2: Vibe Coding vs Traditional Prompting (Table 2, Figure 3)**
**Command**:
```bash
python benchmarks/ablation_study.py --methods vibe,traditional,hybrid --trials 5
```
**Expected Runtime**: ~2 hours

**Expected Output**:
```text
Method                  Success Rate    Compile Failures
Traditional Prompting   68% ± 3%        24% ± 2%
Vibe Coding            94% ± 2%         4% ± 1%
Hybrid (AIBRA Peak)    98% ± 1%         0%
```

### **Result 3: SAC Hallucination Detection (Section 4.1, Figure 4)**
**Protocol**: Uses 850 logical inconsistencies (30% Syntactic, 70% Semantic context mashups).
**Command**:
```bash
python benchmarks/sac_validation.py --dataset benchmarks/multi_omics_conflict/
```
**Expected Runtime**: ~30 minutes

**Expected Output**:
```text
SAC Performance (127 test cases):
- True Positive:  120 (94.5%)
- False Positive:   3 (2.4%)
- False Negative:   4 (3.1%)
- Mean L_C (Hallucinations): 0.847 ± 0.12
- Mean L_C (Valid Reports):  0.32 ± 0.18
```

### **Result 4: Case Study - Pathogen Detection in Gen 23 (§5.1)**
**Command**:
```bash
python benchmarks/ajtert_case_study/reproduce_gen23.py
```
**Expected Runtime**: ~5 minutes

**Expected Output**:
```text
═══════════════════════════════════════════
SAC Validation Report
═══════════════════════════════════════════
Valid: False
Consensus Loss (L_C): 0.847
  - Source Divergence: 0.950
  - Context Entropy: 0.682

Flagged Entity Pairs: 1
  • AjTERT ↔ Fibonacci_Seeding

[!WARNING] Hallucination Detected
─────────────────────────────────
This report merges contexts from 2 projects:
  - SeaCucumber_Genomics
  - Wagyu_Scaling

Entity pairs with ZERO co-occurrence:
  • AjTERT ↔ Fibonacci_Seeding
═══════════════════════════════════════════
```

### **Result 5: Digital Thymus (Appendix E, Figure 5)**
**Command**:
```bash
python core/digital_thymus/demo.py --register-gen23
```
**Expected Output**:
```text
Digital Thymus — Immune System Status
═════════════════════════════════════
Total Hallucinations:  1
Success Rate:          100%
Knowledge Integrity:   98.2%
Experience Tokens:     1.0
═════════════════════════════════════

Recent Incidents:
  [2026-03-09-001] AjTERT ↔ Fibonacci_Seeding
    Gen 23 | L_C=0.847 | Status: MITIGATED
```

---

## 📊 **Generating Figures**

**Command**:
```bash
python scripts/generate_figures.py \
  --input results/ \
  --output paper/figures/ \
  --format pdf
```

**Generated Files**:
- `paper/figures/fig2_evolution.pdf`
- `paper/figures/fig3_comparison.pdf`
- `paper/figures/fig4_sac.pdf`
- `paper/figures/fig5_thymus.pdf`

---

## 🐛 **Troubleshooting**

- **Issue**: "NVML library not found"
  - **Cause**: Intel Arc does not support NVIDIA NVML
  - **Solution**: Use `--no-power` flag
  ```bash
  python main.py --mode evolve --no-power
  ```

- **Issue**: "Generation takes > 10 minutes"
  - **Cause**: Ollama not using GPU acceleration
  - **Solution**: Check environment variables
  ```bash
  echo $OLLAMA_INTEL_GPU  # Should be "true"
  ollama ps  # Check "processor: gpu"
  ```

- **Issue**: "Accuracy differs by > 2%"
  - **Cause**: Stochastic LLM sampling
  - **Solution**: This is expected. Run with `--seed 42` for deterministic results
  ```bash
  python main.py --mode evolve --seed 42
  ```

- **Issue**: "OpenVINO NPU not detected"
  - **Cause**: NPU driver not installed
  - **Solution**:
    - **Windows**: Install Intel NPU driver from Intel website
    - **Linux**: Install `intel-level-zero-gpu` package

---

## ✅ **Validation Checklist**
- [ ] Gen 0 accuracy: 62.0% ± 1.5%
- [ ] Gen 14 Bayesian discovery observed
- [ ] Gen 50 accuracy: 92.8% ± 0.5%
- [ ] Vibe Coding: 94% ± 2% success
- [ ] SAC detection: 94% ± 2%
- [ ] Gen 23 case: L_C = 0.847
- [ ] Digital Thymus: 100% self-correction
- [ ] All figures generated successfully

---

## 📧 **Support**
If you encounter issues:
1. Check [FAQ](docs/FAQ.md)
2. Open GitHub Issue
3. Email: support@bionexus-lab.org

**Last Updated**: 2026-03-09
**Tested Platforms**: Windows 11, Ubuntu 22.04
**Maintainer**: [Your Name]
