# for

words=['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))

#COPIAR O CREAR UNA NUEVA COLECCION EN LA ITERACION

users={'Hans': 'active', 'Eleonore': 'inactive', 'Pedro': 'active'}
print(users)
for user, status in users.copy().items():
  if status=='inactive':
    del users[user]

print(users)

active_users={}
for user, status in users.items():
  if status=='active':
    active_users[user]=status

print(active_users)

#FUNCION range(), REALIZA SECUENCIAS NUMERICAS
for i in range(5):
  print(i)

print(list(range(5,10)))

print(list(range(0, 10, 3)))

#ITERAR EN LOS INDECES DE UNA SECUENCIA
secuencia=['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(secuencia)):
  print(i, secuencia[i])

print(sum(range(4)))

#SENTENCIAS break, continue & else EN BUCLES
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    #si el bucle no encuentra nada
    print(n, 'is a prime number')

#SENTENCIA continue CONTINUA CON LA SIGUIENTE ITERACION DEL CICLO
for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("found an odd number", num)

#SENTENCIA pass NO HACE NADA Se puede usar cuando una sentencia es requerida por la sintaxis pero el programa no requiere ninguna acción
while True:
  pass

class MyEmptyClass:
  pass