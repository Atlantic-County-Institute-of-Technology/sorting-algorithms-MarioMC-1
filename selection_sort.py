
import random

# numbers = [random.randint(0,10) for i in range(10)]

# print("Intial value:", numbers)


def selection_sort(numbers):
    for i in range(len(numbers)):
        temp = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[temp]:
                temp = j
        numbers[i], numbers[temp] = numbers[temp], numbers[i]
    return numbers

# print("Sorted values =", selection_sort(numbers))