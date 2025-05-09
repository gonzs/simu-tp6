def encontrar_habitacion_disponible(self, tipo_habitacion, fecha_inicio):
        """Encontrar una habitación disponible del tipo especificado para el período de tiempo dado.
        Devuelve la habitación comprometida hasta la menor fecha de compromiso."""
        habitaciones = []
        if tipo_habitacion == "simple":
            habitaciones = self.habitaciones_simples
        elif tipo_habitacion == "doble":
            habitaciones = self.habitaciones_dobles
        elif tipo_habitacion == "suite":
            habitaciones = self.habitaciones_suites

        # Ordenar las habitaciones por la fecha de compromiso
        habitaciones_disponibles = [
            (i, habitacion["comprometida_hasta"]) for i, habitacion in enumerate(habitaciones)
            if habitacion["comprometida_hasta"] <= fecha_inicio
        ]
        habitaciones_disponibles.sort(key=lambda x: x[1])

        # Devolver la primera habitación disponible si existe
        return habitaciones_disponibles[0][0] if habitaciones_disponibles else None

def encontrar_cunas_disponibles(self, numero_solicitado, fecha_inicio):
    """Encontrar las cunas disponibles para el período de tiempo dado."""
    cunas_disponibles = []
    for i, cuna in enumerate(self.cunas):
        if cuna["comprometida_hasta"] <= fecha_inicio:
            cunas_disponibles.append((i, cuna["comprometida_hasta"]))

    # Ordenar las cunas por la fecha en que se liberan (comprometida_hasta)
    cunas_disponibles.sort(key=lambda x: x[1])

    # Seleccionar las cunas necesarias
    cunas_seleccionadas = [cuna[0] for cuna in cunas_disponibles[:numero_solicitado]]

    return cunas_seleccionadas if len(cunas_seleccionadas) == numero_solicitado else None

def encontrar_camas_disponibles(self, numero_solicitado, fecha_inicio):
    """Encontrar camas disponibles para el período de tiempo dado"""
    camas_disponibles = []
    for i, cama in enumerate(self.camas_simples):
        if cama["comprometida_hasta"] <= fecha_inicio:
            camas_disponibles.append((i, cama["comprometida_hasta"]))

    # Ordenar las camas por la fecha en que se liberan (comprometida_hasta)
    camas_disponibles.sort(key=lambda x: x[1])

    # Seleccionar las camas necesarias
    camas_seleccionadas = [cama[0] for cama in camas_disponibles[:numero_solicitado]]

    return camas_seleccionadas if len(camas_seleccionadas) == numero_solicitado else None