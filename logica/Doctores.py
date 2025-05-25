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
        
def mostrar_especialidades(Conexion):
    try:
        cursor = Conexion.cursor()
        sql = "select * from DOC_ESPC"
        cursor.execute(sql)
        for fila in cursor.fetchall():
            print(f"{fila}\n")
    
    except Exception as ex:
        print("Error al mostrar las especialidades de los doctores:", ex)
        
def actualizar_doctor(Conexion, Id_Doctor, Nombres, Apellidos, telefono, correo):
    try:
        cursor = Conexion.cursor()       
        sql = " update DOCTORES set Nombres = ?, Apellidos = ?, Telefono = ?, Correo = ? where Id_Doctor = ?"
        cursor.execute(sql, (Nombres, Apellidos, telefono, correo, Id_Doctor))
        Conexion.commit()
        print("--------------------")
        print("Datos del doctor actualizados correctamente")
        print("--------------------")
        
    except Exception as ex:
        print("Error al intentar actualizar el doctor:", ex)
        
def buscar_doctor(Conexion, Id_Doctot):
    try:
        cursor = Conexion.cursor()
        sql = "select * from DOCTORES where Id_Doctor = ?"
        cursor.execute(sql, Id_Doctot)
        for fila in cursor.fetchall():
            print(f"{fila}\n")
    
    except Exception as ex:
        print("Error al intentar buscar el doctor:", ex)
        
def mostrar_especialidad_doctor(Conexion, Id_Doctor):
    try:
        cursor = Conexion.cursor()
        sql = " select doc.Id_Doctor, doc.Nombres, doc.Apellidos, doc_esp.Nombre_esp from DOCTORES doc inner join DOC_ESPC doc_esp on (doc_esp.Id_Espc = doc.Id_Espc) where doc.Id_Doctor = ? "
        cursor.execute(sql, Id_Doctor)
        for fila in cursor.fetchall():
            print(f"{fila}\n")
    
    except Exception as ex:
        print("Error al mostrar las especialidades de los doctores:", ex)