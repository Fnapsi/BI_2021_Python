def is_number(str):
  try:
    float(str)
    return True
  except ValueError:
    return False

a = input()
while not is_number(a):
    a = input()
a = float(a)


b = input()
while b not in {'+','-','*','/','^'}:
    b = input()


c = input()
while not is_number(c):
    c = input()
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

