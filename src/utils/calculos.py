def imprimir_resultados(self):
    """Imprimir resultados de la simulación"""
    print("\n===== RESULTADOS DE LA SIMULACIÓN =====")
    print(f"Total de Arribos de Huéspedes: {self.total_arribos}")
    print(f"Porcentaje de Reservas Rechazadas: {self.reservas_rechazadas/self.total_arribos*100:.2f}%")
    print(f"Porcentaje de Bonificaciones: {self.bonificaciones/self.total_huespedes*100:.2f}%")

    # Calcular Porcentaje de tiempo ocioso para cada tipo de habitación
    pto_simples = self.calcular_pto(self.habitaciones_simples)
    pto_dobles = self.calcular_pto(self.habitaciones_dobles)
    pto_suites = self.calcular_pto(self.habitaciones_suites)

    print("\n===== Utilización de los Recursos =====")
    print(f"Habitaciones Simples: {pto_simples['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Habitaciones Dobles: {pto_dobles['porcentaje_ocioso']:.2f}% ociosidad")
    print(f"Suites: {pto_suites['porcentaje_ocioso']:.2f}% ociosidad")

def calcular_pto(self, recursos):
    """Calcular el Porcentaje de Tiempo Ocioso para un tipo de recurso"""
    tiempo_total = self.tiempo_simulacion * len(recursos) if recursos else 1
    tiempo_ocioso = 0

    for res in recursos:
        tiempo_ocioso += res.get("tiempo_ocioso", 0)

    return {
        "porcentaje_ocioso": (tiempo_ocioso * 100) / tiempo_total if tiempo_total > 0 else 0,
    }
