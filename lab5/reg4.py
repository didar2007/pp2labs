import re

text = "Hello world Python Is Fun dog Cat apple"
a = re.findall(r'[A-Z][a-z]+', text)
print(a)