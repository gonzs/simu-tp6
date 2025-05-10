#!/usr/bin/env python3
import numpy as np
from scipy.stats import gamma

def generar_intervalo_entre_arribos():
    """Generar intervalo entre llegadas de huéspedes (en horas)"""
    # R = random.random()
    # return -math.log(1 - R) / 0.499

    # Distribución Gamma
    # Parámetros de la distribución Gamma
    a = 0.9493717645899579
    loc = -1.1394098234608795e-26
    scale = 0.09213445691039115
    R = np.random.rand()

    # Generar con método de inversa (usando la ppf de scipy)
    return gamma.ppf(R, a, loc=loc, scale=scale)
   
