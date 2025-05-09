def asignar_reserva(habitacion, fecha_fin, tiempo_actual, total_huespedes):
    """Asigna una reserva a una habitación y calcula el tiempo ocioso si estaba vacía."""
    if habitacion["comprometida_hasta"] < tiempo_actual:
        # Calcular tiempo ocioso
        tiempo_ocioso = tiempo_actual - habitacion["comprometida_hasta"]
        habitacion.setdefault("tiempo_ocioso", 0)
        habitacion["tiempo_ocioso"] += tiempo_ocioso

    # Asignar la nueva reserva
    habitacion["comprometida_hasta"] = fecha_fin
    total_huespedes += 1
    return total_huespedes