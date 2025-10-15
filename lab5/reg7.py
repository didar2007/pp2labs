import re

text = "hello_world_python"
a = re.sub(r'_([a--x])', lambda x: x.group(1).upper(), text)
print(a)