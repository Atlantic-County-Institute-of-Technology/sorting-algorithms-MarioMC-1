#import random
import random

# generate a list of 10 random numbers from -100 to 100
numbers = [random.randint(0, 10) for i in range(10)]
# displays values before sort
print("Unsorted values =", numbers)


def insertion_sort(values):
#
    for i in range(1, len(values)):
        #stores values of i inside of temp file so it can be used later
        temp = values[i]
        j = i - 1
        while j >= 0 and temp < values[j]:
            values[j+1] = values[j]
            j -= 1
            values[j+1] = temp
    return values


print("Sorted values =", insertion_sort(numbers))
