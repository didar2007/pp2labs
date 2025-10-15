import re

text = "acb a123b appleb aXYb testb ab axxxxb"


a = re.findall(r'a.*b', text)
print(a)