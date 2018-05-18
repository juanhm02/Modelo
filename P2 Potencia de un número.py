def potencia(x,n):
  resultado=1
  for i in range(0,n):
   
    resultado=resultado*x

  return resultado




x = int(input("numero 1"))
n = int(input("numero entero"))
salida=potencia (x,n)
print(salida)