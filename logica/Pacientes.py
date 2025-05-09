

def AgregarPacientes(Conexion, DUI, Nombres, Apellidos, Edad, Genero, Direccion  ):
    
    try:
    
        cursor = Conexion.cursor()
        sql = "INSERT INTO PACIENTES VALUES ()"
        cursor.execute(sql, (DUI, Nombres, Apellidos, Edad, Genero, Direccion))
        Conexion.commit()
    
    except Exception as e:
        print("Error al insertar paciente:", e)   