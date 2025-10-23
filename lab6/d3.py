from pathlib import Path

def path_info(path):
    p = Path(path)
    exists = p.exists()
    if not exists:
        return {"exists": False}
    return {
        "exists": True,
        "is_file": p.is_file(),
        "is_dir": p.is_dir(),
        "directory": str(p.parent),
        "filename": p.name
    }

print(path_info("some/file.txt"))
