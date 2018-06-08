import math

def longitud(x1,x2,y1,y2):
  resultado=1
  for i in range(0,y1):
    resultado = resultado*x1*x2*y1*y2
    
  return resultado


x1 =int(input("primera funcion x"))
x2 =int(input("segunda funcion y"))
y1 =int(input("tercera funcion x"))
y2 =int(input("cuarta funcion y"))
salida =longitud(x1,x2,y1,y2)
print(salida)
