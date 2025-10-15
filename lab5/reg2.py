import re
text = "abbb"

a = re.match(r'ab{2,3}', text)
print(a)
