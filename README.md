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
- Works through a simple **GUI** or terminal input
  
---


