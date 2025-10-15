import re

text = "hello_world test_case Python_code some_Text more_tests"
a = re.findall(r'[a-z]+_[a-z]+', text)
print(a)