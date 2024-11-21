

class Empleado():        
    def __init__(self, **kwargs):
        self.codigo = kwargs.get("codigo" or None)
        self.apellido_nombre = kwargs.get("apellido_nombre" )
        self.fecha_inicio = kwargs.get("fecha_inicio")
        self.fecha_nacimiento = kwargs.get("fecha_nacimiento")
        self.direccion = kwargs.get("direccion")
        self.nif = kwargs.get("nif")
        self.datos_bancarios = kwargs.get("datos_bancarios")
        self.numero_seguro_social = kwargs.get("numero_seguro_social")
        self.genero = kwargs.get("genero")
        self.departamento = kwargs.get("departamento")
        self.puesto = kwargs.get("puesto")
        self.telefono = kwargs.get("telefono")
        self.email = kwargs.get("email")
        self.salario_mensual = kwargs.get("salario_mensual")
        self.paga_extra = kwargs.get("paga_extra")
        self.irpf = kwargs.get("irpf")
        self.seg_social = kwargs.get("seg_social")
        self.fecha_baja = kwargs.get("fecha_baja")
        
        
    def __str__(self):
        return f"{self.apellido_nombre} - {self.salario_mensual} - {self.paga_extra} - {self.departamento} - {self.puesto} - {self.telefono} - {self.email} - {self.direccion} - {self.nif} - {self.datos_bancarios} - {self.numero_seguro_social} - {self.genero} - {self.fecha_inicio} - {self.fecha_nacimiento} - {self.irpf} - {self.seg_social} , {self.fecha_baja}"  