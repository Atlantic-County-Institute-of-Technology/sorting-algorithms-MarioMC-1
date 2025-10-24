import os

import random

from bubble_sort import bubble_sort

from insertion_sort import insertion_sort

from selection_sort import selection_sort

print(input(" [-] こんにちは \n Please begin simulation"))
os.system('cls' if os.name == 'nt' else 'clear')
numbers = [random.randint(1, 100) for i in range(10)]
temp_numbers = str(numbers)

min_numbers = int(input("[-] What is the lowest value you want?"))
max_numbers = int(input("[-] What is the highest value you want?"))
amo_numbers = int(input("[-] How many numbers you want to see?"))
def main():
    selection_1 = 0
    selection_2 = 0
    shown = 0
    menu = 0

    while True:
        global numbers
        os.system('cls' if os.name == 'nt' else 'clear')

        print("[-] 0. Exit: \n"
              "[-] 1. Renter Numbers: \n"
              "[-] 2. Select Which Sort:")

        selection_1 = int(input("[-] Insert Number:"))

        if selection_1 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        if selection_1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            min_numbers = int(input("[-] What is the lowest value you want?"))
            max_numbers = int(input("[-] What is the highest value you want?"))
            amo_numbers = int(input("[-] What is the amount of numbers you want?"))
        if selection_1 == 2:
            s_menu()

def s_menu():
    selection_1 = 0
    selection_2 = 0
    shown = 0
    menu = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    print("[-] Select which sort you want.\n"
          "[-] 0. Menu\n"
          "[-] 1. Bubble Sort\n"
          "[-] 2. Insertion Sort\n"
          "[-] 3. Selection Sort")
    selection_2 = int(input("[-] Insert Number:"))
    if selection_2 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    if selection_2 == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f" Unsorted List: {temp_numbers}")
        bubble_sort(numbers)
        print(f" Sorted List: {numbers}")
        menu = int(input("[-] Do you want to go back to Menu (0) or Sort Menu (1)?"))
    if selection_2 == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f" Unsorted List: {temp_numbers}")
        insertion_sort(numbers)
        print(f" Sorted List: {numbers}")
        menu = int(input("[-] Do you want to go back to Menu (0) or Sort Menu (1)?"))
    if selection_2 == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f" Unsorted List: {temp_numbers}")
        selection_sort(numbers)
        print(f" Sorted List: {numbers}")
        menu = int(input("[-] Do you want to go back to Menu (0) or Sort Menu (1)?"))
    if menu == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    if menu == 1:
        s_menu()


if __name__ == "__main__":
    main()