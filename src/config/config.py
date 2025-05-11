# Configuración de la simulación de hotel

# Parámetros de tipos de habitaciones
TIPOS_HABITACIONES = {
    "simple": {
        "cantidad": 8,
    },
    "doble": {
        "cantidad": 38,
    },
    "suite": {
        "cantidad": 6
    }
}

# Límites de recursos adicionales
RECURSOS_ADICIONALES = {
    "cunas": 12,
    "camas_extra": 12
}

# Parámetros de simulación
PARAMETROS_SIMULACION = {
    "duracion_simulacion": 365 * 24 * 3,  # horas
    # "seed": 10  # Para reproducir resultados
}