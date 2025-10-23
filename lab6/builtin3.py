def is_palidrome(s):
    return s == s[::-1]

t = "level"
if is_palidrome(t):
    print("Yes")
else:
    print("No")