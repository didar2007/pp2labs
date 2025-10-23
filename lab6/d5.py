def write_list_to_file(path, items):
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(f"{item}\n")

write_list_to_file("out.txt", ["apple", "banana", "cherry"])
