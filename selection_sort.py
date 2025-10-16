
import random

numbers = [random.randint(0,10) for i in range(10)]

print("Intial value:", numbers)


def selectionsort(values):

    for i in range(len(values) - 1):
        for j in range(i + 1, ):

            if j < i:



print("Sorted values =", selectionsort(numbers))