# logica/Citas.py


#1 add
def agregar_cita(conexion, id_cita, fecha_cita, consultorio, descripcion, estado_cita, dui_paciente):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM PACIENTES WHERE Dui_Paciente = ?", (dui_paciente,))
        if not cursor.fetchone():
            return False, "El paciente no existe"
        cursor.execute(
        "INSERT INTO CITAS (Id_Cita, fecha_cita, consultorio, descripcion, estado_cita, Dui_Paciente) VALUES (?, ?, ?, ?, ?, ?)",
        (id_cita, fecha_cita, consultorio, descripcion, estado_cita, dui_paciente)
        )
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar cita: {e}")
        return False
    
#2 eliminar
def eliminar_cita(conexion, id_cita):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM CITAS WHERE Id_Cita = ?", (id_cita,))
        conexion.commit()
        return True
    except Exception as e:
        print("=" * 60)
        print(f"No se puede eliminar esta cita (Elimine la consulta primero)")
        print("=" * 60)
        return False
    
#3 edit
def consultar_cita(conexion, id_cita):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM CITAS WHERE Id_Cita = ?", (id_cita,))
        cita = cursor.fetchone()

        if cita:
            print("\n" + "="*90)
            print(f"{'Id_Cita':<8} {'fecha_cita':<20} {'Consultorio':<15} {'descripcion':<25} {'Estado cita':<12} {'Dui':<15}")
            print("-"*90)
            
            id_cita = cita[0]
            fecha = cita[1].strftime("%Y-%m-%d %H:%M") if cita[1] else ""
            consultorio = cita[2]
            descripcion = cita[3]
            estado = "Completada" if cita[4] else "Pendiente"
            dui = cita[5]

            print(f"{id_cita:<8} {fecha:<20} {consultorio:<15} {descripcion:<25} {estado:<12} {dui:<15}")
            print("="*90 + "\n")
        else:
            print("\n" + "="*60)
            print("Cita no encontrada.")
            print("="*60 + "\n")
    except Exception as e:
        print(f"Error al consultar cita: {e}")


#5
    
def MostrarCitas(conexion):
  
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM CITAS"
        cursor.execute(sql)
        filas = cursor.fetchall()
        
        print(f"{'Id_Cita':<12} {'fecha_cita':<25} {'Consultorio':<25} {'descripcion':<12} {'Estado cita':<12} {'Dui':<30}")
        print("-" * 146)
        for fila in filas:
            id_cita = fila[0]
            fecha = fila[1].strftime("%Y-%m-%d %H:%M") if fila[1] else ""
            consultorio = fila[2]
            descripcion = fila[3]
            estado = "Pendiente" if fila[4] == 0 else "Completada"
            dui = fila[5]
            
            print(f"{id_cita:<4} {fecha:<19} {consultorio:<15} {descripcion:<25} {estado:<12} {dui:<10}")

    except Exception as e:
        print("Error al obtener Citas:")




    
