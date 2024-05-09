from Conexion import *

class CDatosCultivos: 
    
    def mostrarCultivos ():
        
        try:
        
         conectCultivos = CConexion.ConexionDatosCultivos()
         cursor = conectCultivos.cursor()
         cursor.execute("select * from cultivos") 
         vistaCultivos = cursor.fetchall()
         conectCultivos.commit()
         conectCultivos.close()
         return vistaCultivos
            
        except mysql.connector.Error as error:
            print("Error de mostar los datos {}"-format(error))
    
    def ingresarCultivos(nombre,tipo,area,rendimiento):
        
        try:
        
         conectCultivos = CConexion.ConexionDatosCultivos()
         cursor = conectCultivos.cursor()
         sql = "insert into cultivos values (null,%s,%s,%s,%s);"
         valores = (nombre,tipo,area,rendimiento)
         cursor.execute(sql,valores)
         conectCultivos.commit()
         print(cursor.rowcount,"Registro ingresado")
         conectCultivos.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}"-format(error))
            
            
    def modificarCultivos(id,nombre,tipo,area,rendimiento):
        
        try:
        
         conectCultivos = CConexion.ConexionDatosCultivos()
         cursor = conectCultivos.cursor()
         sql = "UPDATE cultivos SET cultivos.nombre = %s,cultivos.tipo=%s,cultivos.area=%s,cultivos.rendimiento =%s Where cultivos.id =%s;"
         valores = (nombre,tipo,area,rendimiento,id)
         cursor.execute(sql,valores)
         conectCultivos.commit()
         print(cursor.rowcount,"Registro Actualizado")
         conectCultivos.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}"-format(error))
            
    def eliminarCultivos(id,nombre,tipo,area,rendimiento):
        
        try:
        
         conectCultivos = CConexion.ConexionDatosCultivos()
         cursor = conectCultivos.cursor()
         sql = "DELETE from cultivos WHERE cultivos.id=%s;"
         valores = (id,)
         cursor.execute(sql,valores)
         conectCultivos.commit()
         print(cursor.rowcount,"Registro Eliminado")
         conectCultivos.close()
            
        except mysql.connector.Error as error:
            print("Error de elimicacion de datos {}"-format(error))
            
class CDatosGanado: 
    
    def mostrarGanado ():
        
        try:
        
         conectGanado = CConexion.ConexionDatosGanado()
         cursor = conectGanado.cursor()
         cursor.execute("select * from ganado") 
         vistaGanado = cursor.fetchall()
         conectGanado.commit()
         conectGanado.close()
         return vistaGanado
            
        except mysql.connector.Error as error:
            print("Error de mostar los datos {}".format(error))
    
    def ingresarGanado(especie,raza,edad,peso,produccion):
        
        try:

         conectGanado= CConexion.ConexionDatosGanado()
         cursor = conectGanado.cursor()
         sql = "insert into ganado values (null,%s,%s,%s,%s,%s);"
         valoresGanado = (especie,raza,edad,peso,produccion)
         cursor.execute(sql,valoresGanado)
         conectGanado.commit()
         print(cursor.rowcount,"Registro ingresado")
         conectGanado.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
    def modificarGanado(id,especie,raza,edad,peso,produccion):
        
        try:
        
         conectGanado = CConexion.ConexionDatosGanado()
         cursor = conectGanado.cursor()
         sql = "update ganado set ganado.especie= %s,ganado.raza = %s, ganado.edad= %s,ganado.peso=%s,ganado.produccion=%s where ganado.id = %s";
         valoresGanado = (especie,raza,edad,peso,produccion,id)
         cursor.execute(sql,valoresGanado)
         conectGanado.commit()
         print(cursor.rowcount,"Registro Actualizado")
         conectGanado.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))
            
    def eliminarGanado(id,especie,raza,edad,peso,produccion):
        
        try:
        
         conectGanado = CConexion.ConexionDatosGanado()
         cursor = conectGanado.cursor()
         sql = "DELETE from ganado WHERE ganado.id=%s;"
         valoresGanado = (id,)
         cursor.execute(sql,valoresGanado)
         conectGanado.commit()
         print(cursor.rowcount,"Registro Eliminado")
         conectGanado.close()
            
        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))       

