from src.fdp import HotelFDP
from src.utils import HotelUtils

def llegada_huesped(self):
        """Tratar un evento de llegada de huésped"""
        # Generar parámetros del huésped
        duracion_estadia = HotelFDP.generar_duracion_estadia()
        tipo_habitacion = HotelFDP.generar_tipo_habitacion()
        num_ninios = HotelFDP.generar_num_ninios()
        num_bebes = HotelFDP.generar_num_bebes()

        self.total_arribos += 1

        # Calcular tiempo de finalización de la estadía
        fecha_fin = self.tiempo_actual + duracion_estadia
        
        # Intentar encontrar una habitación disponible
        id_habitacion = HotelUtils.encontrar_habitacion_disponible(
            tipo_habitacion, self.tiempo_actual, self.habitaciones_simples, self.habitaciones_dobles, self.habitaciones_suites
        )

        if id_habitacion is not None:
            # Chequear si las cunas necesarias están disponibles
            cunas_necesarias = min(num_bebes, 2)
            id_cunas = None
            if cunas_necesarias > 0:
                id_cunas = HotelUtils.encontrar_cunas_disponibles(self.cunas, cunas_necesarias, self.tiempo_actual)

            # Chequear si las camas necesarias están disponibles
            camas_necesarias = min(num_ninios, 2) 
            id_camas = None
            if camas_necesarias > 0:
                id_camas = HotelUtils.encontrar_camas_disponibles(self.camas_simples, camas_necesarias, self.tiempo_actual)

            # Allocate room
            if tipo_habitacion == "simple":
                HotelUtils.asignar_reserva(self.habitaciones_simples[id_habitacion], fecha_fin, self.tiempo_actual, self.total_huespedes)
            elif tipo_habitacion == "doble":
                 HotelUtils.asignar_reserva(self.habitaciones_dobles[id_habitacion], fecha_fin, self.tiempo_actual, self.total_huespedes)
            elif tipo_habitacion == "suite":
                HotelUtils.asignar_reserva(self.habitaciones_suites[id_habitacion], fecha_fin, self.tiempo_actual, self.total_huespedes)

            # Si todos los recursos están disponibles
            # (camas y cunas) se asignan a la habitación
            # Si no hay cunas o camas necesarias, se asignan
            # las que están disponibles
            if (cunas_necesarias == 0 or id_cunas) and (camas_necesarias == 0 or id_camas):
                # Asignar cunas si es necesario
                if id_cunas:
                    for id_cuna in id_cunas:
                        self.cunas[id_cuna]["comprometida_hasta"] = fecha_fin

                # Asignar camas si es necesario
                if id_camas:
                    for id_cama in id_camas:
                        self.camas_simples[id_cama]["comprometida_hasta"] = fecha_fin

                return True
            else:
                # Si no estan disponibles todos los recursos adicionales
                # se aplica una bonificación
                self.bonificaciones += 1
                return False
        else:
            # Si no hay habitación disponible, se rechaza la reserva
            self.reservas_rechazadas += 1
            
            # Registrar el tipo de habitación rechazada
            if tipo_habitacion == "simple":
                self.reservas_rechazadas_simples += 1
            elif tipo_habitacion == "doble":
                self.reservas_rechazadas_dobles += 1
            elif tipo_habitacion == "suite":
                self.reservas_rechazadas_suites += 1
                
            return False