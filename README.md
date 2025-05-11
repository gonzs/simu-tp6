# Simulación de Hotel (HotelSys)

## 📚 Descripción del Proyecto
Este proyecto simula las llegadas de huéspedes a un hotel, permitiendo analizar la utilización de los diferentes tipos de habitaciones. Asi como tambien las reservas rechazadas y aquellas que por no cumplir con alguno de los requerimientos tuvo algun tipo de bonificacion. A través de eventos de llegada y salida de huéspedes, se evalúa la disponibilidad de habitaciones y recursos adicionales.

# 📑 Índice de la Estructura del Proyecto

Este documento presenta la estructura completa del proyecto de simulación de hotel, organizada jerárquicamente para facilitar la navegación y comprensión del código.

## 📂 Estructura General

```
simu-tp6/
├── main.py                      # Punto de entrada principal de la aplicación
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias del proyecto
├── Dockerfile                   # Configuración para contenedores Docker
│
├── dataset/                     # Datos para la simulación
│   └── hotel_bookings.csv       # Dataset con información de reservas hoteleras
│
├── docs/                        # Documentación técnica
│   ├── Doc Inicial TP6.docx     # Documento inicial del proyecto
│   │
│   ├── Diagrama de Flujo/       # Diagramas de flujo del sistema
│   │   ├── Flujograma_1.jpeg
│   │   ├── Flujograma_2.jpeg
│   │   ├── Flujograma_3.jpeg
│   │   ├── Flujograma_4.jpeg
│   │   └── Flujograma_5.jpeg
│   │
│   └── FDPS/                    # Documentación de funciones de distribución de probabilidad
│       ├── FDPs.docx
│       ├── Grafico Duracion_Estadia.png
│       ├── Grafico Intervalo_Entre_Arribos.png
│       ├── Probabilidad_Cantidad_Bebes.png
│       ├── Probabilidad_Cantidad_Niños.png
│       ├── Probabilidad_Tipo_Habitacion.png
│       └── TP6.ipynb            # Notebook con análisis de datos
│
├── resultados/                  # Resultados generados por la simulación
│   ├── hotel_simulation_results.png  # Gráfico con resultados de la simulación
│   └── resultados_simulacion.csv     # Archivo CSV con resultados de múltiples simulaciones
│
└── src/                         # Código fuente del proyecto
    ├── config/                  # Configuración de la simulación
    │   ├── __init__.py
    │   └── config.py            # Parámetros de la simulación (tipos habitación, recursos, etc.)
    │
    ├── eventos/                 # Lógica de eventos de la simulación
    │   ├── __init__.py
    │   └── llegada_huesped.py   # Manejo de llegadas de huéspedes
    │
    ├── fdp/                     # Funciones de distribución de probabilidad
    │   ├── __init__.py
    │   ├── duracion_estadia.py  # Generación de duración de estadía
    │   ├── intervalo_entre_arribos.py  # Intervalos entre arribos de huéspedes
    │   ├── num_bebes.py         # Generación de cantidad de bebés
    │   ├── num_ninios.py        # Generación de cantidad de niños
    │   └── tipo_habitacion.py   # Selección de tipo de habitación
    │
    └── utils/                   # Utilidades y herramientas
        ├── __init__.py
        ├── calculos.py          # Funciones de cálculo y resultados
        ├── disponibilidades.py  # Gestión de disponibilidad de habitaciones
        ├── graficos.py          # Generación de gráficos
        └── reserva.py           # Gestión de reservas
```

## 🔍 Descripción de los Principales Componentes

### 📌 Código Fuente (`src/`)

#### Configuración (`config/`)
- `config.py`: Define parámetros de simulación como cantidad de habitaciones, recursos adicionales y duración.

#### Eventos (`eventos/`)
- `llegada_huesped.py`: Implementa la lógica para el arribo de huéspedes al hotel.

#### Funciones de Distribución de Probabilidad (`fdp/`)
- `duracion_estadia.py`: Genera la duración de estadía de los huéspedes usando distribución Weibull.
- `intervalo_entre_arribos.py`: Calcula el tiempo entre llegadas sucesivas de huéspedes.
- `num_bebes.py` y `num_ninios.py`: Generan la cantidad de bebés y niños por reserva.
- `tipo_habitacion.py`: Determina el tipo de habitación solicitada por los huéspedes.

#### Utilidades (`utils/`)
- `calculos.py`: Contiene funciones para el cálculo de métricas y salida de resultados.
- `disponibilidades.py`: Gestiona la disponibilidad de habitaciones y recursos.
- `graficos.py`: Genera visualizaciones de los resultados de la simulación.
- `reserva.py`: Maneja la lógica de reservas de habitaciones.

### 📊 Resultados (`resultados/`)
- `hotel_simulation_results.png`: Gráfico visual con los resultados de la simulación.
- `resultados_simulacion.csv`: Registro de múltiples simulaciones para análisis comparativo.

### 📚 Documentación (`docs/`)
- Diagramas de flujo que ilustran el funcionamiento del sistema.
- Documentación sobre las funciones de distribución de probabilidad utilizadas.
- Notebook con análisis exploratorio de datos.

## 💡 Guía Rápida

1. El punto de entrada es `main.py`
2. La configuración principal está en `src/config/config.py`
3. Los resultados se almacenan en el directorio `resultados/`
4. La documentación se encuentra en `docs/`
5. Para ejecutar la aplicacion revisar el [RUNBOOK.md](RUNBOOK.md) para ver los pasos a seguir.
