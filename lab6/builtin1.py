def multiply_list(n):
    result = 1
    for i in n:
        result *= n
    return result

a = [1, 3, 4, 5]
print(multiply_list(a))