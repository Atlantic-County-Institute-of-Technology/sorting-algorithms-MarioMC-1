# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
# numbers = [random.randint(0, 10) for i in range(10)]
# print("Initial Values", numbers)



# perform the bubblesort
def bubble_sort(numbers):
    for i in range(len(numbers) - 1):

        for j in range(len(numbers) - i - 1):

            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# print("Sorted values =", bubble_sort(numbers))