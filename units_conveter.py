def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


flag = True

while flag:

    b = input("Choose your system from F, C, K:")
    while b not in {'F', 'C', 'K'}:
        b = input("Please, enter some right symbol:")

    a = input("Please, enter the temperature value :")
    while not is_number(a):
        a = input("Please, enter some number:")
    a = float(a)

    c = input("Choose the result system from F, C, K:")
    while c not in {'F', 'C', 'K'}:
        c = input("Please, enter some right symbol:")

    if b == c:
        res = a

    else:
        if (b == 'C') and (c == 'K'):
            res = a + 273
        elif (b == 'C') and (c == 'F'):
            res = a * 9 / 5 + 32
        elif (b == 'K') and (c == 'C'):
            res = a - 273
        elif (b == 'K') and (c == 'F'):
            res = (a - 273) * 9 / 5 + 32
        elif (b == 'F') and (c == 'C'):
            res = (a - 32) * 5 / 9
        elif (b == 'F') and (c == 'K'):
            res = (a - 32) * 5 / 9 + 273
    print(res, c)
    f = input("Would you like to continue? print y/n:")
    while f not in {'y', 'n', 'Y', 'N'}:
        f = input("Would you like to continue? print y/n:")
    if f == 'n':
        flag = False
print("Thank you, see you later!")

