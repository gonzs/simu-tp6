#!/usr/bin/env python3
import numpy as np

def generar_tipo_habitacion():
    """Generar tipo de habitación solicitada"""
    # PENDING: Probabilidades para simple, doble, suite
    probs = [0.4, 0.5, 0.1]
    return np.random.choice(["simple", "doble", "suite"], p=probs)