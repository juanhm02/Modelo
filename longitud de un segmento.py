import math

def longitud(x1,x2,y1,y2):
 resultado = math.sqrt((x2-x1)**2 + (y2-y1)**2)
 return resultado

x1 =int(input("primera funcion x"))
x2 =int(input("segunda funcion y"))
y1 =int(input("tercera funcion x"))
y2 =int(input("cuarta funcion y"))
ok=longitud(x1,x2,y1,y2)
print(ok)