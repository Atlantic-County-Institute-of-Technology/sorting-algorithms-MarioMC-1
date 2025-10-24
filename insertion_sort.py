#import random
import random

# generate a list of 10 random numbers from -100 to 100
# numbers = [random.randint(0, 10) for i in range(10)]
# displays values before sort
# print("Unsorted values =", numbers)


def insertion_sort(numbers):
#
    for i in range(1, len(numbers)):
        #stores values of i inside of temp file so it can be used later
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
            numbers[j+1] = temp
    return numbers


# print("Sorted values =", insertion_sort(numbers))