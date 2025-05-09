#!/usr/bin/env python3
import numpy as np

def generar_num_ninios():
    """Generar número de niños"""
    # PENDING: Distribución de Poisson con media de 0.8
    return np.random.poisson(0.8)