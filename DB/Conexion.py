import pyodbc

def Conexion():
    try: 
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=XD;DATABASE=CONSULTORIO_DENTAL;Trusted_Connection=YES')
        print("Conexion exitosa")
        return connection
    except Exception as ex :
        print(ex)
        return None
