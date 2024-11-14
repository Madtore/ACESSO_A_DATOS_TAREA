import sqlite3
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
            paga_extra REAL NOT NULL,
            irpf REAL NOT NULL,
            seg_social REAL NOT NULL,
            fecha_baja DATE 
        )"""
        ) 
        self.conexion.commit()
        self.conexion.close()
        
    def __close__(self):
        self.conexion.close()
        
    def __open__(self):
        self.conexion = sqlite3.connect("empleados.db")
        self.cursor = self.conexion.cursor()
        
    def insertar(self,empleado):
        try:
            self.__open__()
            # Insert statement with placeholders for the values
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
      
   
    def darbaja(self, empleado, fecha_baja):
        self.__open__()
        self.cursor.execute("""
                            UPDATE empleados
                            SET fecha_baja = ?
                            WHERE id = ?
                            """, fecha_baja, empleado)
        self.conexion.commit()
        self.__close__()
        
    def buscar_empleado(self, codigo):
        self.__open__
        self.cursor.execute("SELECT * FROM empleados WHERE id = ?", (codigo,))
        empleado = self.cursor.fetchone()
        self.__close__
        return empleado
       
     
        
        
   
    
        
        
    