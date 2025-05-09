from .duracion_estadia import generar_duracion_estadia
from .intervalo_entre_arribos import generar_intervalo_entre_arribos
from .num_bebes import generar_num_bebes
from .num_ninios import generar_num_ninios
from .tipo_habitacion import generar_tipo_habitacion

class HotelFDP:
    generar_duracion_estadia = staticmethod(generar_duracion_estadia)
    generar_intervalo_entre_arribos = staticmethod(generar_intervalo_entre_arribos)
    generar_num_bebes = staticmethod(generar_num_bebes)
    generar_num_ninios = staticmethod(generar_num_ninios)
    generar_tipo_habitacion = staticmethod(generar_tipo_habitacion)

__all__ = [
    "HotelFDP",
]