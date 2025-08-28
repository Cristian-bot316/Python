#usamos el ciclo for para recorrer elementos de un grupo de datos

juegos = {"dota 2", "MK", "street fighter", "counter strike", "7daystodie"}
numeros = {10,20,30,40,50}
diccionario = {
    "nombre": "cristian","apellido":"taibo","edad": 17, "estudiante":True}


for juego in juegos:
    print(juego)
print ()
for numero in numeros:
    resultado = numero * numero
    print (f"el resultado de multiplicar {numero} * {numero} = {resultado}")

for num in range(5):
    print (num)
    
for num in range(5,15): 
    print (num)    

for num in range(5,15,3):
    print (num)

for elemento in enumerate(numeros):
    indice = elemento[0]
    valor = elemento[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

for elemento in diccionario:
    print(f"la clave del dato es:{elemento}")


print()
for elemento in diccionario.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f"la clave del dato es: '{clave}' y el valor es:'{valor}'")

conjunto = {"aquilez baeza",55,True,"comandos",23}

print()
for elemento in conjunto:
    if type(elemento) == str:
     print(elemento)
