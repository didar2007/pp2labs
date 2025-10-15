import re

text = "HelloWorldPython"
a = re.split(r'?=[A-Z]', text)
print(a)