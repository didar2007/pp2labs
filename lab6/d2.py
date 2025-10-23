import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return {"exists": exists, "readable": readable, "writable": writable, "executable": executable}


print(check_access("some/path/here"))
