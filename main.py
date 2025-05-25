from utils.ascii import mostrar_titulo
from DB import Conexion as con
from logica import Pacientes as pa
import os

con = con.Conexion()

def menu_principal():
    print("--------------------")
    print("1-pacientes") #--Kevin
    print("2-Citas") #--Alexis
    print("3-Consultas") #--Andrea
    print("4-Doctores") #--Sebas
    print("5-Salir")

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
            print("--------------------")
            print("Has seleccionado Doctores")
            doctores()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("--------------------")
            print("Opción no válida. Intente de nuevo.")

def pacientes():
    while True:
        print("1-Agregar Paciente")
        print("2-Eliminar Paciente")
        print("3-Actualizar Paciente")
        print("4-Consultar Paciente")
        print("5-Volver al menu principal")
        opcion = input("Seleccione una opción: ")
        
        #Limpiar consola
        os.system('cls')
        
        if opcion == "1":
            
            #variables
            Dui = input("Digite el DUI del paciente: ")
            Nombres = input("Digite el nombres del paciente: ")
            Apellidos = input("Digite el apellidos del paciente: ")
            Fecha_Nacimiento = input("Digite la fecha de nacimiento del paciente (AAAA-MM-DD): ")
            
            Tel_int = int(input("Digite el telefono del paciente: "))
            Tel = str(Tel_int)
            Telefono = Tel.replace(" ", "")
            
            Direccion = input("Digite la direccion del paciente: ")
            Correo = input("Digite el correo del paciente: ")
            #Agregar Paciente
            pa.AgregarPacientes(con, Dui, Nombres, Apellidos, Fecha_Nacimiento, Telefono,Direccion, Correo)
                
        elif opcion == "2":
            
            #variables
            Dui = int(input("Digite el DUI del paciente que quiere eliminar:"))
            #Eliminar Paciente
            pa.EliminarPaciente(con, Dui)
                
        elif opcion == "3":

            #variables
            Dui = input("Digite el DUI del paciente a quien desea modificar: ")
            Nombres = input("Digite el nombres del paciente: ")
            Apellidos = input("Digite el apellidos del paciente: ")
            Fecha_Nacimiento = input("Digite la fecha de nacimiento del paciente (AAAA-MM-DD): ")
            
            Tel_int = int(input("Digite el telefono del paciente: "))
            Tel = str(Tel_int)
            Telefono = Tel.replace(" ", "")
            
            Direccion = input("Digite la direccion del paciente: ")
            Correo = input("Digite el correo del paciente: ")
            dui = input("Digite el nuevo DUI del paciente: ")
            
            # Codigo para actualizar paciente (importar de logica)
            pa.ActualizarPaciente(con, dui, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo, Dui)
            
        elif opcion == "4":
            
            #variables
            Dui = input("Digite el DUI del paciente que quiere buscar: ")
            # Codigo para consultar paciente (importar de logica)
            pa.BuscarPaciente(con, Dui)            
            
        elif opcion == "5":
            break
        else:
            print("--------------------")
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
            print("--------------------")
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
            print("--------------------")
            print("Opción no válida. Intente de nuevo.")


#Pupusas de queso

if __name__ == "__main__":
    mostrar_titulo()
    mostrar_menu()
