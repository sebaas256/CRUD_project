def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError as e:
            print("--------------------")
            print(f"Error: Por favor ingrese un numero entero valido")
            print("--------------------")

def validar_telefono(mensaje):
    while True:
        telefono = int(input(mensaje))
        if len(str(telefono)) == 8:
            return telefono
        else:
            print("--------------------")
            print("Error: El numero de telefono debe tener 8 digitos.")
            print("--------------------")

def validar_correo(mensaje):
    while True:
        correo = input(mensaje)
        if "@" in correo and "." in correo:
            return correo
        else:
            print("--------------------")
            print("Error: El correo debe contener '@' y '.'")
            print("--------------------")
            
def validar_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip():  # Verifica que no sea solo espacios en blanco
            if all(c.isalpha() or c.isspace() or c in ",." for c in texto):
                return texto
            else:
                print("--------------------")
                print("Error: El campo no puede contener numeros.")
                print("--------------------")
        else:
            print("--------------------")
            print("Error: El campo no puede estar vacío.")
            print("--------------------")

def validar_fecha(mensaje):
    from datetime import datetime
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("--------------------")
            print("Error: Formato de fecha inválido. Use 'AAAA-MM-DD'.")
            print("--------------------")

def validar_Fecha_Hora(mensaje):
    from datetime import datetime
    while True:
        fecha_str = input(mensaje)
        try:
            if "-" in fecha_str and ":" not in fecha_str:
                return datetime.strptime(fecha_str, "%Y-%m-%d-%H-%M")
            else:
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            return fecha
        except ValueError:
            print("--------------------")
            print("Error: Formato de fecha inválido. Use 'AAAA-MM-DD-HH-MM'.")
            print("--------------------")

#ESTADOS- transformar estados bool a string 
def validar_estado():
    ESTADOS = {
        0: (True, "Pendiente"),
        1: (False, "Completada"),
        3: (False, "Cancelada")
    }

    while True:
        print("\nEstados disponibles:")
        print("0. Pendiente")
        print("1. Completada")
        print("3. Cancelada")
        
        try:
            opcion_estado = int(input("Estado (0-Pendiente, 1-Completada, 3-Cancelada): "))
            if opcion_estado in ESTADOS:
                return ESTADOS[opcion_estado] #s
            else:
                print("--------------------")
                print("Error: Opción inválida.")
                print("--------------------")
        except ValueError:
            print("--------------------")
            print("Error: Por favor ingrese un número válido.")
            print("--------------------")
            
def validar_dui(mensaje):
    while True:
        try:
            valor = input(mensaje)
            if valor.isdigit(): 
                if len(valor) == 9:
                    return valor    
                else:
                    print("--------------------")
                    print(f"Error: Ingrese los 9 digitos de su DUI!!!")
                    print("--------------------")
            else:
                raise Exception("")
        except Exception as e:
            print("--------------------")
            print("Error: Por favor ingrese un numero entero valido")
            print("--------------------")
