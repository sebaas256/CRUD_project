from utils.ascii import mostrar_titulo
from DB import Conexion as con
from logica import Pacientes as pa
from logica import Citas as cit
from logica import Doctores as doc
from logica import Consultas as cons

from utils.validaciones import * 
import os

con = con.Conexion()

def menu_principal():
    print("--------------------")
    print("0-Salir")
    print("1-pacientes") #--Kevin
    print("2-Citas") #--Alexis
    print("3-Consultas") #--Andrea
    print("4-Doctores") #--Sebas

def mostrar_menu():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("--------------------")
            os.system('cls')
            pacientes()
        elif opcion == "2":
            print("--------------------")
            os.system('cls')
            citas()
        elif opcion == "3":
            print("--------------------")
            os.system('cls')
            consultas()
        elif opcion == "4":
            print("--------------------")
            os.system('cls')
            doctores()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("--------------------")
            print("Opción no válida. Intente de nuevo.")

def pacientes():
    while True:
        print("Has seleccionado Pacientes")
        print("0-Volver al menu principal")
        print("1-Agregar Paciente")
        print("2-Eliminar Paciente")
        print("3-Actualizar Paciente")
        print("4-Consultar Paciente")
        print("5-Mostrar todos los pacientes")
        print("6-Mostrar citas de un paciente")
        
        opcion = input("Seleccione una opción: ")
        
        #Limpiar consola
        os.system('cls')
        
        if opcion == "1":
            
            #variables
            Dui = validar_entero("Digite el DUI del paciente: ")
            Nombres = validar_texto("Digite el nombres del paciente: ")
            Apellidos = validar_texto("Digite el apellidos del paciente: ")
            Fecha_Nacimiento = validar_fecha("Digite la fecha de nacimiento del paciente (AAAA-MM-DD): ")
            Telefono = validar_telefono("Digite el telefono del paciente: ")
            Direccion = validar_texto("Digite la direccion del paciente: ")
            Correo = validar_correo("Digite el correo del paciente: ")
            #Agregar Paciente
            pa.AgregarPacientes(con, Dui, Nombres, Apellidos, Fecha_Nacimiento, Telefono,Direccion, Correo)


        elif opcion == "2":
            
            #variables
            Dui = validar_entero("Digite el DUI del paciente que quiere eliminar:")
            #Eliminar Paciente
            pa.EliminarPaciente(con, Dui)
                
        elif opcion == "3":

            #variables
            Dui = validar_entero("Digite el DUI del paciente a quien desea modificar: ")
            Nombres = validar_texto("Digite el nombres del paciente: ")
            Apellidos = validar_texto("Digite el apellidos del paciente: ")
            Fecha_Nacimiento = validar_fecha("Digite la fecha de nacimiento del paciente (AAAA-MM-DD): ")
            Telefono = validar_telefono("Digite el telefono del paciente: ")
            Direccion = validar_texto("Digite la direccion del paciente: ")
            Correo = validar_correo("Digite el correo del paciente: ")
            dui = validar_entero("Digite el nuevo DUI del paciente: ")
            
            # Codigo para actualizar paciente (importar de logica)
            pa.ActualizarPaciente(con, dui, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo, Dui)
            
        elif opcion == "4":
            
            #variables
            Dui = validar_entero("Digite el DUI del paciente que quiere buscar: ")
            # Codigo para consultar paciente (importar de logica)
            pa.BuscarPaciente(con, Dui)            
            
        elif opcion == "5":
            
            pa.MostrarPacientes(con)
        
        elif opcion == "6":
            
            Dui = validar_entero("Digite el DUI del paciente que quiere buscar: ")
            pa.ConsultarCitas(con,Dui)
        
        elif opcion == "0":
            break
        else:
            print("--------------------")
            print("Opción no v1álida. Intente de nuevo.")
            print("--------------------")
            
#CITAS------

def citas():
    while True:
        print("Has seleccionado Citas")
        print("0-Volver al menu principal")
        print("1-Agregar cita")
        print("2-Eliminar cita")
        print("3-Actualizar cita")
        print("4-Consultar cita")
        print("5-Ver citas")
        opcion = input("Seleccione una opción: ")
        
        os.system('cls')
        
        if opcion == "0":
            break

#Codigo para agregar paciente (importar de logica)
        if opcion == "1":
            print("\n AGREGAR CITA")
            id_cita = validar_entero("ID de la cita: ")
            fecha_cita = validar_Fecha_Hora("Fecha (AAAA-MM-DD HH:MM): ")
            consultorio = input("Consultorio: ")
            descripcion = input("Descripción: ")
            estado_cita = 0           
            dui_paciente = input("DUI del paciente: ")
            if cit.agregar_cita(con, id_cita, fecha_cita, consultorio, descripcion, estado_cita, dui_paciente):
                        print("¡CITA AGREGADA!")
                        print("=" * 60)
                        print(f"\nDETALLES DE LA CITA:")
                        print(f"ID Cita: {id_cita}")
                        print(f"Fecha y Hora: {fecha_cita}")
                        print(f"Consultorio: {consultorio}")
                        print(f"Descripción: {descripcion}")
                        print(f"Estado: {'Pendiente' if estado_cita == 0 else 'Completada'}")
                        print(f"DUI Paciente: {dui_paciente}")
                        print("=" * 60)

            else:
                        print("No se pudo agregar. Verifique los datos.")
            

#Codigo para eliminar cita 
        elif opcion == "2":
            id_cita = validar_entero("ID de la cita a eliminar: ")
            if cit.eliminar_cita(con, id_cita):
                print("\n" + "="*60)
                print("Cita eliminada!")
                print("\n" + "="*60)

#Codigo para actualizar cita (importar de logica)
        elif opcion == "3":
            id_cita = validar_entero("ID de la cita: ")
            nueva_fecha = validar_Fecha_Hora("Nueva fecha (AAAA-MM-DD HH:MM): ")
            nuevo_consultorio = validar_texto ("Inserte nuevo consultorio:  " )
            nueva_descripcion = validar_texto ("Inserte nueva descripcion:  ")
            #nuevo_estado = validar_estado()
            if cit.actualizar_cita(con, id_cita, nueva_fecha, nuevo_consultorio, nueva_descripcion):
                    print("\n" + "="*60)
                    print("Cita actualizada!")
                    print("Los Nuevos datos son")
                    print(f"{'ID Cita:':<25} {id_cita}") 
                    print(f"{'Nueva Fecha:':<25} {nueva_fecha}")
                    print(f"{'Nuevo consultorio:':<25} {nuevo_consultorio}")
                    print(f"{'Nueva descripcion:':<25} {nueva_descripcion}")
                    #print(f"{'Estado:':<25} {nuevo_estado}") 
                    print("=" * 60 + "\n")

            else:
                print("Error al Actualizar la cita.")
#Codigo para consultar cita (importar de logica
        elif opcion == "4":
                id_cita = validar_entero("ID de la cita: ")
                cit.consultar_cita(con, id_cita)

#5
        elif opcion == "5":
                cit.MostrarCitas(con)
#end
        else:
                print("\n" + "="*60)
                print("Opción no válida. Intente de nuevo.")
                print("\n" + "="*60)

            

#------/*


def consultas():
    while True:
        print("Has seleccionado Consultas") 
        print("0-Volver al menu principal")
        print("1-Agregar consulta")
        print("2-Eliminar consulta")
        print("3-Actualizar consulta")
        print("4-Buscar consulta")
        print("5-Mostrar todas las consultas")
        opcion = input("Seleccione una opción: ")

        #Limpiar consola
        os.system('cls')
        if opcion == "0":
            break

        elif opcion == "1":
            Id_Consulta = validar_entero("Digite el Id de la consulta: ")
            Diagnostico = validar_texto("Digite el diagnostico de la consulta: ")
            Observaciones = validar_texto("Digite las observaciones de la consulta: ")
            Fecha_Consulta = validar_fecha("Digite la fecha de la consulta (AAAA-MM-DD): ")
            ID_Doctor = validar_entero("Digite el Id del doctor que atendió la consulta: ")
            ID_Cita = validar_entero("Digite el Id de la cita asociada a la consulta: ")
            cons.agregar_consulta(con, Id_Consulta, Diagnostico, Observaciones, Fecha_Consulta, ID_Doctor, ID_Cita)

        elif opcion == "2":
            Id_Consulta = validar_entero("Digite el Id de la consulta que desea eliminar: ")
            cons.eliminar_consulta(con, Id_Consulta)
            
        elif opcion == "3":
            Id_Consulta = validar_entero("Digite el Id de la consulta que desea actualizar: ")
            Diagnostico = validar_texto("Digite el nuevo diagnostico de la consulta: ")
            Observaciones = validar_texto("Digite las nuevas observaciones de la consulta: ")
            Fecha_Consulta = validar_fecha("Digite la nueva fecha de la consulta (AAAA-MM-DD): ")
            ID_Doctor = validar_entero("Digite el nuevo Id del doctor que atendió la consulta: ")
            ID_Cita = validar_entero("Digite el nuevo Id de la cita asociada a la consulta: ")
            cons.actualizar_consulta(con, Diagnostico, Observaciones, Fecha_Consulta, ID_Doctor, ID_Cita, Id_Consulta)

        elif opcion == "4":
            Id_Consulta = validar_entero("Digite el Id de la consulta que desea buscar: ")
            cons.buscar_consulta(con, Id_Consulta)
        
        elif opcion == "5":
            cons.mostrar_consultas(con)

        else:
            print("--------------------")
            print("Opción no válida. Intente de nuevo.")
            print("--------------------")
            
            
def doctores():
    while True:
        print("Has seleccionado Doctores")
        print("0-Volver al menu principal")
        print("1-Agregar doctor")
        print("2-Eliminar doctor")
        print("3-Actualizar doctor")
        print("4-Consultar doctor")
        print("5-Mostrar todos los doctores")
        print("6-Mostar especialidades")
        print("7-Consultar especialidad de un doctor")
        opcion = input("Seleccione una opción: ")
        
        os.system('cls')
        
        if opcion == "1":
            Id_Doctor = validar_entero("Digite el Id del doctor: ")
            Nombres = validar_texto("Digite los nombres del doctor: ")
            Apellidos = validar_texto("Digite los apellidos del doctor: ")
            telefono = validar_telefono("Digite el numero de telefono del doctor (sin guiones): ")
            correo = validar_correo("Digite el correo del doctor: ")
            Id_Espec = validar_entero("Digite el Id de la especialidad del doctor \n(Si no sabe el Id de la especialidad consulte en '6-Mostrar especialidades'): ")
            doc.agregar_doctor(con, Id_Doctor, Nombres, Apellidos, telefono, correo, Id_Espec)
            
        elif opcion == "2":
            Id_Doctor = validar_entero("Digite el Id del doctor que desea eliminar: ")
            doc.eliminar_doctor(con, Id_Doctor)
            
        elif opcion == "3":
            Id_Doctor = validar_entero("Digite el Id del doctor que desea modificar: ")
            Nombres = validar_texto("Digite los nombres del doctor: ")
            Apellidos = validar_texto("Digite los apellidos del doctor: ")
            telefono = validar_telefono("Digite el numero de telefono del doctor (sin guiones): ")
            correo = validar_correo("Digite el correo del doctor: ")
            doc.actualizar_doctor(con, Id_Doctor, Nombres, Apellidos, telefono, correo)
            
        elif opcion == "4":
            Id_Doctor = validar_entero("Digite el Id del doctor que desea consultar: ")
            print("El doctor consultado es el siguiente: ")
            doc.buscar_doctor(con, Id_Doctor)
            
        elif opcion == "5":
            doc.mostrar_doctores(con)
            
        elif opcion == "6":
            doc.mostrar_especialidades(con)
            
        elif opcion == "7":
            Id_Doctor = validar_entero("Digite el Id del doctor que desea consultar: ")
            print("La especialidad del doctor consultado es: ")
            doc.mostrar_especialidad_doctor(con, Id_Doctor)
            
        elif opcion == "0":
            break
        else:
            print("--------------------")
            print("Opción no válida. Intente de nuevo.")
            print("--------------------")
            

#Pupusas de queso

if __name__ == "__main__":
    mostrar_titulo()
    mostrar_menu()
