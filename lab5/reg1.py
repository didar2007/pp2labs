import re

text = "abbb"

a = re.match(r'ab*', text)
print(a)