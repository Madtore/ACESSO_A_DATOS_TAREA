from dataclasses import dataclass
from datetime import date

@dataclass
class Empleado:
    codigo: str
    apellidos: str
    nombre: str
    fecha_nacimiento: date
    nif: str
    direccion: str
    telefono: str
    email: str
    genero: str
    departamento: str
    puesto: str
    fecha_inicio: date
    datos_bancarios: str
    numero_afiliacion_ss: str
    salario_mensual: float
    pagas_extra: int
    irpf_porcentaje: float

    def calcular_edad(self) -> int:
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )