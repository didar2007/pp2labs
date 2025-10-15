import re

text = "I am, Didar Kalabayev."
a = re.sub(r'[ ,.]', ':', text)
print(a)