import re

text = "helloWorldPython"
a = re.sub(r'[A-Z]', r'_\1', text).lower()
print(a)