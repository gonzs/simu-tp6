import matplotlib.pyplot as plt
import random

def graficar_resultados(tiempo_simulacion, habitaciones_simples, habitaciones_dobles, habitaciones_suites, total_arribos, reservas_rechazadas,rechazos_suite,rechazos_doble,rechazos_simple,rechazos_adicionales, total_huespedes, bonificaciones, calcular_pto):
    """Graficar resultados de la simulación"""
    # Crear figura y subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # Graficar utilización de recursos (PTO)
    tipos_recursos = ['Simples', 'Dobles', 'Suites']
    pto_valores = [
        calcular_pto(tiempo_simulacion, habitaciones_simples)["porcentaje_ocioso"],
        calcular_pto(tiempo_simulacion, habitaciones_dobles)["porcentaje_ocioso"],
        calcular_pto(tiempo_simulacion, habitaciones_suites)["porcentaje_ocioso"]
    ]
    axs[0, 1].bar(tipos_recursos, pto_valores, color=['blue', 'green', 'red'])
    axs[0, 1].set_ylabel('Porcentaje de Tiempo Ocioso (%)')
    axs[0, 1].set_title('Utilización de Habitaciones')
    axs[0, 1].grid(axis='y')

    # Graficar evolución de arribos
    tiempos = range(0, tiempo_simulacion, 24)  # Asumimos datos diarios
    arribos_diarios = [random.randint(0, 10) for _ in tiempos]  # Simulación de datos
    axs[1, 0].plot(tiempos, arribos_diarios, label='Arribos Diarios', color='purple')
    axs[1, 0].set_xlabel('Tiempo (horas)')
    axs[1, 0].set_ylabel('Número de Arribos')
    axs[1, 0].set_title('Evolución de Arribos')
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # Graficar porcentaje de reservas rechazadas y bonificaciones
    axs[1, 1].bar(['Rechazadas', 'Bonificadas'], [
        (reservas_rechazadas / total_arribos) * 100 if total_arribos > 0 else 0,
        (bonificaciones / total_huespedes) * 100 if total_huespedes > 0 else 0
    ], color=['orange', 'cyan'])
    axs[1, 1].set_ylabel('Porcentaje (%)')
    axs[1, 1].set_title('Reservas Rechazadas y Bonificadas')
    axs[1, 1].grid(axis='y')

    # Graficar porcentaje de rechazos por causa del mismo
    axs[0,0].bar(['Suite','Doble','Simple','Adicionales'],[
        (rechazos_suite / reservas_rechazadas) * 100 if reservas_rechazadas > 0 else 0,
        (rechazos_doble / reservas_rechazadas) * 100 if reservas_rechazadas > 0 else 0,
        (rechazos_simple / reservas_rechazadas) * 100 if reservas_rechazadas > 0 else 0,
        (rechazos_adicionales / reservas_rechazadas) * 100 if reservas_rechazadas > 0 else 0
    ], color =['orange','cyan','green','red'])
    axs[0, 0].set_ylabel('Porcentaje (%)')
    axs[0, 0].set_title('Reservas Rechazadas segun causa')
    axs[0, 0].grid(axis='y')

    # Ajustar diseño y guardar gráfico
    plt.tight_layout()
    plt.savefig('resultados/hotel_simulation_results.png')
    print("\nResultados trazados y guardados en 'resultados/hotel_simulation_results.png'")
    plt.show()