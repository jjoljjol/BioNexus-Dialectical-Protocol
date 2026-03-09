# REPRODUCE.md

## Reproducing Paper Results

### Hardware Requirements
- CPU: Intel Core Ultra 7 255H (or equivalent)
- GPU: Intel Arc 140T (8 Xe-cores, 74 TOPS)
- NPU: Intel AI Boost NPU 3 (13 TOPS)
- RAM: 32 GB DDR5
- OS: Windows 11 Home 25H2 / Ubuntu 22.04

### Software Stack
- Python 3.11.8
- Ollama 0.1.x
- OpenVINO 2026.0.0
- Intel oneAPI Base Toolkit 2025.0

### Step-by-Step Instructions

#### 1. Environment Setup (15 minutes)
```bash
git clone https://github.com/jjoljjol/BioNexus-Dialectical-Protocol.git
cd BioNexus-Dialectical-Protocol
./scripts/setup_intel_oneapi.sh
pip install -r requirements.txt
```

#### 2. Pull LLM Models (10 minutes)
```bash
ollama pull llama3.2:3b-instruct-q4_K_M
ollama pull mistral-large-2
```

#### 3. Run Benchmark (Gen 0→50, ~4 hours)
```bash
python main.py --mode evolve --generations 50 --trials 5
```
**Expected Output:**
- Gen 0: 62.0% accuracy
- Gen 14: 87.2% (Bayesian discovery)
- Gen 50: 92.8%
- Results saved to `results/evolution_gen0_50.json`

#### 4. Reproduce Figures
```bash
python scripts/generate_figures.py --input results/ --output paper/figures/
```

#### 5. Reproduce Gen 23 SAC Case Study
```bash
python benchmarks/ajtert_case_study/reproduce_gen23.py
```

### Troubleshooting
- **Issue**: "NVML not found" → Expected on Intel Arc, use `--no-power`
- **Issue**: "Generation takes > 10 min" → Check Ollama GPU acceleration
- **Issue**: "Different accuracy values" → Stochastic variation, ±2% expected

### Citation
If you use this code, please cite:
```bibtex
@article{bionexus2026dialectical,
  title={The Dialectical Protocol: Self-Evolving AI via Bio-Inspired Vibe Coding},
  author={BioNexus AI Squad},
  journal={IEEE Transactions on Neural Networks and Learning Systems},
  year={2026}
}
```
