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

#2 Running program to add then inot json file
<img width="1496" alt="step 2" src="https://github.com/user-attachments/assets/389402c5-fd3e-4b5b-810d-4fab5fed5bab" />

#3 Showing the hashes
<img width="1496" alt="step 3" src="https://github.com/user-attachments/assets/eb8d403d-f1fe-4036-bd48-b108032a7905" />

#4 Cnangin text in one file through terminal in our case (in creal situation it could come from malicious script)
<img width="1496" alt="step 4" src="https://github.com/user-attachments/assets/bee5a83d-bf22-4fd9-8e3d-b0b7fbbb45cd" />

#5 Running programm again to chek for changes ( in our case one file is modified ) 
<img width="1496" alt="step 5" src="https://github.com/user-attachments/assets/2265b355-3482-4afa-91e3-c988d6bddd24" />

#6 Showing the new hashes
<img width="1495" alt="step 6" src="https://github.com/user-attachments/assets/b5f6dc04-e8d7-4c67-b9d9-7367e11433d2" />
