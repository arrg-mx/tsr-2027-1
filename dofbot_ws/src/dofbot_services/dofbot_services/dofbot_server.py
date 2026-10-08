#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from dofbot_interfaces.srv import GetStatus


class DofbotSrcSrv(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
    # creacion del servidor
        self.__status_server = self.create_service(
            GetStatus,
            'dofbot_status_srv',
            self._on_status_srv_rqt
        )
        self.get_logger().info(f"'{node_name}' inicializado, status_srv listo.")

    def _on_status_srv_rqt(self, request:GetStatus.Request, response:GetStatus.Response):
        self.get_logger().info("Recibi una petición...")
        # Tratamiento / procesamiento de la peticion
        is_active = request.is_robot_active
        # TODO: Cualquier proceso que se requiera
        robot_checkup_proc = not is_active

        # Preparación de la respuesta del servicio
        response.is_active = robot_checkup_proc
        response.success = True
        response.string_status_message = "Todo OK"

        return response


def init_node(args=None):
    rclpy.init(args=args)
    srv_node = DofbotSrcSrv('dofbot_server_node')
    rclpy.spin(srv_node)
    rclpy.shutdown()

if __name__ == "__main__":
    init_node()
