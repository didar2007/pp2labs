import os
from pathlib import Path

def safe_delete(path):
    p = Path(path)
    if not p.exists():
        return {"deleted": False, "reason": "not exists"}
    if not os.access(path, os.W_OK):
        return {"deleted": False, "reason": "no write access"}
    try:
        p.unlink()
        return {"deleted": True}
    except Exception as e:
        return {"deleted": False, "reason": str(e)}

print(safe_delete("temp.txt"))
