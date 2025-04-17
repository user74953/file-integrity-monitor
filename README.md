# file-integrity-monitor

Python project that detects file changes (added, modified, or deleted) in any folder using SHA-256 hashing.

---
## 🔍 What It Does

- Scans a folder and calculates a hash for every file
- Saves the hashes to a `.json` file
- Compares files on the next scan to detect:
  - Modified files
  - Deleted files
  - New files added
- Works through a simple terminal input
  
---

#1 Creating test folder

<img width="1496" alt="step 1" src="https://github.com/user-attachments/assets/966da14e-f0df-42e5-bd68-d22337238cd7" />

