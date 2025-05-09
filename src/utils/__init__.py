from .calculos import *
from .disponibilidades import *
from .graficos import *
from .reserva import *

class HotelUtils:
    encontrar_habitacion_disponible = staticmethod(encontrar_habitacion_disponible)
    encontrar_cunas_disponibles = staticmethod(encontrar_cunas_disponibles)
    encontrar_camas_disponibles = staticmethod(encontrar_camas_disponibles)
    asignar_reserva = staticmethod(asignar_reserva)
    imprimir_resultados = staticmethod(imprimir_resultados)
    graficar_resultados = staticmethod(graficar_resultados)