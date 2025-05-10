# Configuración de la simulación de hotel

# Parámetros de tipos de habitaciones
TIPOS_HABITACIONES = {
    "simple": {
        "cantidad": 15,
    },
    "doble": {
        "cantidad": 20,
    },
    "suite": {
        "cantidad": 15
    }
}

# Límites de recursos adicionales
RECURSOS_ADICIONALES = {
    "cunas": 5,
    "camas_extra": 10
}

# Parámetros de simulación
PARAMETROS_SIMULACION = {
    "duracion_simulacion": 365,  # días
    "seed": 10  # Para reproducir resultados
}