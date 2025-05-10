#!/usr/bin/env python3
import numpy as np
from scipy.stats import dweibull

def generar_duracion_estadia():
    """Generar duración de la estadía (en horas)"""
    # Distribución Weibull
    # Parámetros de la distribución Weibull
    c= 0.3510566987873381
    loc= 2.9999999999999996
    scale= 0.9263278639266157
    R = np.random.rand()

    # Generar método de inversa (usando la ppf de scipy)
    ia_inversa = dweibull.ppf(R, c=c, loc=loc, scale=scale).astype(int)

    # Convertir de días a horas y asegurar entre 24 (1 día) y 192 (8 días)
    duracion_en_horas = np.clip(ia_inversa, 1, 8) * 24
    return duracion_en_horas
