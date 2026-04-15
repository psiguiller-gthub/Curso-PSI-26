
class Usuario:
    """
    clase de datos de usuario
    solo contiene id_usario
    """

    def __init__(self, id: int):
        """
            Args:
                id (int): ID del usuario
        """
        self.id = id


    def recibir_notificacion_cierre_ticket(self, mensaje: str):
        """
            simula que se ha enviado una notificacion al usuario
            EJ: Notificado usuario x, mensaje parametro mensaje
            Args:
                mensaje (str): str: mensaje a mostrar
        """
        print(f"Notificado usuario {self.id}, mensaje: {mensaje}")
        