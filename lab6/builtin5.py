def all_true(t):
    return all(t)

data = (True, True, True)
print(all_true(data))

data2 = (True, False, True)
print(all_true(data2))