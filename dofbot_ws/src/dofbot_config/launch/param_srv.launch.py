# 1.Importar las librerias y funciones necesarias para
# crear las acciones de ros launch
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch_ros.actions import Node
# 2. Importar las librerias utilitarias 
# # en este caso, acceso a las funciones del SO
# import re # REGEX - Regular Expressions
import os # Libreria de python para acceder  las funciones del SO

# ROS2_NAMESPACE_PATTERN = re.compile(r"^[a-z0-9_]+$")

# def validate_robot_name()

# 3. Funcion para definir las acciones del nodo(s)
# y otros elementos de ROS a utilizar
def generate_launch_description():
    # Si existe la variable de entorno 'ROBOT_NAME' obtiene el nombre
    # de lo contrario coloca la palabra 'VIRTUAL'
    robot_name = os.getenv('ROBOT_NAME', 'VIRTUAL')
    robot_ip = os.getenv('IPADDR', '127.0.0.1') 
    # Nota: 127.0.0.1 es la direccion que recibe localhost

    # 4. Crear el objeto LaunchDescription
    ld = LaunchDescription()
    
    # 5. Determinamos los elementos a ejecutar
    # 5.1 Definimos un nodo y los elementos con los cuales se ejecutara
    param_srv_node = Node(
        package='dofbot_config',
        executable='param_srv',
        namespace=robot_name.lower(),
        parameters=[{
            'robot_name': robot_name.lower(),
            'ip_address': robot_ip
        }]
    )

    # 6. Agregamos todas las acciones a lanzar en el orden necesario
    ld.add_action(param_srv_node)

    # 7. Regresamos el objeto LaunchDescription con 
    # las acciones ya configuradas
    return ld


