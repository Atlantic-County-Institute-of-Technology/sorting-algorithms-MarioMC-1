
import random

values = [random.randint(0,10) for i in range(10)]

print("Intial value:", values)
# min_value = i
max_value = 0
for i in range(len(values) - 1):
    min_value = i
    for j in range(i + 1, ):

        if j < min_value:
            min_value = j
            values[j], values[i] = values[i], values[j]
print(f"Sorted Values = {values}")