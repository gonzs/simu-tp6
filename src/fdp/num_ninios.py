#!/usr/bin/env python3
import numpy as np

def generar_num_ninios():
    """Generar número de niños"""
    # PENDING: Distribución de Poisson con media de 0.8
    probs = [0.92874448,0.04356667,0.02673704,0.0009518]
    return np.random.choice([0,1,2,3], p=probs)