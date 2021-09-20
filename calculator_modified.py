def is_number(str):
  try:
    float(str)
    return True
  except ValueError:
    return False

print("Hello")

flag = True

while flag:
    a = input("Please, enter the first number:")
    while not is_number(a):
        a = input("Please, enter some number:")
    a = float(a)


    b = input("Choose your operation from +,-,*,/,^:")
    while b not in {'+','-','*','/','^'}:
        b = input("Please, enter some right symbol:")


    c = input("Please, enter the second number:")
    while not is_number(c):
        c = input("Please, enter some number:")
    c = float(c)


    if b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
    elif b == '*':
        print(a*c)
    elif b == '/':
        if c != 0:
            print(a/c)
        else:
            print("Error!")
    elif b == '^':
        if ((a == 0) and (c<=0)):
            print("Error!")
        else:
            print(a**c)

    f = input("Would you like to continue? print y/n:")
    while f not in {'y','n','Y','N'}:
        f = input("Would you like to continue? print y/n:")
        if f == 'n':
            flag = False
print("Thank you, see you later!")