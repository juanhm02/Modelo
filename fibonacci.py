fibonacci=[]
a0=1
a1=1
num = int(input("Numero de elementos:"))
for n in range(num):
    fibonacci.append(a0+a1)
    aux = a0 + a1
    a0 = a1
    a1 = aux
print(fibonacci)