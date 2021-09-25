# var is a position in memory
a = [1, 2, 3]
b = a
b.append(10)
print(a)

# things about cycle for
N = 10

for i in range (1,N):
    print ('hi')
else:
    print ('bye')

#2 deobjectivasion
for el,el2 in((1,2), (3,4), (5,6)):
    print(el,el2)

i,j,k = (1,2,3)
print(i,j,k)

i,j,k, *z = (1,2,3,4,5)

print(i,j,k,z)
z.append(10)
print(i,j,k,z)


