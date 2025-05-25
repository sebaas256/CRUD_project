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
            return texto
        else:
            print("--------------------")
            print("Error: El campo no puede estar vacío.")
            print("--------------------")
            