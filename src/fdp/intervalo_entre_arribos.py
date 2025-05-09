#!/usr/bin/env python3
import numpy as np

def generar_intervalo_entre_arribos():
    """Generar intervalo entre llegadas de huéspedes (en horas)"""
    # PENDING: Suposición: Distribución exponencial con media de 2 horas
    return np.random.exponential(2)