# Simulación de Hotel

## 📚 Descripción del Proyecto
Este proyecto simula las llegadas de huéspedes a un hotel, permitiendo analizar la utilización de los diferentes tipos de habitaciones. Asi como tambien las reservas rechazadas y aquellas que por no cumplir con alguno de los requerimientos tuvo algun tipo de bonificacion. A través de eventos de llegada y salida de huéspedes, se evalúa la disponibilidad de habitaciones y recursos adicionales.

## 🚀 Instrucciones para Ejecutar

### Usando DevContainer (recomendado)

1. **Requisitos previos**:
   - [VS Code](https://code.visualstudio.com/)
   - [Docker](https://www.docker.com/products/docker-desktop)
   - Extensión [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) en VS Code

2. **Abrir el proyecto en DevContainer**:
   - Abrir VS Code
   - Abrir la carpeta del proyecto
   - Cuando se le solicite, seleccionar "Reopen in Container" o usar el comando:
     ```
     Ctrl+Shift+P → Remote-Containers: Reopen in Container
     ```

3. **Ejecutar la simulación**:
   ```bash
   python src/main.py
   ```

## 📁 Estructura de Archivos

- `src/`: Contiene el código fuente del proyecto
  - `main.py`: Punto de entrada de la aplicación
  - `config/`: Configuración del proyecto
    - `config.py`: Archivo de configuración principal
  - `eventos/`: Módulo para manejar eventos de la simulación
    - `llegada_huesped.py`: Evento de llegada de huéspedes
  - `fdp/`: Funciones de distribución de probabilidad
    - `duracion_estadia.py`: Distribución para la duración de estadías
    - `intervalo_entre_arribos.py`: Intervalos entre arribos
    - `num_bebes.py`: Número de bebés por reserva
    - `num_ninios.py`: Número de niños por reserva
    - `tipo_habitacion.py`: Selección de tipo de habitación
  - `utils/`: Utilidades para cálculos y gráficos
    - `calculos.py`: Funciones de cálculo
    - `disponibilidades.py`: Gestión de disponibilidades
    - `graficos.py`: Generación de gráficos
    - `reserva.py`: Manejo de reservas
- `resultados/`: Directorio donde se almacenan los resultados
  - `hotel_simulation_results.png`: Gráfico de resultados de la simulación
  - `resultados_simulacion.csv`: Archivo CSV con resultados de múltiples simulaciones
- `.devcontainer/`: Configuración del contenedor de desarrollo

## ⚙️ Configuración del Proyecto

El archivo `src/config/config.py` contiene la configuración principal del proyecto. Está compuesto por los siguientes elementos:

- **TIPOS_HABITACIONES**: Define los tipos de habitaciones disponibles en el hotel y su cantidad.
  ```python
  TIPOS_HABITACIONES = {
      "simple": {"cantidad": 10},
      "doble": {"cantidad": 15},
      "suite": {"cantidad": 5}
  }
  ```

- **RECURSOS_ADICIONALES**: Especifica los recursos adicionales disponibles, como cunas y camas extra.
  ```python
  RECURSOS_ADICIONALES = {
      "cunas": 8,
      "camas_extra": 10
  }
  ```

- **PARAMETROS_SIMULACION**: Contiene los parámetros generales de la simulación, como la duración y la semilla para reproducibilidad.
  ```python
  PARAMETROS_SIMULACION = {
      "duracion_simulacion": 365,  # días
      "seed": 42
  }
  ```

## 📊 Resultados de la Simulación
Los resultados de la simulación se almacenan en el directorio `resultados/`. Se generan reportes y gráficos que permiten analizar la utilización de recursos y el desempeño del hotel.

### Archivo CSV de Resultados
El archivo `resultados_simulacion.csv` almacena los resultados de todas las simulaciones ejecutadas, permitiendo comparar diferentes configuraciones y parámetros. Los resultados se guardan con el siguiente formato:

- **Estructura**: Cada fila representa una ejecución de simulación distinta, mientras que las columnas contienen las variables y métricas.
- **Variables almacenadas**:
  - Fecha y hora de la simulación
  - Variables de control (cantidad de habitaciones, cunas, camas adicionales)
  - Total de arribos
  - Porcentaje de rechazos (total y por tipo de habitación)
  - Porcentaje de bonificaciones
  - Porcentaje de tiempo ocioso de cada tipo de habitación
  
Este formato facilita el análisis y comparación de resultados en herramientas como Excel o programas de análisis estadístico.
