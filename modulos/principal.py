from funciones.cuadrilatero import perimetro_cuadrilatero,area_cuadrilatero,volumen_cuadrilatero
from funciones.circunferencia import perimetro_circunferencia,area_circunferencia,volumen_circunferencia

def menu():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: Perímetro")
    print("2: Área")
    print("3: Volumen")
    print("0: Salir")
    print()
            
def sub_menu():
    print()
    print("¿Para qué figura geométrica?")
    print("1: Cuadrilátero")
    print("2: Circunferencia")
    print("0: Salir")
    print()

def programa_principal():
    while True:
        menu()
        opcion = input("Seleccione su opción (0-3): ")
        
        if opcion == "1":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Perímetro: {perimetro_cuadrilatero(ancho,largo)}")
                
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese el radio: "))
                print(f"Perímetro: {perimetro_circunferencia(radio)}")

            elif opcion_sub_menu == "0":
                return
            else:
                print("Opción Inválida!")

        elif opcion == "2":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Area cuadrilatero: {area_cuadrilatero(ancho,largo)}")

            elif opcion_sub_menu == "2":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Area Circunferencia: {area_circunferencia(ancho,largo)}")

            elif opcion_sub_menu == "0":
                return
            else:
                print ("opcion invalida")
                return

        elif opcion_sub_menu =="3":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"volumen cuadrilatero: {volumen_cuadrilatero(ancho,largo)}")
            elif opcion_sub_menu == "2":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Volumen Circunferencia: {volumen_circunferencia(ancho,largo)}")
                
            elif opcion == "0":
                print("saliendo del sistema...")
            break
        else:
            print("Opción inválida...")

programa_principal()