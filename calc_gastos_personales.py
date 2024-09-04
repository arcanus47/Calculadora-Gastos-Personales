import os
import datetime

def mostrar_menu():
    print("=== Calculadora de Gastos Personales ===")
    print("1. Agregar Ingresos")
    print("2. Agregar Gastos")
    print("3. Ver Resumen")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def agregar_ingreso():
    pass

def agregar_gasto():
    pass

def ver_resumen():
    pass

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_ingreso()
        elif opcion == "2":
            agregar_gasto()
        elif opcion == "3":
            ver_resumen()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
