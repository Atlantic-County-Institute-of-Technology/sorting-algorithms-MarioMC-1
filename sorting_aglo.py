import random

from bubble_sort import bubblesort

values = [random.randint(-10,10) for i in range(20)]
print(f"Initial Values = {values}")
bubblesort(values)
print(f"Sorted Values = {values}")