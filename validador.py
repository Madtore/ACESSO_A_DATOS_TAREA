import re


class Validador():

    def __init__(self):
        self.comprobar = {
    '0': "T",
    '1': "R",
    '2': "W",
    '3': "A",
    '4': "G",
    '5': "M",
    '6': "Y",
    '7': "F",
    '8': "P",
    '9': "D",
    '10': "X",
    '11': "B",
    '12': "N",
    '13': "J",
    '14': "Z",
    '15': "S",
    '16': "Q",
    '17': "V",
    '18': "H",
    '19': "L",
    '20': "C",
    '21': "K",
    '22': "E"
}
        
    def validador_paga_extra(self, valor ):
        regex = r'^[1-4]$'
        return re.match(regex, valor)

    def validadorGeneral(self, valor ):
        return valor != ""
    

    def validadorFecha(self, valor ):
        regex = r"^\d{4}-\d{2}-\d{2}$"
        return re.match(regex, valor)
    

    def validadorTelefono(self, valor ):
        regex = r'^\+\d{9}$'
        return re.match(regex, valor)
    

    def validarGenero(self, valor ):
        regex = r'^(Hombre|Mujer)$'
        return re.match(regex, valor)
    

    def validaraSalario(self, valor ):
        regex = r'^\d+\.\d{2}$'
        return re.match(regex, valor)
    

    def validarEmail(self, valor ):

        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        return re.match(regex, valor)
    


    def validar_nif(self, nif):
        """
        validar nif 
        """

        nif = nif.replace(" ", "")
        nif = nif.upper()
        regexNie = r'^([ZXY])(\d{7})([A-Z])$'
        regexNif = r'^(\d{8})([A-Z]$)' 
        nieComp = re.match(regexNie, nif)

        if nieComp:

            if nif[0] == 'X':
               nif =  '0'+ nif[1:]
            elif nif[0] == 'Y':
                nif =  '1'+ nif[1:]
            elif nif[0] == 'Z':
                nif =  '2'+ nif[1:]

        nifComp = re.match(regexNif, nif)          
        if not nifComp:
            return False

        letra = nifComp.group(2)
        result = int(nifComp.group(1))-(int(int(nifComp.group(1))/ 23)*23)
        if self.comprobar[str(result)] != letra:
            return False  
        return True


    def validar_naf(self , naf):
        """
        validar naf 
        """
        naf = naf.replace(" ", "")
        regexNaf = r"^(\d{2})(\d{8})(\d{2})$"
        nafComp = re.match(regexNaf, naf)

        if not nafComp:
            return False

        a = nafComp.group(1)
        b = nafComp.group(2)
        c = nafComp.group(3)

        if int(b) < 1000000:
            if (int(b) + int(a) * 1000000) % 97 != int(c):
                return False
        else:
            if ( int(a+b)) % 97 != int(c):
                return False

        return True


    def validar_ccc(self, ccc):        
        """
        validar ccc
        """
        ccc = ccc.replace(" ", "")
        regexCcc = r'^(\d{4})(\d{4})(\d{2})(\d{10})$'
        cccComp = re.match(regexCcc, ccc)
        if not cccComp:
            return False

        entidad = cccComp.group(1)
        sucursal = cccComp.group(2)
        digitos = cccComp.group(3)
        cod_cuenta = cccComp.group(4)

        suma_entidad = (int(entidad[0])*4 + 
                        int(entidad[1])*8 + 
                        int(entidad[2])*5 + 
                        int(entidad[3])*10) 

        suma_sucursal = (int(sucursal[0])*9 + 
                         int(sucursal[1])*7 + 
                         int(sucursal[2])*3 + 
                         int(sucursal[3])*6)

        primerer_digito = 11 - ((suma_entidad + suma_sucursal) % 11)

        if primerer_digito == 10:
            primerer_digito = 1

        suma_cod_cuenta = (int(cod_cuenta[0])*1 
                           + int(cod_cuenta[1])*2 
                           + int(cod_cuenta[2])*4 
                           + int(cod_cuenta[3])*8 
                           + int(cod_cuenta[4])*5
                           + int(cod_cuenta[5])*10
                           + int(cod_cuenta[6])*9
                           + int(cod_cuenta[7])*7
                           + int(cod_cuenta[8])*3
                           + int(cod_cuenta[9])*6
                           )
        segundo_digito = 11 - (suma_cod_cuenta % 11)

        if segundo_digito == 10:
            segundo_digito = 1

        if primerer_digito == int(digitos[0]) and segundo_digito == int(digitos[1]):
            return True

        return False


    def generar_iban(self , ccc):
        """
        generar iban
        """
        if not validar_ccc(ccc):
            return None

        ccc = ccc.replace(" ", "")
        codigo_pais = "142800"
        secuencia = ccc + codigo_pais

        resta = int(secuencia) % 97
        cont_dig = 98 - resta    
        digito_control = f"{cont_dig}"

        iban = f"ES{digito_control}{ccc}"
        return iban
    
    
    
    