from pathlib import Path

def list_dir_files(path):
    p = Path(path)
    if not p.exists():
        return {"error": "Path does not exist"}

    dirs  = [str(x) for x in p.iterdir() if x.is_dir()]
    files = [str(x) for x in p.iterdir() if x.is_file()]
    all_items = [str(x) for x in p.iterdir()]

    return {"dirs": dirs, "files": files, "all": all_items}

print(list_dir_files("."))
