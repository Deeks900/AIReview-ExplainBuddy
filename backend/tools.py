import os
from pathlib import Path

IGNORE_DIRS = {
    "node_modules", "__pycache__", ".venv", "venv", "env", ".git",
    ".idea", ".vscode", "dist", "build", "target", "coverage"
}

IGNORE_FILE_EXTENSIONS = {".lock", ".log"}

files = {}  # Global dict for file contents

#Let's first create the function that will be listing all the files in the directory or subdirectories
def listFiles():
    allFiles = []
    try:
        for filePath in files.keys():
            path = Path(filePath)
            if any(ignored_dir in path.parts for ignored_dir in IGNORE_DIRS):
                continue
            if path.suffix not in IGNORE_FILE_EXTENSIONS:
                allFiles.append(filePath)
    except Exception as e:
        print(f"Exception {e} in listFiles")
    finally:
        return allFiles



#Now let's create the other function to read those files 
def readFile(filePath):
    try:
        if filePath in files:
            return files[filePath]
        else:
            print(f"[readFile] File not found: {filePath}")
            return ""
    except Exception as e:
        print(f"[readFile] Exception: {e}")
        return ""


#Thirdly write a function to write the contents to the file delivered by llm 
def writeFile(filePath, content):
    isSuccess = True
    try:
        files[filePath] = content
        print("Data is written to file successfully.")
    except Exception as e:
        print(f"Exception {e} occurred in the writeFile function.")
        isSuccess = False
    finally:
        return isSuccess        