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
- `resultados/`: Directorio donde se almacenan los resultados
- `.devcontainer/`: Configuración del contenedor de desarrollo

## 📊 Resultados de la Simulación
Los resultados de la simulación se almacenan en el directorio `resultados/`. Se generan reportes y gráficos que permiten analizar la utilización de recursos y el desempeño del hotel.
