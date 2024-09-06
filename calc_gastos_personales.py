import os
import datetime
from tkinter import *
from tkcalendar import Calendar

def mostrar_menu():
    print("=== Calculadora de Gastos Personales ===")
    print("1. Agregar Ingresos")
    print("2. Agregar Gastos")
    print("3. Ver Resumen")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def agregar_ingreso():
    ingreso = float(input("Introduce la cantidad que desea ingresar: "))
    categoria_ingreso = input("Introduce la categoría a la que pertenece este ingreso: ")

    def grad_date():
        date_str = cal.get_date()
        month, day, year = date_str.split('/')
        formatted_date = f"{day}/{month}/{year}"
        
        print(f"Introduce la fecha del ingreso: {formatted_date}")
        date_label.config(text="Ingresa la fecha (DD/MM/AAAA): " + formatted_date)
        
        with open ("ingresos.txt", "a") as file:
            file.write(f"{ingreso},{categoria_ingreso},{formatted_date}\n")
            
        print(f"La cantidad {ingreso} ha sido guardada en la categoría {categoria_ingreso}, y en la fecha {formatted_date} correctamente.")
        root.destroy()
    
    root = Tk()
    root.geometry("300x300")
    
    cal = Calendar(root, selectmode='day', year=2024, month=9, day=6)
    cal.pack(pady=20)
    
    date_label = Label(root, text="Ingresa la fecha (DD/MM/AAAA): ")
    date_label.pack(pady=5)
    
    Button(root, text="Confirmar", command=grad_date).pack(pady=5)
    root.mainloop()

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
