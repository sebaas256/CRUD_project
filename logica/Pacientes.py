def AgregarPacientes(Conexion, DUI, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo):
    
    try:
        
        cursor = Conexion.cursor()
        sql = "INSERT INTO PACIENTES VALUES (?,?,?,?,?,?,?)"
        cursor.execute(sql, (DUI, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo))
        Conexion.commit()
        print("Paciente agregado exitosamente!\n")   
        
    except Exception as e:
        print("Error al insertar el paciente:", e)   
        
def EliminarPaciente(Conexion, DUI):   
    
    try:
    
        cursor = Conexion.cursor()
        sql = "DELETE FROM PACIENTES WHERE DUI_Paciente = ? "
        cursor.execute(sql, DUI)
        Conexion.commit()
        print("Paciente eliminado exitosamente!\n")   
    
    except Exception as e:
        print("Error al eliminar el paciente:", e)
        
def ActualizarPaciente(Conexion, DUI, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo, dui):
    
    try:
        cursor = Conexion.cursor()
        sql = '''
        UPDATE PACIENTES
        SET DUI_Paciente = ?, Nombres = ?, Apellidos = ?, Fecha_Nacimiento = ?, Telefono = ?, Direccion = ?, Correo = ?
        WHERE DUI_Paciente = ?
        '''
        cursor.execute(sql, (DUI, Nombres, Apellidos, Fecha_Nacimiento, Telefono, Direccion, Correo, dui))
        Conexion.commit()
        print("Paciente actualizado correctamente!\n")
    except Exception as e:
        print("Error al actualizar paciente:", e)
    
def MostrarPacientes(Conexion):
    
    try:
        cursor = Conexion.cursor()
        cursor.execute("SELECT * FROM PACIENTES")
        for fila in cursor.fetchall():
            print(f"{fila}\n")
            

    except Exception as e:
        print("Error al obtener pacientes:", e)
    
def BuscarPaciente(Conexion, DUI):

    Paciente = {
    'Dui' : [] ,    
    'Nombres' : [] ,   
    'Apellidos' : [] ,   
    'Fecha_Nacimiento' : [] ,  
    'Telefono' : [] ,  
    'Direccion' : [] ,
    'Correo' : []    
    
    }
    
    try:
        cursor = Conexion.cursor()
        sql = 'SELECT * FROM PACIENTES WHERE DUI_Paciente = ?'
        cursor.execute(sql, DUI)
        filas = cursor.fetchall()
        
        for fila in filas:
            Paciente['Dui'].append(fila[0])
            Paciente['Nombres'].append(fila[1])
            Paciente['Apellidos'].append(fila[2])
            Paciente['Fecha_Nacimiento'].append(fila[3])
            Paciente['Telefono'].append(fila[4])
            Paciente['Direccion'].append(fila[5])
            Paciente['Correo'].append(fila[6])
            
        for i in range(len(Paciente['Dui'])):
            print(f"DUI: {Paciente['Dui'][i]} ")
            print(f"Nombres: {Paciente['Nombres'][i]}")
            print(f"Apellidos: {Paciente['Apellidos'][i]}")
            print(f"Fecha de Nacimiento: {Paciente['Fecha_Nacimiento'][i]}")
            print(f"Teléfono: {Paciente['Telefono'][i]}")
            print(f"Dirección: {Paciente['Direccion'][i]}")
            print(f"Correo: {Paciente['Correo'][i]} \n")
    
    except Exception as e:
        print("Error al buscar paciente", e)
        
