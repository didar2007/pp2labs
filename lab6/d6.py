from string import ascii_uppercase

def generate_a_to_z(folder="."):
    from pathlib import Path
    Path(folder).mkdir(parents=True, exist_ok=True)
    for ch in ascii_uppercase:
        fname = Path(folder) / f"{ch}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(f"This is file {ch}.txt\n")


generate_a_to_z("letters")
