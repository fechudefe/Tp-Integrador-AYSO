lista_promedio = []
suma = 0
for i in range(10):
    while True:
        try:
            numero = int(input("Ingrese un numero entero: "))
        except ValueError:
            print("Error: Debe ingresar un numero entero")
        else:
            lista_promedio.append(numero)
            break

for numero in lista_promedio:
    suma += numero
print("---Promedio de los numeros ingresados---")
try:
    print(suma/10)
except ZeroDivisionError:
    print("Error: La suma de todos los números ingresados dio 0, por lo cual no se puede realizar el promedio. ")
