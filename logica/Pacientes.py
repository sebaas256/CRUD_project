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
        sql = "SELECT * FROM PACIENTES"
        cursor.execute(sql)
        filas = cursor.fetchall()
        
        print(f"{'DUI':<12} {'Nombres':<25} {'Apellidos':<25} {'Nacimiento':<12} {'Teléfono':<12} {'Dirección':<30} {'Correo':<30}")
        print("-" * 146)
        for fila in filas:
            f_na = fila[3].strftime("%Y-%m-%d") if fila[3] else ""
            print(f"{fila[0]:<12} {fila[1]:<25} {fila[2]:<25} {f_na:<12} {fila[4]:<12} {fila[5]:<30} {fila[6]:<30}")

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
        
def ConsultarCitas(conexion, DUI):
    cursor = conexion.cursor()
    sql = 'SELECT P.Dui_Paciente, P.Nombres, P.Apellidos, C.consultorio, C.descripcion, C.fecha_cita, C.estado_cita FROM PACIENTES P INNER JOIN CITAS C ON C.Dui_Paciente = P.Dui_Paciente WHERE P.Dui_Paciente = ?'
            
    cursor.execute(sql, DUI)
    filas = cursor.fetchall()
    
    print(f"{'DUI':<12} {'Nombres':<30} {'Apellidos':<30} {'Consultorio':<12} {'Descripción':<30} {'Fecha':<20} {'Estado':<10}")
    print("-" * 144)
    for fila in filas:
        fecha = fila[5].strftime("%Y-%m-%d %H:%M:%S") if fila[5] else ""
        print(f"{fila[0]:<12} {fila[1]:<30} {fila[2]:<30} {fila[3]:<12} {fila[4]:<30} {fecha:<20} {fila[6]:<10}")
   