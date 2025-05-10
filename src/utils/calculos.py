def imprimir_resultados(total_arribos, reservas_rechazadas, rechazos_adicionales,rechazos_suite,rechazos_simple,rechazos_doble, bonificaciones, total_huespedes, habitaciones_simples, habitaciones_dobles, habitaciones_suites, calcular_pto, tiempo_simulacion,guardar_csv=True,camas_simples=None, cunas=None):
    """Imprimir resultados de la simulación"""
    print("\n===== RESULTADOS DE LA SIMULACIÓN =====")
    print(f"Total de Arribos de Huéspedes: {total_arribos}")
    porcentaje_rechazos = (reservas_rechazadas/total_arribos*100) if total_arribos > 0 else 0
    print(f"Porcentaje de Reservas Rechazadas: {porcentaje_rechazos:.2f}%")
    print(f"De las cuales:")
    print(f"Reservas Rechazadas por Habitacion Suite: {rechazos_suite/reservas_rechazadas*100:.2f}%")
    print(f"Reservas Rechazadas por Habitacion Doble: {rechazos_doble/reservas_rechazadas*100:.2f}%")
    print(f"Reservas Rechazadas por Habitacion Simple: {rechazos_simple/reservas_rechazadas*100:.2f}%")
    print(f"Reservas Rechazadas por falta de cunas o camas simples: {rechazos_adicionales/reservas_rechazadas*100:.2f}%")

    porcentaje_bonificaciones = (bonificaciones / total_arribos * 100) if total_huespedes > 0 else 0
    print(f"Porcentaje de Bonificaciones: {porcentaje_bonificaciones:.2f}%")

    # Calcular Porcentaje de tiempo ocioso para cada tipo de habitación
    pto_simples = calcular_pto(tiempo_simulacion, habitaciones_simples)
    pto_dobles = calcular_pto(tiempo_simulacion, habitaciones_dobles)
    pto_suites = calcular_pto(tiempo_simulacion, habitaciones_suites)

    print("\n===== Utilización de los Recursos =====")
    print(f"Habitaciones Simples: {pto_simples['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Habitaciones Dobles: {pto_dobles['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Suites: {pto_suites['porcentaje_ocioso']:.2f}% ociosidad")
    
    # Guardar resultados en archivo CSV
    if guardar_csv:
        print("\n===== Guardando resultados en archivo =====")
        guardar_resultados(
            "resultados_simulacion",  # nombre del archivo
            len(habitaciones_suites),  # cantidad de suites
            len(habitaciones_dobles),  # cantidad de habitaciones dobles
            len(habitaciones_simples), # cantidad de habitaciones simples
            len(cunas),  # cantidad de cunas
            len(camas_simples),  # cantidad de camas simples
            total_arribos,
            porcentaje_rechazos,
            rechazos_suite,
            rechazos_doble,
            rechazos_simple,
            porcentaje_bonificaciones,
            pto_suites['porcentaje_ocioso'],
            pto_dobles['porcentaje_ocioso'],
            pto_simples['porcentaje_ocioso']
        )
        print(f"Resultados guardados en 'resultados/resultados_simulacion.csv'")

def calcular_pto(tiempo_simulacion, recursos):
    """Calcular el Porcentaje de Tiempo Ocioso para un tipo de recurso"""
    tiempo_total = tiempo_simulacion * len(recursos) if recursos else 1
    tiempo_ocioso = 0

    for res in recursos:
        tiempo_ocioso += res.get("tiempo_ocioso", 0)

    return {
        "porcentaje_ocioso": (tiempo_ocioso * 100) / tiempo_total if tiempo_total > 0 else 0,
    }
    
def guardar_resultados(nombre_archivo, habitaciones_suites, habitaciones_dobles, 
                      habitaciones_simples, cunas, camas_simples, total_arribos, 
                      porcentaje_rechazos, rechazos_suite, rechazos_doble, rechazos_simple,
                      porcentaje_bonificaciones, pto_suites, pto_dobles, pto_simples):
    """
    Guarda los resultados de la simulación en un archivo CSV.
    
    Las variables se organizan como columnas y cada simulación es una fila nueva.
    Si el archivo no existe, lo crea con los encabezados adecuados.
    """
    import os
    import csv
    from datetime import datetime
    
    # Construir la ruta completa al archivo
    ruta_archivo = f"resultados/{nombre_archivo}.csv"
    
    # Asegurarse de que el directorio resultados exista
    os.makedirs("resultados", exist_ok=True)
    
    # Obtener la fecha y hora actual para identificar la simulación
    fecha_simulacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Definir los encabezados (nombres de columnas)
    headers = [
        "Fecha Simulación",
        "Cantidad de Habitaciones Suite",
        "Cantidad de Habitaciones Dobles",
        "Cantidad de Habitaciones Simples",
        "Cantidad de Cunas",
        "Cantidad de Camas Simples",
        "Total de arribos",
        "Porcentaje de Rechazos",
        "Rechazos Suite",
        "Rechazos Doble",
        "Rechazos Simple",
        "Porcentaje de Bonificaciones",
        "Porcentaje Ocioso Habitaciones Suite",
        "Porcentaje Ocioso Habitaciones Dobles",
        "Porcentaje Ocioso Habitaciones Simples"
    ]
    
    # Preparar los datos de esta simulación
    row_data = [
        fecha_simulacion,
        habitaciones_suites,
        habitaciones_dobles,
        habitaciones_simples,
        cunas,
        camas_simples,
        total_arribos,
        f"{porcentaje_rechazos:.2f}%",
        rechazos_suite,
        rechazos_doble,
        rechazos_simple,
        f"{porcentaje_bonificaciones:.2f}%",
        f"{pto_suites:.2f}%",
        f"{pto_dobles:.2f}%",
        f"{pto_simples:.2f}%"
    ]
    
    # Si el archivo existe, añadir una nueva fila
    if os.path.isfile(ruta_archivo):
        with open(ruta_archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)
    else:
        # Crear un nuevo archivo
        with open(ruta_archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Escribir encabezados
            writer.writerow(row_data)  # Escribir la primera fila de datos
