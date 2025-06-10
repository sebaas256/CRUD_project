# logica/Citas.py


#1 add
def agregar_cita(conexion, id_cita, fecha_cita, consultorio, descripcion, estado_cita, dui_paciente):
    try:
        cursor = conexion.cursor()
       

            #fix----------
        if isinstance(estado_cita, tuple):
            estado_cita = estado_cita[0]
        else:
            estado_cita = bool(estado_cita)
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
        print(f"Error al eliminar cita: {e}")
        return False
    
#3 edit
def actualizar_cita(conexion, id_cita, nueva_fecha, nuevo_estado):
    try:
        cursor = conexion.cursor()
        if isinstance(nuevo_estado, tuple):
                nuevo_estado = nuevo_estado[0]
        else:
                nuevo_estado = bool(nuevo_estado)
    
        cursor.execute(
            "UPDATE CITAS SET fecha_cita = ?, estado_cita = ? WHERE Id_Cita = ?",
            (nueva_fecha, nuevo_estado, id_cita)
        )
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar cita: {e}")
        return False
#4 consult
def consultar_cita(conexion, id_cita):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM CITAS WHERE Id_Cita = ?",
            (id_cita,)
        )
        return cursor.fetchone() or None
    except Exception as e:
        print(f"Error al consultar cita: {e}")
        return None
    



    
