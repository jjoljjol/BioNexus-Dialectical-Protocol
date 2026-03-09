# Contributing to BioNexus-Dialectical-Protocol

Thank you for your interest in contributing! 🎉

---

## 🤝 **How to Contribute**

### **Types of Contributions**

1. **🐛 Bug Reports**: Found a bug? Open an issue.
2. **✨ Feature Requests**: Have an idea? Discuss in Discussions.
3. **📝 Documentation**: Improve docs, add examples.
4. **🧪 Benchmarks**: Add new evaluation datasets.
5. **🔧 Code**: Fix bugs, add features.

---

## 🚀 **Getting Started**

### **Step 1: Fork & Clone**
```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/BioNexus-Dialectical-Protocol.git
cd BioNexus-Dialectical-Protocol
git remote add upstream https://github.com/original/BioNexus-Dialectical-Protocol.git
```

### **Step 2: Create Branch**
```bash
git checkout -b feature/your-feature-name
```

### **Step 3: Make Changes**
- Follow code style (see below).
- Add tests if applicable.
- Update documentation.

### **Step 4: Test**
```bash
pytest tests/
python benchmarks/verify_environment.py
```

### **Step 5: Submit PR**
```bash
git push origin feature/your-feature-name
# Then create Pull Request on GitHub
```

---

## 📏 **Code Style**

- **Python**: Follow PEP 8.
- **Docstrings**: Google style.
- **Type Hints**: Required for new code.
- **Line Length**: 88 characters (Black formatter).

**Example**:
```python
def identify_pathogens(
    source_code: str,
    threshold: float = 0.75
) -> List[Dict[str, Any]]:
    """
    Identify logical pathogens in source code.
    
    Args:
        source_code: Python source code to analyze
        threshold: Detection threshold (0-1)
        
    Returns:
        List of detected pathogens with metadata
        
    Example:
        >>> pathogens = identify_pathogens(code, threshold=0.8)
        >>> print(len(pathogens))
        3
    """
    ...
```

---

## ✅ **Pull Request Checklist**
- [ ] Code follows style guidelines
- [ ] Tests pass (`pytest tests/`)
- [ ] Documentation updated
- [ ] `CHANGELOG.md` updated
- [ ] No merge conflicts
- [ ] PR description explains changes

---

## 📝 **Commit Messages**
Use conventional commits:
- `feat: Add Bayesian weighting module`
- `fix: Resolve Merkle validation bug`
- `docs: Update REPRODUCE.md`
- `test: Add SAC unit tests`

---

## 🐛 **Reporting Bugs**
Use the bug report template:

**Good Bug Report**:
```text
**Bug**: SAC false positive on valid entity pairs

**Environment**:
- OS: Windows 11
- Python: 3.11.8
- OpenVINO: 2026.0.0

**Steps to Reproduce**:
1. Run `python benchmarks/sac_validation.py`
2. Observe false positive on case #45

**Expected**: L_C = 0.32 (valid)
**Actual**: L_C = 0.78 (flagged)

**Logs**:
[Paste relevant logs]
```

---

## 💬 **Questions?**
- **General**: Use GitHub Discussions
- **Bugs**: Open an Issue
- **Email**: dev@bionexus-lab.org

Thank you for contributing! 🙏
