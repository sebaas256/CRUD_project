from utils.ascii import mostrar_titulo

def menu_principal():
    print("--------------------")
    print("1-pacientes")
    print("2-Citas")
    print("3-Consultas")
    print("4-Salir")

def mostrar_menu():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("--------------------")
            print("Has seleccionado Pacientes")
            pacientes()
        elif opcion == "2":
            print("--------------------")
            print("Has seleccionado Citas")
            citas()
        elif opcion == "3":
            print("--------------------")
            print("Has seleccionado Consultas")
            consultas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def pacientes():
    while True:
        print("1-Agregar Paciente")
        print("2-Eliminar Paciente")
        print("3-Actualizar Paciente")
        print("4-Consultar Paciente")
        print("5-Volver al menu principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            #Codigo para agregar paciente (importar de logica)
            print("")
        elif opcion == "2":
            #Codigo para eliminar paciente (importar de logica)
            print("")
        elif opcion == "3":
            #Codigo para actualizar paciente (importar de logica)
            print("")
        elif opcion == "4":
            #Codigo para consultar paciente (importar de logica)
            print("")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def citas():
    while True:
        print("1-Agregar cita")
        print("2-Eliminar cita")
        print("3-Actualizar cita")
        print("4-Consultar cita")
        print("5-Volver al menu principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            #Codigo para agregar paciente (importar de logica)
            print("")
        elif opcion == "2":
            #Codigo para eliminar paciente (importar de logica)
            print("")
        elif opcion == "3":
            #Codigo para actualizar paciente (importar de logica)
            print("")
        elif opcion == "4":
            #Codigo para consultar paciente (importar de logica)
            print("")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def consultas():
    while True:
        print("1-Agregar consulta")
        print("2-Eliminar consulta")
        print("3-Actualizar consulta")
        print("4-Consultar consulta")
        print("5-Volver al menu principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            #Codigo para agregar paciente (importar de logica)
            print("")
        elif opcion == "2":
            #Codigo para eliminar paciente (importar de logica)
            print("")
        elif opcion == "3":
            #Codigo para actualizar paciente (importar de logica)
            print("")
        elif opcion == "4":
            #Codigo para consultar paciente (importar de logica)
            print("")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    mostrar_titulo()
    mostrar_menu()
