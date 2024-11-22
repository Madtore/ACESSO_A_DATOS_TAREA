import sqlite3
from empleado import Empleado
class DataBase:
    def __init__(self):
        self.conexion = sqlite3.connect("empleados.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS empleados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            apellido_nombre TEXT NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            direccion TEXT NOT NULL,
            nif TEXT NOT NULL,
            datos_bancarios TEXT NOT NULL,
            numero_seguro_social TEXT NOT NULL,
            genero TEXT NOT NULL,
            departamento TEXT NOT NULL,
            puesto TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL,
            salario_mensual REAL NOT NULL,
            paga_extra INT NOT NULL,
            irpf REAL NOT NULL,
            seg_social REAL NOT NULL,
            fecha_baja DATE 
        )"""
        ) 
        self.conexion.commit()
        
        
    def __close__(self):
        self.conexion.close()
        
    def __open__(self):
        self.conexion = sqlite3.connect("empleados.db")
        self.cursor = self.conexion.cursor()
        
    def insertar(self,empleado):
        try:
            self.__open__()
            self.cursor.execute("""
                INSERT INTO empleados 
                (apellido_nombre, fecha_inicio, fecha_nacimiento, direccion, nif, datos_bancarios, 
                numero_seguro_social, genero, departamento, puesto, telefono, email, salario_mensual, paga_extra , irpf, seg_social)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? , ?)
            """, (
                empleado.apellido_nombre,
                empleado.fecha_inicio,
                empleado.fecha_nacimiento,
                empleado.direccion,
                empleado.nif,
                empleado.datos_bancarios,
                empleado.numero_seguro_social,
                empleado.genero,
                empleado.departamento,
                empleado.puesto,
                empleado.telefono,
                empleado.email,
                empleado.salario_mensual,
                empleado.paga_extra,
                empleado.irpf,
                empleado.seg_social
            ))
            self.conexion.commit()
        except sqlite3.OperationalError as e:
            print(f"SQLite OperationalError: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.__close__()
      
        
    def buscar_empleado(self, codigo):
        self.__open__()
        self.cursor.execute("SELECT * FROM empleados WHERE id = ?", (codigo,))
        datos_empleado = self.cursor.fetchone()
        self.__close__()
        
        if datos_empleado is None:
            return None
        
        empleado = Empleado(
        id=datos_empleado[0],
        apellido_nombre=datos_empleado[1],
        fecha_inicio=datos_empleado[2],
        fecha_nacimiento=datos_empleado[3],
        direccion=datos_empleado[4],
        nif=datos_empleado[5],
        datos_bancarios=datos_empleado[6],
        numero_seguro_social=datos_empleado[7],
        genero=datos_empleado[8],
        departamento=datos_empleado[9],
        puesto=datos_empleado[10],
        telefono=datos_empleado[11],
        email=datos_empleado[12],
        salario_mensual=datos_empleado[13],
        paga_extra=datos_empleado[14],
        irpf=datos_empleado[15],
        seg_social=datos_empleado[16],
        fecha_baja=datos_empleado[17]
    )
        
        return empleado
       
     
        
    def listar_empleados(self):
        self.__open__()
        self.cursor.execute("SELECT * FROM empleados")
        empleados = self.cursor.fetchall()
        self.__close__()
        return empleados
    
    
    def num_empleados_alta(self):
        self.__open__()
        self.cursor.execute("""
                            SELECT 
                                COUNT(id) AS numtotal, 
                                ROUND(SUM(CASE WHEN genero = 'Hombre' THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS porcentaje_hombres, 
                                ROUND(SUM(CASE WHEN genero = 'Mujer' THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS porcentaje_mujeres 
                                FROM empleados 
                                WHERE fecha_baja IS NULL;
                            """)
        num = self.cursor.fetchone()
        self.__close__()
        return{
            "empleados": num[0] if num[0] is not None else 0,
            "hombres": num[1] if num[1] is not None else 0,
            "mujeres": num[2] if num[2] is not None else 0
        }
    
    
    def num_empleados_baja(self):
        self.__open__()
        self.cursor.execute("""
                            SELECT 
                                COUNT(id) AS numtotal, 
                                ROUND(SUM(CASE WHEN genero = 'Hombre' THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS porcentaje_hombres, 
                                ROUND(SUM(CASE WHEN genero = 'Mujer' THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS porcentaje_mujeres 
                                FROM empleados 
                                WHERE fecha_baja IS NOT NULL;
                            """)
        num = self.cursor.fetchone()
        self.__close__()
              
        return {
            "empleados": num[0] if num[0] is not None else 0,
            "hombres": num[1] if num[1] is not None else 0,
            "mujeres": num[2] if num[2] is not None else 0
        }
    
    
    def edad_media(self):
        self.__open__()
        self.cursor.execute("""
                            SELECT 
                                ROUND(AVG((JULIANDAY('now') - JULIANDAY(fecha_nacimiento)) / 365.25), 2),
                                ROUND(AVG(CASE WHEN genero = 'Hombre' THEN (JULIANDAY('now') - JULIANDAY(fecha_nacimiento)) / 365.25 ELSE NULL END), 2) , 
                                ROUND(AVG(CASE WHEN genero = 'Mujer' THEN (JULIANDAY('now') - JULIANDAY(fecha_nacimiento)) / 365.25 ELSE NULL END), 2) 
                                FROM empleados WHERE fecha_baja IS NULL;
                            """)
        num = self.cursor.fetchone()
        self.__close__()
        return {
            "empleados": num[0] if num[0] is not None else 0,
            "hombres": num[1] if num[1] is not None else 0,
            "mujeres": num[2] if num[2] is not None else 0
        }
        
       
    
        
    def retribucion_media(self):
        self.__open__()
        self.cursor.execute("""
                            SELECT 
                                ROUND(AVG(salario_mensual), 2),
                                ROUND(AVG(CASE WHEN genero = 'Hombre' THEN salario_mensual ELSE 0 END), 2), 
                                ROUND(AVG(CASE WHEN genero = 'Mujer' THEN salario_mensual ELSE 0 END), 2) 
                                FROM empleados WHERE fecha_baja IS NULL;
                            """)
        num = self.cursor.fetchone()
        print(num)
        self.__close__()
        return {
            "total": num[1],
            "hombres": num[0],
            "mujeres": num[2]
        }
    
    
    def existe_empleado(self, codigo):
        self.__open__()
        self.cursor.execute("SELECT * FROM empleados WHERE id = ?", (codigo,))
        empleado = self.cursor.fetchone()
        self.__close__()
        
        if empleado:
            return True
        
        return False
        
    def darbaja_empleado(self, codigo , fecha_baja):
        self.__open__()
        try:
            self.cursor.execute("UPDATE empleados SET fecha_baja = ? WHERE id = ?", (fecha_baja, codigo))
            self.conexion.commit()
        except sqlite3.OperationalError as e:
            print(f"SQLite OperationalError: {e}")
        finally:
            self.__close__()