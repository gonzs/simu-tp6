#!/usr/bin/env python3
import numpy as np
from scipy.stats import exponnorm
import random 
import math 

def generar_intervalo_entre_arribos():
    """Generar intervalo entre llegadas de huéspedes (en horas)"""
    R = random.random()
    return -math.log(1 - R) / 0.499