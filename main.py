#como hacer un hola mundo con python
#Salida por consola

'''
print("Hola mundo")
print('Hola mundo')
'''

#entradas 
#datos primitivos
dato = None
nombre = "Alexis"
edad = 24
estatura = 1.76
hinchaDelMejor = True

#salida por teclado
print("hola" , nombre  , "Tu edad es" , edad)
print(f'hola {nombre} tu edad es {edad}')

#recibir datos por teclado
ciudad = input("Digita la ciudad donde vives: ")
print(f'La ciudad donde usted vive es: {ciudad}')

#recibir datos numericos por teclado
numero1 = int(input("Digita un numero: "))
numero2 = int(input("Digita otro numero: "))
print(f'El primer numero es: {numero1} y el segundo numero es: {numero2}')

#Operadores aritmeticos
#(+ - */ %)
suma = numero1 + numero2
print(f'el resultado de la suma es: {suma}')