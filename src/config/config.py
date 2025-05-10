# Configuración de la simulación de hotel

# Parámetros de tipos de habitaciones
TIPOS_HABITACIONES = {
    "simple": {
        "cantidad": 15,
    },
    "doble": {
        "cantidad": 30,
    },
    "suite": {
        "cantidad": 5
    }
}

# Límites de recursos adicionales
RECURSOS_ADICIONALES = {
    "cunas": 4,
    "camas_extra": 7
}

# Parámetros de simulación
PARAMETROS_SIMULACION = {
    "duracion_simulacion": 365 * 24 * 3,  # horas
    # "seed": 10  # Para reproducir resultados
}