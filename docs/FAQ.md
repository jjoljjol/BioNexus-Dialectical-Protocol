# FAQ (Frequently Asked Questions)

### Q1: Why use Intel Arc A770 specifically?
**A**: Our SAC algorithm and Digital Thymus use INT8/FP16 quantization optimized for the Xe-HPG architecture, providing superior throughput for local LLM inference compared to standard iGPUs.

### Q2: Can I run this with NVIDIA GPUs?
**A**: Yes, but you will need to modify the `setup_intel_oneapi.sh` script to use CUDA/cuDNN instead of OpenVINO. Power telemetry features are currently exclusive to Intel Sysman.

### Q3: How do I resolve "Ollama connection refused"?
**A**: Ensure the Ollama background service is running. On Windows, check the tray icon. On Linux, run `systemctl status ollama`.

### Q4: Genetic accuracy isn't reaching 92%. What's wrong?
**A**: Small variations are normal due to LLM temperature settings. Try increasing `--trials` to 10 for more stable averages. Ensure you are using `llama3.2:3b-instruct-q4_K_M`.
