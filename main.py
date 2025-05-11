#!/usr/bin/env python3
from src.config.config import TIPOS_HABITACIONES, RECURSOS_ADICIONALES, PARAMETROS_SIMULACION
from src.eventos import HotelEventos
from src.utils import HotelUtils
from src.fdp import HotelFDP
from src.utils.calculos import calcular_pto
import random
import numpy as np

class HotelSimulation:
    def __init__(self,
        habitaciones_simples=10,
        habitaciones_dobles=15,
        habitaciones_suites=5,
        cunas=8,
        camas_simples=10,
        duracion_simulacion=365*24,
        seed=None):
        """
        Inicializar la simulación del hotel.
        Esta clase simula la llegada de huéspedes a un hotel, la asignación de habitaciones,
        la gestión de recursos auxiliares (camas adicionales y cunas) y el seguimiento de métricas
        de rendimiento.
        
        Parameters:
        -----------
        habitaciones_simples : int
            Numero de habitaciones simples en el hotel
        habitaciones_dobles : int
            Numero de habitaciones dobles en el hotel
        habitaciones_suites : int
            Numero de suites en el hotel
        cunas : int
            Numero de cunas disponibles en el hotel
        camas_simples : int
            Numero de camas adicionales disponibles en el hotel
        duracion_simulacion : int
            Duración de la simulación en horas
        seed : int, optional
            Semilla aleatoria para reproducibilidad
        """
        
        # # Set random seed 
        #if seed is not None:
        #    np.random.seed(seed)
        #    random.seed(seed)
        
        #Si no hay semilla fija, genero una al azar, pero la guardo para reproducir el resultado
        if seed is None:
            seed = random.randint(0, 2**32 - 1)
            print(f"Seed generada aleatoriamente: {seed}")
        else:
            print(f"Seed fija usada: {seed}")
        np.random.seed(seed)
        random.seed(seed)

        # Configuración del hotel
        self.habitaciones_simples = habitaciones_simples    # HS
        self.habitaciones_dobles = habitaciones_dobles      # HD
        self.habitaciones_suites = habitaciones_suites      # HU
        self.cunas = cunas                                  # CU
        self.camas_simples = camas_simples                  # SI
        
        # Parametros de la simulación
        self.tiempo_simulacion = duracion_simulacion
        self.tiempo_actual = 0  # Tiempo actual de la simulación
        
        # Inicializar habitaciones y recursos
        self.habitaciones_simples = [{"comprometida_hasta": 0} for _ in range(habitaciones_simples)]
        self.habitaciones_dobles = [{"comprometida_hasta": 0} for _ in range(habitaciones_dobles)]
        self.habitaciones_suites = [{"comprometida_hasta": 0} for _ in range(habitaciones_suites)]
        self.cunas = [{"comprometida_hasta": 0} for _ in range(cunas)]
        self.camas_simples = [{"comprometida_hasta": 0} for _ in range(camas_simples)]
        
        self.total_arribos = 0
        self.total_huespedes = 0
        self.reservas_rechazadas = 0
        self.rechazos_simple= 0
        self.rechazos_doble = 0
        self.rechazos_suite = 0
        self.rechazos_adicionales = 0
        self.bonificaciones = 0
        
        # Inicializar el primer evento de llegada
        self.tiempo_proxima_llegada = max(0, HotelFDP.generar_intervalo_entre_arribos(self.tiempo_actual))
        self.events = [("llegada", self.tiempo_proxima_llegada)]

    def correr_simulacion(self):
        print("Comenzando la simulacion...")

        hotel_eventos = HotelEventos()

        while self.tiempo_actual < self.tiempo_simulacion:
            # Manejar el evento de llegada de huéspedes
            self.tiempo_actual = self.tiempo_proxima_llegada

            # Procesar la llegada de huéspedes
            hotel_eventos.llegada_huesped(self)

            # Programar la próxima llegada
            self.tiempo_proxima_llegada = self.tiempo_actual + max(0, HotelFDP.generar_intervalo_entre_arribos(self.tiempo_actual))

            # Actualización del progreso cada semana simulada
            if int(self.tiempo_actual / 24) % 7 == 0:
                dias_simulados = int(self.tiempo_actual / 24)
                # print(f"{dias_simulados} dias simulados...")
        
        print("Simulacion finalizada")
        HotelUtils.imprimir_resultados(
            self.total_arribos,
            self.reservas_rechazadas,
            self.rechazos_adicionales,
            self.rechazos_suite,
            self.rechazos_simple,
            self.rechazos_doble,
            self.bonificaciones,
            self.total_huespedes,
            self.habitaciones_simples,
            self.habitaciones_dobles,
            self.habitaciones_suites,
            calcular_pto,
            self.tiempo_simulacion
        )
    

if __name__ == "__main__":
    # Variables de control de la simulación
    config = {
        "habitaciones_simples": TIPOS_HABITACIONES["simple"]["cantidad"],
        "habitaciones_dobles": TIPOS_HABITACIONES["doble"]["cantidad"],
        "habitaciones_suites": TIPOS_HABITACIONES["suite"]["cantidad"],
        "cunas": RECURSOS_ADICIONALES["cunas"],
        "camas_simples": RECURSOS_ADICIONALES["camas_extra"],
        "duracion_simulacion": PARAMETROS_SIMULACION["duracion_simulacion"]#,
        #"seed": PARAMETROS_SIMULACION.get("seed", None)
    }
    
    # Crear instancia de la simulación
    # y ejecutar la simulación
    sim = HotelSimulation(**config)
    sim.correr_simulacion()
    HotelUtils.graficar_resultados(
        sim.tiempo_simulacion,
        sim.habitaciones_simples,
        sim.habitaciones_dobles,
        sim.habitaciones_suites,
        sim.total_arribos,
        sim.reservas_rechazadas,
        sim.rechazos_suite,
        sim.rechazos_doble,
        sim.rechazos_simple,
        sim.rechazos_adicionales,
        sim.total_huespedes,
        sim.bonificaciones,
        calcular_pto
    )