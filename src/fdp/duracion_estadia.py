#!/usr/bin/env python3
import numpy as np
from scipy.stats import gennorm
import random
import math
from scipy.stats import norm

def generar_duracion_estadia():
    """Generar duración de la estadía (en horas)"""
    # PENDING: Suposición: Distribución normal con media de 3 días, desviación estándar de 1 día
    R = random.random()  # R ~ U(0,1)
    mu = math.log(507.69)
    sigma = 0.04605
    return math.exp(mu + sigma * norm.ppf(R)) - 435.97
