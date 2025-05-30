def mostrar_doctores(Conexion):
    try:
        cursor = Conexion.cursor()
        cursor.execute("SELECT * FROM DOCTORES")
        
        doctores = cursor.fetchall()
        
        if not doctores:
            print("No hay doctores registrados en la base de datos.")
            return
        
        print("\n" + "="*120)
        print(f"{'ID':<5} {'NOMBRES':<20} {'APELLIDOS':<20} {'TELEFONO':<15} {'CORREO':<30} {'ID_ESPC':<10}")
        print("="*120)
        
        for fila in doctores:
            id_doctor = str(fila[0]) 
            nombres = str(fila[1])
            apellidos = str(fila[2])
            telefono = str(fila[3]) 
            correo = str(fila[4])
            id_espc = str(fila[5]) 
            
            print(f"{id_doctor:<5} {nombres:<20} {apellidos:<20} {telefono:<15} {correo:<30} {id_espc:<10}")
        
        print("="*120)
        print(f"Total de doctores: {len(doctores)}")
        
    except Exception as ex:
        print("Error al mostrar doctores:", ex)

        
def eliminar_doctor(Conexion, Id_Doctor):
    try:
        cursor = Conexion.cursor()
        
        #verificar si el doctor existe
        cursor.execute("SELECT Nombres, Apellidos FROM DOCTORES WHERE Id_Doctor = ?", (Id_Doctor,))
        doctor = cursor.fetchone()
        
        if not doctor:
            print("\n" + "="*50)
            print("DOCTOR NO ENCONTRADO")
            print("="*50)
            print(f"No existe un doctor con ID: {Id_Doctor}")
            print("="*50)
            return
        
        sql = "DELETE FROM DOCTORES WHERE Id_Doctor = ?"
        cursor.execute(sql, (Id_Doctor,))
        Conexion.commit()
        
        print("\n" + "="*50)
        print("DOCTOR ELIMINADO EXITOSAMENTE")
        print("="*50)
        print(f"Doctor: {doctor[0]} {doctor[1]}")
        print(f"ID: {Id_Doctor}")
        print("="*50)
       
    except Exception as ex:        
        print("\n" + "="*50)
        print("ERROR AL ELIMINAR DOCTOR")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)


def agregar_doctor(Conexion, Id_Doctor, Nombres, Apellidos, telefono, correo, Id_espec):
    try:
        cursor = Conexion.cursor()
        
        # Verificar si ya existe un doctor con ese id
        cursor.execute("SELECT Id_Doctor FROM DOCTORES WHERE Id_Doctor = ?", (Id_Doctor,))
        if cursor.fetchone():
            print("\n" + "="*50)
            print("ERROR AL AGREGAR DOCTOR")
            print("="*50)
            print(f"Ya existe un doctor con ID: {Id_Doctor}")
            print("="*50)
            return
        
        # Verificar si existe la especialidad
        cursor.execute("SELECT Nombre_esp FROM DOC_ESPC WHERE Id_Espc = ?", (Id_espec,))
        especialidad = cursor.fetchone()
        
        if not especialidad:
            print("\n" + "="*50)
            print("ERROR AL AGREGAR DOCTOR")
            print("="*50)
            print(f"No existe la especialidad con ID: {Id_espec}")
            print("="*50)
            return
        
        # Agregar datos del doctor
        sql = "INSERT INTO DOCTORES VALUES (?,?,?,?,?,?)"
        cursor.execute(sql, (Id_Doctor, Nombres, Apellidos, telefono, correo, Id_espec))
        Conexion.commit()
        
        print("\n" + "="*70)
        print("DOCTOR AGREGADO EXITOSAMENTE")
        print("="*70)
        print(f"{'Campo':<15} {'Valor':<50}")
        print("-"*70)
        print(f"{'ID Doctor:':<15} {Id_Doctor}")
        print(f"{'Nombres:':<15} {Nombres}")
        print(f"{'Apellidos:':<15} {Apellidos}")
        print(f"{'Telefono:':<15} {telefono}")
        print(f"{'Correo:':<15} {correo}")
        print(f"{'Especialidad:':<15} {especialidad[0]}")
        print("="*70)
       
    except Exception as ex:
        print("\n" + "="*50)
        print("ERROR AL AGREGAR DOCTOR")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)


def mostrar_especialidades(Conexion):
    try:
        cursor = Conexion.cursor()
        sql = "SELECT * FROM DOC_ESPC"
        cursor.execute(sql)
        especialidades = cursor.fetchall()
        
        if not especialidades:
            print("\n" + "="*50)
            print("NO HAY ESPECIALIDADES REGISTRADAS")
            print("="*50)
            return
        
        print("\n" + "="*60)
        print("ESPECIALIDADES MEDICAS")
        print("="*60)
        print(f"{'ID':<10} {'ESPECIALIDAD':<45}")
        print("-"*60)
        
        for fila in especialidades:
            id_espc = str(fila[0]) 
            nombre_esp = str(fila[1])
            print(f"{id_espc:<10} {nombre_esp:<45}")
        
        print("="*60)
        print(f"Total de especialidades: {len(especialidades)}")
        print("="*60)
   
    except Exception as ex:
        print("\n" + "="*50)
        print("ERROR AL MOSTRAR ESPECIALIDADES")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)


def actualizar_doctor(Conexion, Id_Doctor, Nombres, Apellidos, telefono, correo):
    try:
        cursor = Conexion.cursor()
        
        # Verificar si el doctor existe
        cursor.execute("SELECT * FROM DOCTORES WHERE Id_Doctor = ?", (Id_Doctor,))
        doctor_actual = cursor.fetchone()
        
        if not doctor_actual:
            print("\n" + "="*50)
            print("DOCTOR NO ENCONTRADO")
            print("="*50)
            print(f"No existe un doctor con ID: {Id_Doctor}")
            print("="*50)
            return
        
        # Actualizar datos del doctor
        sql = "UPDATE DOCTORES SET Nombres = ?, Apellidos = ?, telefono = ?, correo = ? WHERE Id_Doctor = ?"
        cursor.execute(sql, (Nombres, Apellidos, telefono, correo, Id_Doctor))
        Conexion.commit()
        
        print("\n" + "="*80)
        print("DOCTOR ACTUALIZADO EXITOSAMENTE")
        print("="*80)
        print(f"{'Campo':<15} {'Antes':<30} {'Después':<30}")
        print("-"*80)
        print(f"{'ID:':<15} {doctor_actual[0]:<30} {Id_Doctor:<30}")
        print(f"{'Nombres:':<15} {doctor_actual[1]:<30} {Nombres:<30}")
        print(f"{'Apellidos:':<15} {doctor_actual[2]:<30} {Apellidos:<30}")
        print(f"{'Telefono:':<15} {doctor_actual[3]:<30} {telefono:<30}")
        print(f"{'Correo:':<15} {doctor_actual[4]:<30} {correo:<30}")
        print("="*80)
       
    except Exception as ex:
        print("\n" + "="*50)
        print("ERROR AL ACTUALIZAR DOCTOR")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)


def buscar_doctor(Conexion, Id_Doctor):  
    try:
        cursor = Conexion.cursor()
        sql = "SELECT * FROM DOCTORES WHERE Id_Doctor = ?"
        cursor.execute(sql, (Id_Doctor,))
        doctor = cursor.fetchone()
        
        if not doctor:
            print("\n" + "="*50)
            print("DOCTOR NO ENCONTRADO")
            print("="*50)
            print(f"No existe un doctor con ID: {Id_Doctor}")
            print("="*50)
            return
        
        print("\n" + "="*70)
        print("INFORMACION DEL DOCTOR")
        print("="*70)
        print(f"{'Campo':<15} {'Información':<50}")
        print("-"*70)
        print(f"{'ID Doctor:':<15} {doctor[0]}")
        print(f"{'Nombres:':<15} {doctor[1]}")
        print(f"{'Apellidos:':<15} {doctor[2]}")
        print(f"{'Telefono:':<15} {doctor[3]}")
        print(f"{'Correo:':<15} {doctor[4]}")
        print(f"{'ID Especialidad:':<15} {doctor[5]}")
        print("="*70)
   
    except Exception as ex:
        print("\n" + "="*50)
        print("ERROR AL BUSCAR DOCTOR")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)


def mostrar_especialidad_doctor(Conexion, Id_Doctor):
    try:
        cursor = Conexion.cursor()
        sql = """SELECT doc.Id_Doctor, doc.Nombres, doc.Apellidos, doc_esp.Nombre_esp, 
                        doc.telefono, doc.correo
                 FROM DOCTORES doc 
                 INNER JOIN DOC_ESPC doc_esp ON (doc_esp.Id_Espc = doc.Id_Espc) 
                 WHERE doc.Id_Doctor = ?"""
        cursor.execute(sql, (Id_Doctor,))
        doctor = cursor.fetchone()
        
        if not doctor:
            print("\n" + "="*60)
            print("DOCTOR NO ENCONTRADO")
            print("="*60)
            print(f"No se encontro doctor con ID: {Id_Doctor}")
            print("="*60)
            return
        
        print("\n" + "="*80)
        print("INFORMACION COMPLETA DEL DOCTOR")
        print("="*80)
        print(f"{'Campo':<20} {'Información':<55}")
        print("-"*80)
        print(f"{'ID Doctor:':<20} {doctor[0]}")
        print(f"{'Nombres:':<20} {doctor[1]}")
        print(f"{'Apellidos:':<20} {doctor[2]}")
        print(f"\033[94m{'Especialidad:':<20} {doctor[3]}\033[0m")
        print(f"{'Telefono:':<20} {doctor[4]}")
        print(f"{'Correo:':<20} {doctor[5]}")
        print("="*80)
   
    except Exception as ex:
        print("\n" + "="*50)
        print("ERROR AL MOSTRAR ESPECIALIDAD")
        print("="*50)
        print(f"Error: {ex}")
        print("="*50)