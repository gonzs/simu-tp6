#!/usr/bin/env python3
import numpy as np

def generar_duracion_estadia():
    """Generar duración de la estadía (en horas)"""
    # PENDING: Suposición: Distribución normal con media de 3 días, desviación estándar de 1 día
    return max(24, np.random.normal(3 * 24, 24))