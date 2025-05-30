def agregar_consulta(Conexion, Id_Consulta, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita):
    try:
        cursor = Conexion.cursor()
        sql = "INSERT INTO CONSULTAS VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (Id_Consulta, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita))
        Conexion.commit()
        print("Consulta agregada correctamente.")
    except Exception as ex:
        print(f"Error al agregar la consulta: {ex}")


def eliminar_consulta(Conexion, Id_Consulta):
    try:
        cursor = Conexion.cursor()
        sql = "DELETE FROM CONSULTAS WHERE Id_Consulta = ?"
        cursor.execute(sql, (Id_Consulta))
        Conexion.commit()
        print("Consulta eliminada correctamente.")
    except Exception as ex:
        print(f"Error al eliminar la consulta: {ex}")



def actualizar_consulta(Conexion, Id_Consulta, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita):
    try:
        cursor = Conexion.cursor()
        sql = """
        UPDATE CONSULTAS
        SET diagnostico = ?, observaciones = ?, fecha_consulta = ?, Id_Doctor = ?, Id_Cita = ?
        WHERE Id_Consulta = ?
        """
        cursor.execute(sql, (diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita, Id_Consulta_Original))
        Conexion.commit()
        print("Consulta actualizada correctamente.\n")
    except Exception as ex:
        print(f"Error al actualizar la consulta: {ex}")

def mostrar_consultas(Conexion):
    try:
        cursor = Conexion.cursor()
        cursor.execute("SELECT * FROM CONSULTAS")
        for fila in cursor.fetchall():
            print(f"{fila}\n")
    except Exception as ex:
        print(f"Error al mostrar las consultas: {e}")


def buscar_consulta(Conexion, Id_Consulta):

    Consulta = {
        'Id_Consulta': [],
        'Diagnostico': [],
        'Observaciones': [],
        'Fecha_Consulta': [],
        'Id_Doctor': [],
        'Id_Cita': []
    }

    try:
        cursor = Conexion.cursor()
        sql = 'SELECT * FROM CONSULTAS WHERE Id_Consulta = ?'
        cursor.execute(sql, (Id_Consulta,)) 
        filas = cursor.fetchall() 

        if not filas:
            print("No se encontró ninguna consulta con ese ID.\n")
            return

        for fila in filas: 
            Consulta['Id_Consulta'].append(fila[0])
            Consulta['Diagnostico'].append(fila[1])
            Consulta['Observaciones'].append(fila[2])
            Consulta['Fecha_Consulta'].append(fila[3])
            Consulta['Id_Doctor'].append(fila[4])
            Consulta['Id_Cita'].append(fila[5])

            print("\n--- Detalles de la Consulta ---")
        for i in range(len(Consulta['Id_Consulta'])): 
            print(f"ID Consulta: {Consulta['Id_Consulta'][i]}")
            print(f"Diagnóstico: {Consulta['Diagnostico'][i]}")
            print(f"Observaciones: {Consulta['Observaciones'][i]}")
            print(f"Fecha de Consulta: {Consulta['Fecha_Consulta'][i]}")
            print(f"ID Doctor: {Consulta['Id_Doctor'][i]}")
            print(f"ID Cita: {Consulta['Id_Cita'][i]}\n")

    except Exception as e:
        print(f"Error al buscar consulta: {e}")