   def asignar_reserva(self, habitacion, fecha_fin):
        """Asigna una reserva a una habitación y calcula el tiempo ocioso si estaba vacía."""
        if habitacion["comprometida_hasta"] < self.tiempo_actual:
            # Calcular tiempo ocioso
            tiempo_ocioso = self.tiempo_actual - habitacion["comprometida_hasta"]
            habitacion.setdefault("tiempo_ocioso", 0)
            habitacion["tiempo_ocioso"] += tiempo_ocioso

        # Asignar la nueva reserva
        habitacion["comprometida_hasta"] = fecha_fin
        self.total_huespedes += 1