# Installation Guide

This guide provides detailed instructions on how to set up the **BioNexus-Dialectical-Protocol** environment.

---

## 🛠️ Step 1: System Requirements

### Hardware
- **CPU**: Intel Core Ultra series or 12th+ Gen Core processors.
- **GPU**: Intel Arc A-Series (A770 recommended) or Intel Arc iGPU.
- **NPU**: Intel AI Boost (optional, for low-power inference).
- **RAM**: Minimum 32 GB.

### OS
- Windows 11 (build 22621+)
- Ubuntu 22.04 LTS or 24.04 LTS

---

## 🏗️ Step 2: Dependencies

### 1. Python 3.11
We recommend using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
.\venv\Scripts\activate  # Windows
```

### 2. Intel oneAPI (Optional but Recommended)
For maximum GPU performance, install the [Intel oneAPI Base Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html).

### 3. Ollama
Install Ollama from [ollama.com](https://ollama.com) to run local LLMs.

---

## 📦 Step 3: Setup

```bash
# Install core dependencies
pip install -r requirements.txt

# Run Intel Arc optimization script
./scripts/setup_intel_oneapi.sh

# Pull required models
ollama pull llama3.2:3b-instruct-q4_K_M
ollama pull mistral-large-2
```

---

## ✅ Step 4: Verification

Run the verification script to ensure everything is configured correctly:
```bash
python benchmarks/verify_environment.py
```

Check the [FAQ](FAQ.md) if you encounter any issues.
