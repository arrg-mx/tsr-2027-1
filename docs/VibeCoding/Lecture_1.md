# VibeCoding - Lecture 1

## Introduction

## Practice 1

_**Prompt:**_

```text
Asiste en programación de Python para ROS2 Jazzy, confirma
```

_**Answers:**_

**Google AI Assistant**
**Model:** Gemma4

> Confirmado, estoy listo para asistirte en programación de Python para ROS 2 Jazzy Jalisco. Puedo ayudarte desde la creación de paquetes y nodos básicos con rclpy hasta el manejo de parámetros, servicios, acciones y archivos launch en Python.
>
> Capacidades de soporte en ROS 2 Jazzy
>
> • Estructura y paquetes. Creación y configuración de paquetes ament_python (package.xml, setup.py, setup.cfg) y resolución de dependencias con rosdep.
> • Comunicación entre nodos. Implementación de publicadores, suscriptores, servicios, clientes y servidores de acciones utilizando rclpy y perfiles QoS.
> • Nodos avanzados. Uso de temporizadores, grupos de callbacks (MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup), ejecutores multihilo y gestión dinámica de parámetros.
> • Orquestación y depuración. Escritura de archivos de lanzamiento en Python (.launch.py), inspección de tópicos, pruebas unitarias con pytest y resolución de errores de compilación con colcon.
>
> Para comenzar a trabajar en tu proyecto, cuéntame:
>
> • ¿Qué funcionalidad o tipo de nodo necesitas desarrollar?
> • ¿Qué mensajes o interfaces (estándar o personalizados) vas a utilizar?
> • ¿Tienes algún código inicial o mensaje de error que quieras revisar?
> Con estos detalles puedo escribir el código listo para probar o ayudarte a depurar tu paquete.

**ChatGPT**
**Model:** ChatGPT6

¡Confirmado! Puedo asistirte como especialista en programación de **Python para ROS 2 Jazzy Jalisco**.

Te apoyaré en:

- **Nodos ROS 2:** creación, ejecución y depuración con `rclpy`.
- **Topics:** publicación y suscripción (`Publisher`, `Subscriber`).
- **Services y Actions:** comunicación síncrona y asíncrona.
- **TF2:** transformaciones entre sistemas de coordenadas.
- **Robótica:** integración con sensores, actuadores y control de movimiento.
- **URDF y Gazebo:** simulación e integración de robots.
- **Nav2 y SLAM:** navegación autónoma y mapeo.
- **Launch files:** automatización de despliegues.
- **Debugging:** análisis de errores y optimización de código.

ROS 2 Jazzy + Python (rclpy)

Trabajaremos con código compatible con ROS 2 Jazzy, explicaciones técnicas y soluciones reproducibles en Ubuntu 24.04.

Puedes compartir tu código, problema técnico o requerimiento de desarrollo. Estoy listo.

---

_**Prompt:**_

````
El siguiente texto corresponde a varias líneas de la salida de la función statdistics_snapshot de la librería de SysReport escrita en Python:

```text
{'cpu': 3.88094, 'time': '13:46:28', 'ram': {'available': 2.5, 'total': 3.9}, 'disk': {'available': 34.0, 'total': 59.0}, 'ip': '172.16.8.136'}
{'cpu': 3.88073, 'time': '13:46:30', 'ram': {'available': 2.5, 'total': 3.9}, 'disk': {'available': 34.0, 'total': 59.0}, 'ip': '172.16.8.136'}
{'cpu': 3.87962, 'time': '13:46:32', 'ram': {'available': 2.5, 'total': 3.9}, 'disk': {'available': 34.0, 'total': 59.0}, 'ip': '172.16.8.136'}
{'cpu': 3.87831, 'time': '13:46:34', 'ram': {'available': 2.5, 'total': 3.9}, 'disk': {'available': 34.0, 'total': 59.0}, 'ip': '172.16.8.136'}
{'cpu': 3.87683, 'time': '13:46:36', 'ram': {'available': 2.5, 'total': 3.9}, 'disk': {'available': 34.0, 'total': 59.0}, 'ip': '172.16.8.136'}
```
El formato de cada linea esta compuesto por:
- 'cpu',  Tipo flotante,
- 'time', cadena de tiempo con la hora que se registro en el momento
- 'ram', contiene 'available': ram disponible, tipo flotante, 'total': ram total tipo flotante
- 'disk', contiene 'available': espaio disponible tipo flotante, 'total': espacio disponible tipo flotante
- 'ip', cadena que representa la dirección ip
Meta: Escribe un nuevo script llamado robot_telemetry.py con las siguientyes características:
- Debe contener una clase llamada RobotTelem que genere un nodo de ROS llamado 'telemetry' y publique el resultado de la función statdistics_snapshot
- Crea un mensaje personalizado llamado RobotTelem.msg con las variables de la función
- El paquete de ROS2 ya existe y se llama dofbot_telemetry
````

_**Answers:**_

**Google AI Assistant**
**Model:** Gemma4

Aquí tienes la solución completa para integrar la telemetría en tu paquete dofbot_telemetry bajo ROS 2 Jazzy.
Dado que los mensajes personalizados en ROS 2 requieren compilación en CMake (ament_cmake), si tu paquete dofbot_telemetry es únicamente de Python (ament_python), la práctica estándar en ROS 2 es crear un paquete dedicado para las interfaces (por ejemplo, dofbot_telemetry_interfaces) o configurar el paquete actual para soportar ambos lenguajes. A continuación te muestro la definición del mensaje y el script en Python listos para usar.

1. Definición del mensaje (RobotTelem.msg)

Crea la carpeta msg dentro de tu paquete de interfaces (o en dofbot_telemetry/msg/ si usas compilación híbrida) y guarda este archivo como RobotTelem.msg.

```text
float64 cpu
string time
float64 ram_available
float64 ram_total
float64 disk_available
float64 disk_total
string ip
```

Usa el código con precaución.
Nota sobre configuración: Asegúrate de declarar `rosidl_generate_interfaces` en tu `CMakeLists.txt` y agregar `<exec_depend>rosidl_default_runtime</exec_depend>` junto con `<member_of_group>rosidl_interface_packages</member_of_group>` en el `package.xml` correspondiente.

2. Script del nodo (robot_telemetry.py)

Guarda este código en `dofbot_telemetry/dofbot_telemetry/robot_telemetry.py`. El nodo ejecuta la lectura y publicación cada 2.0 segundos (coincidiendo con el intervalo de tus muestras).
python
import rclpy
from rclpy.node import Node

### Ajusta el nombre del paquete si decides alojar el .msg en un paquete de interfaces separado

`from dofbot_telemetry.msg import RobotTelem`

### Importación de la función desde tu librería SysReport

```python
from SysReport import statdistics_snapshot


class RobotTelemNode(Node):
    def __init__(self):
        # El nodo se inicializa con el nombre exacto 'telemetry'
        super().__init__('telemetry')

        # Publicador en el tópico 'robot_telemetry' con cola de tamaño 10
        self.publisher_ = self.create_publisher(RobotTelem, 'robot_telemetry', 10)

        # Temporizador cada 2.0 segundos según la frecuencia de los datos de ejemplo
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Nodo telemetry iniciado. Publicando estadísticas del sistema...')

    def timer_callback(self):
        try:
            # Obtener el diccionario con la instantánea de estadísticas
            data = statdistics_snapshot()

            # Construir y rellenar el mensaje personalizado
            msg = RobotTelem()
            msg.cpu = float(data['cpu'])
            msg.time = str(data['time'])
            msg.ram_available = float(data['ram']['available'])
            msg.ram_total = float(data['ram']['total'])
            msg.disk_available = float(data['disk']['available'])
            msg.disk_total = float(data['disk']['total'])
            msg.ip = str(data['ip'])

            # Publicar el mensaje en ROS 2
            self.publisher_.publish(msg)

        except KeyError as e:
            self.get_logger().error(f'Clave faltante en statdistics_snapshot: {e}')
        except Exception as e:
            self.get_logger().error(f'Error al leer o publicar telemetría: {e}')


# Alias para cumplir estrictamente con el nombre de clase solicitado
robotTelem = RobotTelemNode


def main(args=None):
    rclpy.init(args=args)
    telemetry_node = RobotTelem()

    try:
        rclpy.spin(telemetry_node)
    except KeyboardInterrupt:
        pass
    finally:
        telemetry_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Usa el código con precaución.

3. Detalles clave de la implementación

• Prevención de colisión de nombres. Como el mensaje (RobotTelem.msg) y la clase del nodo (RobotTelem) comparten exactamente el mismo nombre, se define internamente RobotTelemNode y se asigna el alias RobotTelem después de instanciar el publicador para evitar conflictos de referencia en Python.
• Registro en setup.py. Agrega el punto de entrada en console_scripts dentro de tu setup.py para ejecutarlo con ros2 run:python
'telemetry = dofbot_telemetry.robot_telemetry:main',
Usa el código con precaución.
• Conversión explícita de tipos. Se aplican float() y str() a cada campo antes de asignarlo al mensaje para evitar excepciones de tipo estricto propias de rclpy en ROS 2 Jazzy.
Si necesitas ayuda para terminar de integrar esto en tu workspace, dime:
• ¿Tu paquete dofbot_telemetry es actualmente ament_python o ament_cmake?
• ¿Cómo se importa exactamente SysReport en tu entorno (instalado por pip o archivo local)?
Con eso puedo darte los archivos CMakeLists.txt, package.xml y setup.py listos para compilar con colcon build.

**ChatGPT**
**Model:** ChatGPT6

Para el paquete existente `dofbot_telemetry` en ROS 2 Jazzy, propongo implementar el nodo `telemetry` utilizando `rclpy` y un mensaje personalizado `RobotTelem.msg`.

La solución contempla:

- Una clase `RobotTelem` que hereda de `Node`.
- Un nodo ROS 2 con nombre `telemetry`.
- Un publisher que publica las estadísticas del sistema.
- Un timer para tomar muestras periódicamente de `SysReport`.
- Un mensaje personalizado con CPU, RAM, disco, hora e IP.
- La conversión de los diccionarios anidados de `statdistics_snapshot()` a campos del mensaje ROS.

**Importante:** Los valores de RAM y disco disponibles y totales se representarán como `float32`. El campo `time` será un `string` e `ip` también será `string`.

### **1. Archivo&#x20;**`msg/RobotTelem.msg`

Mensaje personalizado ROS 2

Crea el directorio `msg` en la raíz del paquete `dofbot_telemetry` y dentro el archivo `RobotTelem.msg`.

```text
float32 cpu
string time

float32 ram_available
float32 ram_total

float32 disk_available
float32 disk_total

string ip
```

La estructura del mensaje queda aplanada, lo cual facilita su uso en ROS 2 y evita complicaciones con diccionarios anidados.

## **2. Script&#x20;**`robot_telemetry.py`

Ubicación propuesta:

`dofbot_telemetry/scripts/robot_telemetry.py`

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Mensaje personalizado del paquete
from dofbot_telemetry.msg import RobotTelem as RobotTelemMsg

# Librería SysReport
# Ajustar esta importación a la estructura real de la librería.
from sysreport import SysReport


class RobotTelem(Node):

    def __init__(self):
        super().__init__('telemetry')

        # Publisher ROS 2
        self.publisher_ = self.create_publisher(
            RobotTelemMsg,
            'robot_telemetry',
            10
        )

        # Instancia de SysReport
        self.sys_report = SysReport()

        # Timer de publicación cada 2 segundos
        self.timer = self.create_timer(
            2.0,
            self.publish_telemetry
        )

        self.get_logger().info(
            'Nodo telemetry iniciado correctamente'
        )

    def publish_telemetry(self):
        try:
            # Obtener estadísticas del sistema
            snapshot = self.sys_report.statdistics_snapshot()

            # Crear mensaje ROS 2
            msg = RobotTelemMsg()

            # CPU
            msg.cpu = float(snapshot['cpu'])

            # Tiempo
            msg.time = str(snapshot['time'])

            # RAM
            msg.ram_available = float(
                snapshot['ram']['available']
            )
            msg.ram_total = float(
                snapshot['ram']['total']
            )

            # Disco
            msg.disk_available = float(
                snapshot['disk']['available']
            )
            msg.disk_total = float(
                snapshot['disk']['total']
            )

            # Dirección IP
            msg.ip = str(snapshot['ip'])

            # Publicar mensaje
            self.publisher_.publish(msg)

            self.get_logger().debug(
                f'Telemetría publicada: {snapshot}'
            )

        except Exception as e:
            self.get_logger().error(
                f'Error al obtener o publicar telemetría: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = RobotTelem()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            'Interrupción del nodo telemetry'
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
```

**Nota sobre SysReport:** He asumido que la librería se instancia con `SysReport()` y que `statdistics_snapshot()` es un método de instancia. Si la función es estática o el nombre del módulo es diferente, habrá que ajustar la importación y la llamada.

### **3. Configuración de&#x20;**`CMakeLists.txt`

Asumiendo que `dofbot_telemetry` es un paquete de tipo `ament_cmake`, incorpora lo siguiente a su archivo `CMakeLists.txt`, conservando las configuraciones existentes del paquete.

```cmake
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generar mensaje personalizado
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotTelem.msg"
)

# Instalar script Python
install(
  PROGRAMS
    scripts/robot_telemetry.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
```

## **4. Configuración de&#x20;**`package.xml`

Asegúrate de incluir estas dependencias en el archivo `package.xml`:

```xml
<buildtool_depend>ament_cmake</buildtool_depend>

<buildtool_depend>rosidl_default_generators</buildtool_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<exec_depend>rclpy</exec_depend>

<exec_depend>python3-sysreport</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

`python3-sysreport` es un nombre de dependencia ilustrativo: utiliza el nombre real del paquete que proporciona SysReport en tu entorno.

## **5. Compilación y ejecución**

Desde la raíz de tu workspace:

```console
cd ~/ros2_ws

colcon build --packages-select dofbot_telemetry
```

Carga el workspace:

```console
source install/setup.bash
```

Ejecuta el nodo:

```console
ros2 run dofbot_telemetry robot_telemetry.py
```

## **6. Verificación de la publicación**

Comprueba que el mensaje se haya generado:

```console
ros2 interface show dofbot_telemetry/msg/RobotTelem
```

Comprueba el tópico:

```console
ros2 topic list
```

Salida esperada:

```console
/robot_telemetry
```

Visualiza los mensajes publicados:

```console
ros2 topic echo /robot_telemetry
```

La salida tendrá una estructura similar a esta:

```console
cpu: 3.88094
time: "13:46:28"
ram_available: 2.5
ram_total: 3.9
disk_available: 34.0
disk_total: 59.0
ip: "172.16.8.136"
```

Y la frecuencia de publicación puede comprobarse con:

```console
ros2 topic hz /robot_telemetry
```

Frecuencia esperada: 0.5 Hz

Esto corresponde a una publicación cada dos segundos.

Como siguiente paso, puedo ayudarte a integrar el nodo con el `CMakeLists.txt` y `package.xml` reales de tu paquete `dofbot_telemetry`, evitando conflictos con su configuración actual.

Revisar integración ROS 2 mañanaToca para configurar
