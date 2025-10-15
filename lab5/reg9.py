import re

text = "HelloWorldPython"
a = re.sub(r'?=[A-Z]', ' ', text).strip()
print(a)