numero = int(input("Digite un numero entero "))

resultado = numero %3
print(f'el residuo es: {resultado}')

#condicional simple de python
if(resultado == 0):
    print("es multiplo de tres")
else:
    print("No es multiplo de tres")
print("Fin del programa")