import os

from bubble_sort import bubble_sort

from insertion_sort import insertion_sort

from selection_sort import selection_sort
# [-]
print(input(" [-] こんにちは \n Please begin simulation"))
os.system('cls' if os.name == 'nt' else 'clear')
# temp_numbers = str(numbers)

min_numbers = int(input("[-] What is the lowest value you want?"))
max_numbers = int(input("[-] What is the highest value you want?"))
amo_numbers = int(input("[-] How many numbers you want to see?"))
def main()

    selection_1 = 0
    selection_2 = 0
    shown = 0
    menu = 0

    while True:
        global amo_numbers
        os.system('cls' if os.name == 'nt' else 'clear')

        print("[-] 0. Exit: \n"
              "[-] 1. Renter Numbers: \n"
              "[-] 2. Select Which Sort:")

        selection_1 = int(input("[-] Insert Number:"))

