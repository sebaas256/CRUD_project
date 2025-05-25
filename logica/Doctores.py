def mostrar_doctores(Conexion):
    try:
        cursor = Conexion.cursor()
        cursor.execute("select * from DOCTORES")
        for fila in cursor.fetchall():
            print(f"{fila}\n")
            
    except Exception as ex:
        print("Error al mostrar doctores:", ex)
        
def eliminar_doctor(Conexion, Id_Doctor):
    try:
        cursor = Conexion.cursor()
        sql = "delete from DOCTORES where Id_Doctor = ?"
        cursor.execute(sql, Id_Doctor)
        Conexion.commit()
        print("--------------------")
        print("Paciente eliminado exitosamente")
        print("--------------------")
        
    except Exception as ex:        
        print("Error al intertar elminar un doctor:", ex)
        
def agregar_doctor(Conexion, Id_Doctor, Nombres, Apellidos, telefono, correo, Id_espec):
    try:
        cursor = Conexion.cursor()
        sql = "insert into DOCTORES values (?,?,?,?,?,?)"
        cursor.execute(sql, (Id_Doctor, Nombres, Apellidos, telefono, correo, Id_espec))
        Conexion.commit()
        print("--------------------")
        print("Doctor agregado exitosamente")
        print("--------------------")
        
    except Exception as ex:
        print("Error al intentar agregar el doctor:", ex)