a =int(input('numero 1'))
b =int(input('numero 2'))
if (a < b):
 for c in range(a, b+1): 
  print(c)
else: 
 for c in range(b, a+1):
  print(c)