#Crear un programa que convierta unidades de temperatura.
# 1.- El usuario debera ingresar el valor de T°.
# 2.- El usuario debera ingresar escala de T° ORIGINAL.
# 3.- El usuario debera ingresar escala de T° FINAL.
# 4.- El sistema debera entregar resultados de conversion.
#
# de °C a °K => °C + 273.15
# de °K a °C => °K - 273.15


# de °C a °F => (°C * 9/5) + 32
# de °F a °C => (°F - 32) * 9/5





# de °F a °K => (°F -32) * 5/9 + 273.15
# de °K a °F => ((°K -273.15) * 5/9) + 32

#definir variables
temp = float(input("ingrese su temperatura: "))
escala_inicial = input("indique escala inicial: C, F, K ").upper().strip()
escala_final = input("indique escala final: C, F, K ").upper().strip()
#crear funcion convertir temperatura
def convertidor_C(temp, inicio, final):
    resultado = 0
    if inicio == "K":
        if final == "C":
           resultado = temp - 273.15
        elif final == "F":
           resultado = ((temp -273.15) * 5/9) + 32
        else:
           print("escala final erronea")
    elif inicio == "C":
       if final == "K":
          resultado = temp + 273.15
       elif final == "F":
          resultado = (temp * 9/5) + 32
       else:
          print("escala final erronea")
    elif inicio == "F":
       if final == "K":
          resultado = (temp -32) * 5/9 + 273.15
       elif final == "C":
          resultado = (temp - 32) * 9/5
       else:
          print("escala final errronea")
    else:
       print("escala final erronea")
       
    print(f"{temp}°{inicio} = {resultado}°{final}")

convertidor_C(temp,escala_inicial,escala_final)
