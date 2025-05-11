#!/usr/bin/env python3
import numpy as np
from scipy.stats import weibull_min
from datetime import datetime, timedelta

PARAMS_WEIBULL_POR_MES = {
        1: (0.6687, -0.0, 45.8101), 
        2: (0.6876, -0.0, 29.2809), 
        3: (0.7166, 0.0167, 19.0633), 
        4: (0.695, -0.0, 17.6058), 
        5: (0.7022, -0.0, 16.2093), 
        6: (0.6847, -0.0, 17.1343), 
        7: (0.6703, -0.0, 22.2839), 
        8: (0.6926, 0.0167, 21.8141), 
        9: (0.7028, -0.0, 16.2188), 
        10: (0.6783, -0.0, 18.7329), 
        11: (0.655, 0.0167, 31.0093), 
        12: (0.6712, -0.0, 46.9967)
}

def obtener_mes_simulacion(t_horas):
    """
    Dado un tiempo t en horas desde el inicio de la simulación,
    devuelve el mes calendario correspondiente (1 = enero, ..., 12 = diciembre).
    """
    # Convertimos t en días y horas
    fecha_inicio = datetime(2025, 1, 1)  # año ficticio, sirve solo para usar datetime
    fecha_simulada = fecha_inicio + timedelta(hours=t_horas)
    return fecha_simulada.month

def generar_intervalo_entre_arribos(t_horas):
    """Generar intervalo entre llegadas de huéspedes (en horas)"""
    # R = np.random.random()
    # return -math.log(1 - R) / 0.499

    # Obtener el mes de la simulación
    mes = obtener_mes_simulacion(t_horas)
    
    # Parámetros Weibull para el mes correspondiente
    shape, loc, scale = PARAMS_WEIBULL_POR_MES[mes]
    R = np.random.uniform()
    return weibull_min.ppf(R, shape, loc=loc, scale=scale)
