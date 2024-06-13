# Learning Python

[by documentación 3.12.4]("https://docs.python.org/es/3/tutorial/")

## Listas
## Control de Flujo
1. > **if & elif**
    - Puede haber cero o más bloques elif, y el bloque else es opcional. La palabra reservada elif es una abreviación de “else if”, y es útil para evitar un sangrado excesivo. Una secuencia if … elif … elif … sustituye las sentencias switch o case encontradas en otros lenguajes. Si necesitas comparar un mismo valor con muchas constantes, o comprobar que tenga un tipo o atributos específicos puede que encuentres útil la sentencia match.

    ```python
    if x < 0:
      x = 0
      print('Negative changed to zero')
    elif x == 0:
      print('Zero')
    else:
      print('x greater than zero')
    ```

2. > **for**
    - La sentencia for en Python difiere un poco de lo que uno puede estar acostumbrado en lenguajes como C o Pascal. En lugar de siempre iterar sobre una progresión aritmética de números (como en Pascal) o darle al usuario la posibilidad de definir tanto el paso de la iteración como la condición de fin (como en C), la sentencia for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia.

    ```python
    words = ['cat', 'window', 'defenestrate']
    for w in words:
      print(w, len(w))
    ```
    - **Sentencias break, continue & else**
      - **break**: La sentencia break termina el bucle for o while más anidado.
      - **else**: Un bucle for o while puede incluir una cláusula else. En un bucle for, la cláusula else se ejecuta después de que el bucle alcance su iteración final. En un bucle while, se ejecuta después de que la condición del bucle se vuelva falsa. En cualquier tipo de bucle, la cláusula else no se ejecuta si el bucle ha finalizado con break.
      - **continue**:La declaración continue, también tomada de C, continua con la siguiente iteración del ciclo.

3. >**Pass**
    - La sentencia pass no hace nada. Se puede usar cuando una sentencia es requerida por la sintaxis pero el programa no requiere ninguna acción.

    ```python
    while True:
      pass

    class MyEmptyClass:
      pass
    ```
