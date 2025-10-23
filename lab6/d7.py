import shutil
from pathlib import Path

def copy_file(src, dst):
    srcp = Path(src)
    if not srcp.exists() or not srcp.is_file():
        return False
    shutil.copyfile(src, dst)
    return True

print(copy_file("source.txt", "dest.txt"))
