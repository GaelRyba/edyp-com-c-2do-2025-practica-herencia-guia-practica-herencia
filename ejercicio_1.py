class Vehiculo():
    patentes_T = []
    patentes_A = []
    vehiculos = []
    def __init__(self, patente, marca, anio):
        self.patente = patente
        self.marca = marca
        self.anio = self.valida_anio(anio)
        
    def valida_anio(self, anio):
        if not isinstance(anio, int):
            raise TypeError ('El anio debe ser un numero entero')
        return anio
    
    def valida_patente_T(self, patente):
        if patente in Vehiculo.patentes_T:
            raise ValueError ('La patente ya esta registrada en patentes de vehiculos terrestres.')
        Vehiculo.patentes_T.append(patente)
        return patente
            
    def valida_patente_A(self, patente):
        if patente in Vehiculo.patentes_A:
            raise ValueError ('La patente ya esta registrada en patentes de vehiculos acuaticos.')
        Vehiculo.patentes_A.append(patente)
        return patente

    def __str__(self):
        return f'Patente: {self.patente}\nMarca: {self.marca}\nAnio: {self.anio}'
    
class Camion(Vehiculo):
    camiones = []
    def __init__(self, patente, marca, carga, anio):
        patente = self.valida_patente_T(patente)
        super().__init__(patente, marca, anio)
        self.carga = self.valida_carga(carga)
        self.ruedas = 8
        Camion.camiones.append(self)
        Vehiculo.vehiculos.append(self)
    
    def __str__(self):
        info = super().__str__()
        return f'{info}\nCarga: {self.carga}'
    
    def valida_carga(self, carga):
        if not isinstance(carga, int):
            raise TypeError ('La carga debe ser un entero.')
        return carga

    def modificar_carga(self, carga):
        self.carga = self.setter_carga(carga)
        print('La carga a sido modificada.')
        
    def setter_carga(self,carga):
        return carga  
    
class Auto(Vehiculo):
    autos = []
    def __init__(self, patente, marca, anio):
        patente = self.valida_patente_T(patente)
        super().__init__(patente, marca, anio)
        self.ruedas = 4
        self.kilometraje = 0
        Auto.autos.append(self)
        Vehiculo.vehiculos.append(self)
    
    def trasladarse(self, desplazamiento):
        if not isinstance(desplazamiento, int):
            raise TypeError ('El desplazamiento debe ser un numero entero')
        self.kilometraje += desplazamiento
        return(f'El vehiculo se a desplazado por tierra {desplazamiento}km.')
    
    def __str__(self):
        info = super().__str__()
        return f'{info}\nKilometraje: {self.kilometraje}'

class Lancha(Vehiculo):
    lanchas = []
    def __init__(self, patente, marca, marca_motor, anio):
        patente = self.valida_patente_A(patente)
        super().__init__(patente, marca, anio)
        self.kilometraje = 0
        self.marca_motor = marca_motor
        Lancha.lanchas.append(self)
        Vehiculo.vehiculos.append(self)
    
    def trasladarse(self, desplazamiento):
        if not isinstance(desplazamiento, int):
            raise TypeError ('El desplazamiento debe ser un numero entero')
        self.kilometraje += desplazamiento
        return(f'El vehiculo se a desplazado por agua a motor {desplazamiento}km.')
    
    def __str__(self):
        info = super().__str__()
        return f'{info}\nKilometraje: {self.kilometraje}\nMarca del Motor: {self.marca_motor}'

class Velero(Vehiculo):
    veleros = []
    def __init__(self, patente, marca, cantidad_velas, anio):
        patente = self.valida_patente_A(patente)
        super().__init__(patente, marca, anio)
        self.kilometraje = 0
        self.cantidad_velas = self.valida_cantidad_velas(cantidad_velas)
        Velero.veleros.append(self)
        Vehiculo.vehiculos.append(self)
    
    def valida_cantidad_velas(self, cantidad_velas):
        if not isinstance(cantidad_velas, int):
            raise TypeError ('La cantidad de velas debe ser un numero entero.')
        return cantidad_velas
    
    def trasladarse(self, desplazamiento):
        if not isinstance(desplazamiento, int):
            raise TypeError ('El desplazamiento debe ser un numero entero')
        self.kilometraje += desplazamiento
        return(f'El vehiculo se a desplazado por agua a vela {desplazamiento}km.')
    
    def __str__(self):
        info = super().__str__()
        return f'{info}\nKilometraje: {self.kilometraje}\nCantidad de velas: {self.cantidad_velas}'

class Anfibio(Vehiculo):
    anfibios = []
    def __init__(self, patente, marca, marca_motor, anio):
        patente = self.valida_patente_T(patente)
        super().__init__(patente, marca, anio)
        self.kilometraje = 0
        self.marca_motor = marca_motor
        Anfibio.anfibio.append(self)
        Vehiculo.vehiculos.append(self)
    
    def trasladarse(self, desplazamiento):
        if not isinstance(desplazamiento, int):
            raise TypeError ('El desplazamiento debe ser un numero entero')
        self.kilometraje += desplazamiento
        return(f'El vehiculo se a desplazado por tierra {desplazamiento}km.')
    
    def trasladarse_agua(self, desplazamiento):
        if not isinstance(desplazamiento, int):
            raise TypeError ('El desplazamiento debe ser un numero entero')
        self.kilometraje += desplazamiento
        return(f'El vehiculo se a desplazado por agua a motor {desplazamiento}km.')
    
    def __str__(self):
        info = super().__str__()
        return f'{info}\nKilometraje: {self.kilometraje}\nMarca del Motor: {self.marca_motor}'