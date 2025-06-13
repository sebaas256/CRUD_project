def agregar_consulta(Conexion, Id_Consulta, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita):
    try:
        cursor = Conexion.cursor()
        # Verificar si ya existe una consulta con ese id
        cursor.execute("SELECT Id_Consulta FROM CONSULTAS WHERE Id_Consulta = ?", (Id_Consulta,))
        if cursor.fetchone():
            print("\n" + "="*50)
            print("ERROR AL AGREGAR CONSULTA")
            print("="*50)
            print(f"Ya existe una consulta con ID: {Id_Consulta}")
            print("="*50)
            return
        # Agregar la consulta y mostrar los datos de la consulta en formato de tabla
        sql = "INSERT INTO CONSULTAS VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (Id_Consulta, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita))
        Conexion.commit()
        print("\n" + "="*70)
        print("Consulta agregada correctamente.")
        print("="*70)
        print(f"{'campo':<20} {'Valor':<45}")
        print("-"*70)
        print(f"{'ID Consulta:':<20} {Id_Consulta}")
        print(f"{'Diagnóstico:':<20} {diagnostico}")
        print(f"{'Observaciones:':<20} {observaciones}")
        print(f"{'Fecha de Consulta:':<20} {fecha_consulta}")
        print(f"{'ID Doctor:':<20} {Id_Doctor}")
        print(f"{'ID Cita:':<20} {Id_Cita}")  
        print("="*70)
    except Exception as ex:
        print("\n" + "="*50)
        print(f"Error al agregar la consulta: {ex}")
        print("="*50)


def eliminar_consulta(Conexion, Id_Consulta):
    try:
        cursor = Conexion.cursor()
        # Verificar si la consulta existe
        cursor.execute("SELECT Id_Consulta FROM CONSULTAS WHERE Id_Consulta = ?", (Id_Consulta,))
        consulta = cursor.fetchone()
        if not consulta:
            print("\n" + "="*50)
            print("ERROR AL ELIMINAR CONSULTA")
            print("="*50)
            print(f"No existe una consulta con ID: {Id_Consulta}")
            print("="*50)
            return
        # Eliminar la consulta y mostrar un mensaje de confirmación
        sql = "DELETE FROM CONSULTAS WHERE Id_Consulta = ?"
        cursor.execute(sql, (Id_Consulta))
        Conexion.commit()
        print("\n" + "="*50)
        print("Consulta eliminada correctamente.")
        print("="*50)
        print(f"ID Consulta: {Id_Consulta}")
        print("="*50)
    except Exception as ex:
        print("\n" + "="*50)
        print(f"Error al eliminar la consulta: {ex}")
        print("="*50)



def actualizar_consulta(Conexion, diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita, Id_Consulta_Original):
    try:
        cursor = Conexion.cursor()
        # Verificar si la consulta existe
        cursor.execute("SELECT Id_Consulta FROM CONSULTAS WHERE Id_Consulta = ?", (Id_Consulta_Original,))
        consulta_actual = cursor.fetchone()
        if not consulta_actual:
            print("\n" + "="*50)
            print("Error al actualizar la consulta")
            print("="*50)
            print(f"No existe una consulta con ID: {Id_Consulta_Original}")
            print("="*50)
            return
        # Actualizar la consulta y mostrar los datos actualizados en formato de tabla
        sql = """
        UPDATE CONSULTAS
        SET diagnostico = ?, observaciones = ?, fecha_consulta = ?, Id_Doctor = ?, Id_Cita = ?
        WHERE Id_Consulta = ?;
        """
        cursor.execute(sql, (diagnostico, observaciones, fecha_consulta, Id_Doctor, Id_Cita, Id_Consulta_Original))
        Conexion.commit()
        print("\n" + "="*80)
        print("Consulta actualizada correctamente.\n")
        print("="*80)
        print(f"{'Campo':<20} {'Valor':<45}")
        print("-"*80)
        print(f"{'ID Consulta:':<20} {Id_Consulta_Original}")
        print(f"{'Diagnóstico:':<20} {diagnostico}")
        print(f"{'Observaciones:':<20} {observaciones}")
        print(f"{'Fecha de Consulta:':<20} {fecha_consulta}")
        print(f"{'ID Doctor:':<20} {Id_Doctor}")
        print(f"{'ID Cita:':<20} {Id_Cita}")
        print("="*80)
    except Exception as ex:
        print("\n" + "="*50)
        print(f"Error al actualizar la consulta: {ex}")
        print("="*50)


def buscar_consulta(Conexion, Id_Consulta):
    try:
        cursor = Conexion.cursor()
        # Verificar si la consulta existe
        sql = 'SELECT * FROM CONSULTAS WHERE Id_Consulta = ?'
        cursor.execute(sql, (Id_Consulta,)) 
        consulta = cursor.fetchone()
        # Si no se encuentra la consulta, mostrar un mensaje
        if not consulta:
            print("\n" + "="*50)
            print("No se encontró ninguna consulta con ese ID.\n")
            print("="*50)
            return
        
        print("\n" + "="*80)
        print("\n--- Detalles de la Consulta ---")
        print("="*80)
        print(f"{'Campo':<20} {'Valor':<55}")
        print("-"*80)
        print(f"{'ID Consulta:':<20} {consulta[0]}")
        print(f"{'Diagnóstico:':<20} {consulta[1]}")
        print(f"{'Observaciones:':<20} {consulta[2]}")
        print(f"{'Fecha de Consulta:':<20} {consulta[3]}")
        print(f"{'ID Doctor:':<20} {consulta[4]}")
        print(f"{'ID Cita:':<20} {consulta[5]}")
        print("="*80)
    except Exception as e:
        print("\n" + "="*50)
        print(f"Error al buscar consulta: {e}")
        print("="*50)

def mostrar_consultas(Conexion):
    try:
        cursor = Conexion.cursor()
        # Obtener todas las consultas de la base de datos
        sql = "SELECT * FROM CONSULTAS"
        cursor.execute(sql)
        consultas = cursor.fetchall()
        # Si no hay consultas, mostrar un mensaje
        if not consultas:
            print("\n" + "="*50)
            print("No hay consultas registradas.")
            print("="*50)
            return
        # Mostrar las consultas en formato de tabla
        # El ancho de las columnas se ajusta a los datos para que la tabla se vea bien
        ancho_diag = 30
        ancho_obs = 30
        print("\n" + "="*100)
        print(f"{'ID':<5} {'DIAGNÓSTICO':<{ancho_diag}} {'OBSERVACIONES':<{ancho_obs}} {'FECHA':<12} {'ID DOCTOR':<10} {'ID CITA':<8}")
        print("="*100)
        # Imprimir cada consulta en una fila de la tabla
        for fila in consultas:
            diag = (fila[1][:ancho_diag-3] + '...') if len(fila[1]) > ancho_diag else fila[1]
            obs = (fila[2][:ancho_obs-3] + '...') if len(fila[2]) > ancho_obs else fila[2]
            print(f"{str(fila[0]):<5} {diag:<{ancho_diag}} {obs:<{ancho_obs}} {str(fila[3]):<12} {str(fila[4]):<10} {str(fila[5]):<8}")
        print("="*100)
        print(f"Total de consultas: {len(consultas)}")
        print("="*100)
    except Exception as ex:
        print("\n" + "="*50)
        print(f"Error al mostrar las consultas: {ex}")
        print("="*50)