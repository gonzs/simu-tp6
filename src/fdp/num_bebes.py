#!/usr/bin/env python3
import numpy as np

def generar_num_bebes():
    """Generar número de bebés"""
    
    probs = [0.99340227,0.00642468,0.00012979,0.00002163,0.00002163]
    return np.random.choice([0,1,2,9,10], p=probs)