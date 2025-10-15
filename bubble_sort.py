# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(0, 10) for i in range(10)]
print(f"Initial Values = {values}")



# perform the bubblesort
for i in range(len(values) - 1):

    for j in range(len(values) -i -1):

        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]


print(f"Sorted Values = {values}")
