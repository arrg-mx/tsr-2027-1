#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult

class ParamSrv(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        # Para declara un solo parametro
        self.declare_parameter(
            name='time_period',
            value=0.01,
            descriptor=ParameterDescriptor(description="telemetry sampling time in sec.")
        )
        # Para declara varios parametros
        self.declare_parameters(
            namespace='',
            parameters=[
                ('vel_lin', 0.1),
                ('vel_ang', 0.25),
                ('joint_names', rclpy.Parameter.Type.STRING_ARRAY),
                ('joint_values', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('ip_address', rclpy.Parameter.Type.STRING),
                ('robot_name', rclpy.Parameter.Type.STRING)
            ]
        )
        # Para obtener el valor de un parametro 
        self._time_period = self.get_parameter('time_period').get_parameter_value().double_value
        # Para ageragr una funcion de validacion
        self.add_on_set_parameters_callback(self._on_parameters_change)

        self.get_logger().info(f"Parameter Server [{node_name}] initialized. time period = {self._time_period}")

    def _on_parameters_change(self, params:list[Parameter]):
        success = True
        # Para validar el valor(es) deseado necesitamos recorrer 
        # toda la lista de parameters
        for param in params:
            if param.name == 'time_period':
                if param.value < 0.0 or param.value > 10.0: 
                    self.get_logger().warn(f"Parameter {param.name} debe ser mayor a cero y menor a 10.0.")
                    success = False
            # TODO: Aqui van las demás validaciones en caso de ser necesarias 

        result_msg = SetParametersResult()
        result_msg.successful = success
        result_msg.reason = "Proceso exitos" if success else "Error en la validacion"

        return result_msg

def init_node(args=None):
    rclpy.init(args=args)
    param_srv_node = ParamSrv('param_srv')
    try:
        rclpy.spin(param_srv_node)
    except KeyboardInterrupt:
        param_srv_node.get_logger().warn("keybord interrupt (SIGITN) received. Shutting down...")
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    init_node()