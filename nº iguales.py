a = int(input("numero 1?"))
b = int(input("numero 2?"))
c = int(input("numero 3?"))
if ( a == b == c ):
  print(3)
elif ( a == b )or( b == c )or( a == c ):
  print(2)
else:
  print(0)