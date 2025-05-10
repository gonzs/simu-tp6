#!/usr/bin/env python3
import numpy as np

def generar_tipo_habitacion():
    """Generar tipo de habitación solicitada"""
    # PENDING: Probabilidades para simple, doble, suite
    probs = [0.16485680, 0.76462317, 0.07052003]
    return np.random.choice(["simple", "doble", "suite"], p=probs)