"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Andrea Dvorakova
email: csajka.andi@gmail.com
"""

from Functions import *
import random

if __name__ == '__main__':
    # uvod pro uzivatele
    ODDELOVAC = '-'*50
    print('Hi there!')
    print(ODDELOVAC)
    print("I've generated a random 4 digit number for you.\nLet's play bulls and cows game.")
    print(ODDELOVAC)

    # generovani 4mistniho random cisla
    n = str(random.randint(1000, 9999))
    n_list = convert(n)

    #pro rychlejsi testovani staci odmazat # pred printem
    print(n_list)
    # promenne pro pocitani
    bulls = 0
    cows = 0
    attempt = 1

    # cyklus pro hadani se zabudovanou funkci inputu a pocitani cows, bulls a pokusu
    while bulls != 4 and cows != 4:
        ui_num = erVal(print_promnt())
        ui_num_list = convert(ui_num)
        cows = cows_count(ui_num_list, n_list)
        bulls = bulls_count(ui_num_list, n_list)
        print(cows, ' cows and ', bulls, ' bulls')
        attempt += 1
    print("Correct, you've guessed the right number in ", attempt, ' guesses!')