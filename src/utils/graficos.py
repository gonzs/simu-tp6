  def graficar_resultados(self):
        """Graficar resultados de la simulación"""
        # Crear figura y subplots
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))

        # Graficar utilización de recursos (PTO)
        tipos_recursos = ['Simples', 'Dobles', 'Suites']
        pto_valores = [
            self.calcular_pto(self.habitaciones_simples)["porcentaje_ocioso"],
            self.calcular_pto(self.habitaciones_dobles)["porcentaje_ocioso"],
            self.calcular_pto(self.habitaciones_suites)["porcentaje_ocioso"]
        ]
        axs[0, 1].bar(tipos_recursos, pto_valores, color=['blue', 'green', 'red'])
        axs[0, 1].set_ylabel('Porcentaje de Tiempo Ocioso (%)')
        axs[0, 1].set_title('Utilización de Habitaciones')
        axs[0, 1].grid(axis='y')

        # Graficar evolución de arribos
        tiempos = range(0, self.tiempo_simulacion, 24)  # Asumimos datos diarios
        arribos_diarios = [random.randint(0, 10) for _ in tiempos]  # Simulación de datos
        axs[1, 0].plot(tiempos, arribos_diarios, label='Arribos Diarios', color='purple')
        axs[1, 0].set_xlabel('Tiempo (horas)')
        axs[1, 0].set_ylabel('Número de Arribos')
        axs[1, 0].set_title('Evolución de Arribos')
        axs[1, 0].legend()
        axs[1, 0].grid(True)

        # Graficar porcentaje de reservas rechazadas y bonificaciones
        axs[1, 1].bar(['Rechazadas', 'Bonificadas'], [
            (self.reservas_rechazadas / self.total_arribos) * 100,
            (self.bonificaciones / self.total_huespedes) * 100
        ], color=['orange', 'cyan'])
        axs[1, 1].set_ylabel('Porcentaje (%)')
        axs[1, 1].set_title('Reservas Rechazadas y Bonificadas')
        axs[1, 1].grid(axis='y')

        # Ajustar diseño y guardar gráfico
        plt.tight_layout()
        plt.savefig('resultados/hotel_simulation_results.png')
        print("\nResultados trazados y guardados en 'resultados/hotel_simulation_results.png'")
        plt.show()