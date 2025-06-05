import pyodbc

def Conexion():
    try:
        connection = pyodbc.connect(
<<<<<<< HEAD
            r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-5IVCK1D\SQLEXPRESS;DATABASE=CONSULTORIO_DENTAL;Trusted_Connection=Yes'
=======
            r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\serverITCA;DATABASE=CONSULTORIO_DENTAL;Trusted_Connection=Yes'
>>>>>>> eeab7f27b160a514f52b02abd55d63fe720da71f
        )
        print("Conexión exitosa")
        return connection
    except Exception as ex:
        print("Error:", ex)
        return None
Conexion()    

