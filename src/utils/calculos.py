def imprimir_resultados(total_arribos, reservas_rechazadas, bonificaciones, total_huespedes, habitaciones_simples, habitaciones_dobles, habitaciones_suites, calcular_pto, tiempo_simulacion):
    """Imprimir resultados de la simulación"""
    print("\n===== RESULTADOS DE LA SIMULACIÓN =====")
    print(f"Total de Arribos de Huéspedes: {total_arribos}")
    print(f"Porcentaje de Reservas Rechazadas: {reservas_rechazadas/total_arribos*100:.2f}%")
    
    porcentaje_bonificaciones = (bonificaciones / total_huespedes * 100) if total_huespedes > 0 else 0
    print(f"Porcentaje de Bonificaciones: {porcentaje_bonificaciones:.2f}%")

    # Calcular Porcentaje de tiempo ocioso para cada tipo de habitación
    pto_simples = calcular_pto(tiempo_simulacion, habitaciones_simples)
    pto_dobles = calcular_pto(tiempo_simulacion, habitaciones_dobles)
    pto_suites = calcular_pto(tiempo_simulacion, habitaciones_suites)

    print("\n===== Utilización de los Recursos =====")
    print(f"Habitaciones Simples: {pto_simples['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Habitaciones Dobles: {pto_dobles['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Suites: {pto_suites['porcentaje_ocioso']:.2f}% ociosidad")

def calcular_pto(tiempo_simulacion, recursos):
    """Calcular el Porcentaje de Tiempo Ocioso para un tipo de recurso"""
    tiempo_total = tiempo_simulacion * len(recursos) if recursos else 1
    tiempo_ocioso = 0

    for res in recursos:
        tiempo_ocioso += res.get("tiempo_ocioso", 0)

    return {
        "porcentaje_ocioso": (tiempo_ocioso * 100) / tiempo_total if tiempo_total > 0 else 0,
    }
