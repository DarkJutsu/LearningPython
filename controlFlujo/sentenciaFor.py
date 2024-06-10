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