import datetime

# almacenar los gastos
gastos = []

def agregar_gasto():
    
    # Solicita datos del gasto
    fecha_str = input("Ingresa la fecha del gasto (formato DD-MM-AAAA): ")
    monto_str = input("Ingresa el monto del gasto: ")
    categoria = input("Ingresa la categoria del gasto por ejemplo, alimentos, transporte, entretenimiento: ")
    
    try:
        # Convierte la fecha a un objeto datetime
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
    except ValueError:
        print("Fecha invalida. Usa el formato DD-MM-AAAA.")
        return

    try:
        # Convierte el monto a un numero flotante
        monto = float(monto_str)
    except ValueError:
        print("Monto invalido. Por favor ingresa un numero.")
        return

    # Crea un diccionario para el nuevo gasto
    nuevo_gasto = {
        "fecha": fecha,
        "monto": monto,
        "categoria": categoria
    }

    # Agrega el nuevo gasto a la lista global
    gastos.append(nuevo_gasto)
    print("Gasto agregado exitosamente.")
