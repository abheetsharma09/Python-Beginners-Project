# 📂 Project 02: File Extension Reporter (Version 1.0)

### 📝 Description
A Python utility designed to scan a directory and provide a count of all file types present. This project focuses on identifying unique file extensions and calculating their frequency within the local file system.

### 🚀 Logic & Approach
This version of the project uses a **multi-pass algorithm** to ensure data accuracy:
1.  **Safety Filter:** Implemented an `if "." in files` check. This prevents the script from crashing when it encounters folders or system files without extensions (avoiding `IndexError`).
2.  **Uniqueness via Sets:** Utilized a Python `set()` to automatically filter out duplicate extensions, creating a master list of unique file types.
3.  **Frequency Mapping:** Looped through the unique set and used the `.count()` method on the master list to populate a results dictionary.

### 🛠 Skills Demonstrated
* **File System Interaction:** Using `os.listdir()` to ingest filenames.
* **Data Structures:** Leveraging `Lists`, `Sets`, and `Dictionaries` in a single workflow.
* **Functional Programming:** Wrapping logic inside a reusable `file_func()` for cleaner execution.
* **Problem Solving:** Identifying and patching "Edge Case" crashes related to sub-folders.

### 📂 Files
* `extension_reporter.py`: The main script containing the counting logic.
* `README.md`: Project documentation.
