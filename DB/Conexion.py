import pyodbc

def Conexion():
    try:
        connection = pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\serverITCA;DATABASE=CONSULTORIO_DENTAL;Trusted_Connection=Yes'
        )
        print("Conexión exitosa")
        return connection
    except Exception as ex:
        print("Error:", ex)
        return None
