import re

class Validadores:
    @staticmethod
    def validar_nif(nif: str) -> bool:
        """Validar NIF español"""
        patron = r'^[0-9]{8}[A-Z]$'
        if not re.match(patron, nif):
            return False
        
        numeros = int(nif[:-1])
        letra = nif[-1]
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letra == letras[numeros % 23]

    @staticmethod
    def validar_numero_afiliacion_ss(naf: str) -> bool:
        """Validar Número de Afiliación a la Seguridad Social"""
        patron = r'^\d{12}$'
        return re.match(patron, naf) is not None

    @staticmethod
    def validar_email(email: str) -> bool:
        """Validar formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None