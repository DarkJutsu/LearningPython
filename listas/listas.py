frutas=['manzana', 'pera', 'mango', 'fresa', 'sandia', 'banana', 'uva']
print(frutas)

#BUSCAR EN LAS LISTA POR EL INDEX
print(frutas[0])
print(frutas[-2])

#DEVUELVE UN RANGO DE LA LISTA
print(frutas[-4:])

#CONCATENACION DE LISTA
print(frutas + ['ceresa', 'kiwi', 'melon'])

#LISTAS MUTABLES
cubes=[1, 8, 27, 65, 125]
cubes[3]=4**3
print(cubes)

#AGREGAR ELEMENTOS AL FINAL DE LA LISTA
cubes.append(216)
cubes.append(7**3)
print(cubes)

#CUANDO IGUALAMOS UNA COPIA DEL OBJETO NUNCA DE HACE UNA COPIA, SI NO QUE APUNTA AL OBJETO EN MEMORIA
rgb=['red', 'green', 'blue']
rgba=rgb
print(id(rgb)==id(rgba))
rgba.append('alph')
print(rgb)

#HACER COPIAS DE OBJETOS " : "
correct_rgba=rgba[:]
correct_rgba[-1]='alpha'
print('rgba corregida: ', correct_rgba)
print(rgba)

#AL USAR EL OPERADOR " : " PODEMOS CAMBIAR LA LONGITUD DE LA LISTA O VACIARLA COMPLETAMENTE
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5]=['C', 'D', 'E']
print(letters)
letters[2:5]=[]
print(letters)
letters[:]=[]
print(letters)

#len CONTAR LOS ELEMENTOS DE LA LISTA
letters_size=['a', 'b', 'c', 'd', 'e']
print(len(letters_size))

#ANIDAR LISTAS
a=['a', 'b', 'c']
b=[1, 2, 3]
x=[a, b]
print(x)
print(x[0][1])

#SERIE DE FIBONACCI
q, w=0, 1
while q < 10:
  print(q, end=', ')
  q, w=w, q+w