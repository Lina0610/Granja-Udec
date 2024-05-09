
import mysql.connector 

class CConexion:
    
 def ConexionDatosCultivos():
    try:
        conexion = mysql.connector.connect (user= 'root',password='lina0610',
                                            host = '127.0.0.1',
                                            database='cultivosdb',
                                            port='3306')
        print("Conexion Bienn")
        return conexion
            
    except mysql.connector.Error as error:
        print("Error al concectarse a la base de Datos {}".format(error))
            
        return conexion
        
 ConexionDatosCultivos()

 def ConexionDatosGanado():
    try:
        conexion = mysql.connector.connect (user= 'root',password='lina0610',
                                            host = '127.0.0.1',
                                            database='ganadodb',
                                            port='3306')
        print("Conexion Bienn")
        return conexion
            
    except mysql.connector.Error as error:
        print("Error al concectarse a la base de Datos {}".format(error))
            
        return conexion
        
 ConexionDatosGanado()

