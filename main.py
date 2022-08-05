"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Andrea Dvorakova
email: csajka.andi@gmail.com
"""

from Functions import *
import random

if __name__ == '__main__':
    # user welcome
    ODDELOVAC = '-'*50
    print('Hi there!')
    print(ODDELOVAC)
    print("I've generated a random 4 digit number for you.\nLet's play bulls and cows game.")
    print(ODDELOVAC)

    # generate random 4digit number
    number_digit_first = ''.join(random.sample("123456789", 1))
    number_digits = ''.join(random.sample("0123456789", 3))
    n = (number_digit_first + number_digits)
    n_list = convert(n)

    #for quick testing print out the next row
    #print(n_list)
    # variables for counting
    bulls = 0
    cows = 0
    attempt = 1

    # loop for guessing with function for input and cows, bulls and attempt counting
    while bulls != 4 and cows != 4:
        ui_num = erVal(print_promnt())
        ui_num_list = convert(ui_num)
        cows = cows_count(ui_num_list, n_list)
        bulls = bulls_count(ui_num_list, n_list)
        print(cows, ' cows and ', bulls, ' bulls')
        attempt += 1
    print("Correct, you've guessed the right number in ", attempt, ' guesses!')