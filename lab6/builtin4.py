import math
import time

def delayed_sqrt(n, m):
    time.sleep(m/1000)
    return math.sqrt(n)

num = int(input("num: "))
ms = int(input("ms: "))

result = delayed_sqrt(num, ms)
print(f"Square root of {num} after {ms} milliseconds is {result}")