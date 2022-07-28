def print_promnt() -> str:
    # vyzva uzivatele pro zadani cisla
    num_in = str(input('Enter a number: '))
    return num_in

def erVal(num_in) -> str:
    # kontrola inputu od uzivatele jestli je to 4mistni cislo bez 0 na zacatku
    ODDELOVAC = '-' * 50
    print(ODDELOVAC)
    while (num_in.isdecimal() is not True) or (len(num_in) != 4) or (num_in[0] == '0'):
        num_in = str(input('Enter a 4digit number with no 0 in the first digit: '))
        print(ODDELOVAC)
    return num_in

def convert(string) -> list:
    # prevod stringu na list
    list1=[]
    list1[:0]=string
    return list1

def cows_count(n_ui, n_pc) -> int:
    # odstraneni duplicit a spocitani uhodnutych cisel
    n_ui = [*set(n_ui)]
    cows = 0
    for i in n_pc:
        if i in n_ui:
            cows += 1
        else:
            cows += 0
    return cows

def bulls_count(n_ui, n_pc) -> int:
    # pocitani uhodnutych cisel na spravne pozici
    bulls = 0
    for i in range(0, 4):
        if n_ui[i] == n_pc[i]:
            bulls += 1
        else:
            bulls += 0
    return bulls





