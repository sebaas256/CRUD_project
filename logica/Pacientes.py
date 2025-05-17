def AgregarPacientes(Conexion, DUI, Nombres, Apellidos, Edad, Genero, Direccion):
    
    try:
        
        cursor = Conexion.cursor()
        sql = "INSERT INTO PACIENTES VALUES (?,?,?,?,?,?)"
        cursor.execute(sql, (DUI, Nombres, Apellidos, Edad, Genero, Direccion))
        Conexion.commit()
        print("Paciente agregado exitosamente!")   
        
    except Exception as e:
        print("Error al insertar el paciente:", e)   
        
def EliminarPaciente(Conexion, DUI):   
    
    try:
    
        cursor = Conexion.cursor()
        sql = "DELETE * FROM PACIENTES WHERE DUI = ? "
        cursor.execute(sql, DUI)
        Conexion.commit()
        print("Paciente eliminado exitosamente!")   
    
    except Exception as e:
        print("Error al eliminar el paciente:", e)
        
def ActualizarPaciente(Conexion, DUI, Nombres, Apellidos, Edad, Genero, Direccion):
    
    try:
        cursor = Conexion.cursor()
        sql = '''
        UPDATE PACIENTES
        SET DUI = ?, Nombres = ?, Apellidos = ? Edad = ?, Genero = ?, Direccion = ?
        WHERE DUI = ?
        '''
        cursor.execute(sql, (DUI, Nombres, Apellidos, Edad, Genero, Direccion, DUI))
        Conexion.commit()
        print("Paciente actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar paciente:", e)
    
def MostrarPacientes(Conexion):
    
    try:
        cursor = Conexion.cursor()
        cursor.execute("SELECT id, nombre, edad, genero, direccion FROM PACIENTES")
        for fila in cursor.fetchall():
            print(fila)
    
    except Exception as e:
        print("Error al obtener pacientes:", e)
    
def BuscarPaciente(Conexion, DUI):

    try:
        cursor = Conexion.cursor()
        sql = 'SELECT * FROM PACIENTES WHERE DUI = ?'
        cursor.execute(sql, DUI)
    
    except Exception as e:
        print("Error al buscar paciente", e)