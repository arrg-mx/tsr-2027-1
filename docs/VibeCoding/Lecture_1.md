# VibeCoding - Lección 1

| Campo | Valor |
|---|---|
| Fecha de la sesión | `[completar]` |
| Entorno | Ubuntu 24.04, ROS 2 Jazzy Jalisco |
| Asistentes | Google AI Assistant (Gemma4) y ChatGPT (ChatGPT6) |
| Tipo de acceso | `[completar]` |
| Prompts comparados | 2 |
| Tipo de comparación | Cualitativa |

## Introducción

Este documento registra la primera sesión de **VibeCoding** del curso **Temas Selectos de Robótica (TSR) 2027-I**. La práctica tiene como propósito evidenciar, con evidencia directa, que dos modelos de lenguaje distintos pueden producir respuestas diferentes ante un mismo *prompt*, aunque ambos reciban exactamente la misma instrucción.

### Objetivo

Comparar de forma cualitativa las respuestas de dos asistentes de IA aplicados a la programación en Python para ROS 2 Jazzy, identificando diferencias en precisión técnica, completitud, claridad, supuestos implícitos y valor agregado.

### Modelos comparados

| Asistente | Modelo | Enfoque observado |
|---|---|---|
| Google AI Assistant | Gemma4 | Detalle en `rclpy` y preguntas de aclaración. |
| ChatGPT | ChatGPT6 | Visión amplia de robótica y pasos de verificación. |

> Los nombres y versiones corresponden a las etiquetas mostradas por cada plataforma durante la práctica; pueden cambiar con el tiempo.

### Metodología

1. Se definió un *prompt* por práctica.
2. El mismo texto se envió sin modificaciones a ambos asistentes.
3. Las respuestas se transcribieron conservando su contenido original.
4. Se compararon con los criterios descritos a continuación.

> Las respuestas se presentan con un formato uniforme para facilitar la lectura y la comparación; no se modificó su contenido técnico.

### Criterios de comparación

- **Correctitud técnica:** validez del código, las interfaces y la configuración ROS 2.
- **Completitud:** cobertura de todos los requisitos solicitados.
- **Claridad:** organización, estructura y legibilidad.
- **Supuestos:** decisiones tomadas sin información suficiente y riesgos asociados.
- **Valor agregado:** explicaciones, advertencias, pasos de compilación y verificación.
- **Reconocimiento de incertidumbre:** cómo maneja el modelo lo que no sabe o no puede verificar.

### Contexto técnico

- **Entorno de referencia:** Ubuntu 24.04 con ROS 2 Jazzy Jalisco.
- **Lenguaje:** Python 3 con `rclpy`.
- **Paquete existente:** `dofbot_telemetry`.
- **Origen de datos:** `SysReport`, función `statdistics_snapshot()` (según el enunciado del *prompt*).

### Estructura del documento

Cada práctica presenta el *prompt* utilizado, las respuestas de ambos modelos y un análisis comparativo. La **Práctica 1** funciona como prueba inicial de reconocimiento; la **Práctica 2** plantea una tarea técnica compleja y es la que mejor expone las diferencias entre los modelos.

## Práctica 1

_**Propósito del prompt:**_ verificar la disposición y el enfoque general de cada modelo ante una instrucción mínima de reconocimiento.

_**Prompt:**_

```text
Asiste en programación de Python para ROS2 Jazzy, confirma
```

_**Respuestas:**_

### Respuesta de Google AI Assistant (Gemma4)

Confirmado, estoy listo para asistirte en programación de Python para ROS 2 Jazzy Jalisco. Puedo ayudarte desde la creación de paquetes y nodos básicos con `rclpy` hasta el manejo de parámetros, servicios, acciones y archivos launch en Python.

**Capacidades de soporte en ROS 2 Jazzy**

- **Estructura y paquetes.** Creación y configuración de paquetes `ament_python` (`package.xml`, `setup.py`, `setup.cfg`) y resolución de dependencias con `rosdep`.
- **Comunicación entre nodos.** Implementación de publicadores, suscriptores, servicios, clientes y servidores de acciones utilizando `rclpy` y perfiles QoS.
- **Nodos avanzados.** Uso de temporizadores, grupos de callbacks (`MutuallyExclusiveCallbackGroup`, `ReentrantCallbackGroup`), ejecutores multihilo y gestión dinámica de parámetros.
- **Orquestación y depuración.** Escritura de archivos de lanzamiento en Python (`.launch.py`), inspección de tópicos, pruebas unitarias con `pytest` y resolución de errores de compilación con `colcon`.

**Para comenzar a trabajar en tu proyecto, cuéntame:**

- ¿Qué funcionalidad o tipo de nodo necesitas desarrollar?
- ¿Qué mensajes o interfaces (estándar o personalizados) vas a utilizar?
- ¿Tienes algún código inicial o mensaje de error que quieras revisar?

Con estos detalles puedo escribir el código listo para probar o ayudarte a depurar tu paquete.

### Respuesta de ChatGPT (ChatGPT6)

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

ROS 2 Jazzy + Python (`rclpy`)

Trabajaremos con código compatible con ROS 2 Jazzy, explicaciones técnicas y soluciones reproducibles en Ubuntu 24.04.

Puedes compartir tu código, problema técnico o requerimiento de desarrollo. Estoy listo.

_**Análisis comparativo:**_

| Criterio | Google AI Assistant (Gemma4) | ChatGPT (ChatGPT6) |
|---|---|---|
| Enfoque | Asistencia centrada en programación Python/ROS 2 con `rclpy`. | Asistencia como especialista en Python para ROS 2, con visión amplia de robótica. |
| Alcance técnico | Paquetes `ament_python`, publicadores/suscriptores, servicios, acciones, QoS, temporizadores, grupos de callbacks, ejecutores, parámetros, launch, `pytest` y `colcon`. | Nodos, topics, services/actions, TF2, sensores y actuadores, URDF, Gazebo, Nav2, SLAM, launch y debugging. |
| Preguntas de aclaración | Formula tres preguntas: funcionalidad o tipo de nodo, interfaces y código o error inicial. | No formula preguntas; invita a compartir código, problema o requerimiento. |
| Claridad y estilo | Respuesta estructurada en capacidades y viñetas, con lenguaje técnico y conciso. | Respuesta directa con lista de áreas y frases breves; menos detalle en `rclpy`. |
| Extensión | Media. | Media. |

**Conclusión de la práctica:** Ambos modelos confirman la instrucción, pero con enfoques distintos. Gemma4 se concentra en las capacidades concretas de `rclpy` y solicita contexto antes de trabajar; ChatGPT6 amplía el alcance hacia el ecosistema de robótica y no hace preguntas. El prompt es demasiado general para evaluar precisión técnica, por lo que esta práctica funciona como calibración de estilo.

---

## Práctica 2

_**Propósito del prompt:**_ evaluar la capacidad de ambos modelos para generar una solución ROS 2 completa y correcta a partir de una especificación con datos de entrada y un paquete existente.

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

_**Respuestas:**_

### Respuesta de Google AI Assistant (Gemma4)

Aquí tienes la solución completa para integrar la telemetría en tu paquete `dofbot_telemetry` bajo ROS 2 Jazzy.

Dado que los mensajes personalizados en ROS 2 requieren compilación en CMake (`ament_cmake`), si tu paquete `dofbot_telemetry` es únicamente de Python (`ament_python`), la práctica estándar en ROS 2 es crear un paquete dedicado para las interfaces (por ejemplo, `dofbot_telemetry_interfaces`) o configurar el paquete actual para soportar ambos lenguajes. A continuación te muestro la definición del mensaje y el script en Python listos para usar.

**1. Definición del mensaje (`RobotTelem.msg`)**

Crea la carpeta `msg` dentro de tu paquete de interfaces (o en `dofbot_telemetry/msg/` si usas compilación híbrida) y guarda este archivo como `RobotTelem.msg`.

```text
float64 cpu
string time
float64 ram_available
float64 ram_total
float64 disk_available
float64 disk_total
string ip
```

Nota sobre configuración: asegúrate de declarar `rosidl_generate_interfaces` en tu `CMakeLists.txt` y agregar `<exec_depend>rosidl_default_runtime</exec_depend>` junto con `<member_of_group>rosidl_interface_packages</member_of_group>` en el `package.xml` correspondiente.

**2. Script del nodo (`robot_telemetry.py`)**

Guarda este código en `dofbot_telemetry/dofbot_telemetry/robot_telemetry.py`. El nodo ejecuta la lectura y publicación cada 2.0 segundos (coincidiendo con el intervalo de tus muestras).

```python
import rclpy
from rclpy.node import Node

# Ajusta el nombre del paquete si decides alojar el .msg en un paquete de interfaces separado
from dofbot_telemetry.msg import RobotTelem

# Importación de la función desde tu librería SysReport
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

**3. Detalles clave de la implementación**

- **Prevención de colisión de nombres.** Como el mensaje (`RobotTelem.msg`) y la clase del nodo (`RobotTelem`) comparten exactamente el mismo nombre, se define internamente `RobotTelemNode` y se asigna el alias `RobotTelem` después de instanciar el publicador para evitar conflictos de referencia en Python.
- **Registro en `setup.py`.** Agrega el punto de entrada en `console_scripts` dentro de tu `setup.py` para ejecutarlo con `ros2 run`:

```python
'telemetry = dofbot_telemetry.robot_telemetry:main',
```

- **Conversión explícita de tipos.** Se aplican `float()` y `str()` a cada campo antes de asignarlo al mensaje para evitar excepciones de tipo estricto propias de `rclpy` en ROS 2 Jazzy.

Si necesitas ayuda para terminar de integrar esto en tu workspace, dime:

- ¿Tu paquete `dofbot_telemetry` es actualmente `ament_python` o `ament_cmake`?
- ¿Cómo se importa exactamente `SysReport` en tu entorno (instalado por pip o archivo local)?

Con eso puedo darte los archivos `CMakeLists.txt`, `package.xml` y `setup.py` listos para compilar con `colcon build`.

### Respuesta de ChatGPT (ChatGPT6)

Para el paquete existente `dofbot_telemetry` en ROS 2 Jazzy, propongo implementar el nodo `telemetry` utilizando `rclpy` y un mensaje personalizado `RobotTelem.msg`.

La solución contempla:

- Una clase `RobotTelem` que hereda de `Node`.
- Un nodo ROS 2 con nombre `telemetry`.
- Un publisher que publica las estadísticas del sistema.
- Un timer para tomar muestras periódicamente de `SysReport`.
- Un mensaje personalizado con CPU, RAM, disco, hora e IP.
- La conversión de los diccionarios anidados de `statdistics_snapshot()` a campos del mensaje ROS.

**Importante:** los valores de RAM y disco disponibles y totales se representarán como `float32`. El campo `time` será un `string` e `ip` también será `string`.

**1. Archivo `msg/RobotTelem.msg`**

Mensaje personalizado ROS 2.

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

**2. Script `robot_telemetry.py`**

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

**Nota sobre SysReport:** he asumido que la librería se instancia con `SysReport()` y que `statdistics_snapshot()` es un método de instancia. Si la función es estática o el nombre del módulo es diferente, habrá que ajustar la importación y la llamada.

**3. Configuración de `CMakeLists.txt`**

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

**4. Configuración de `package.xml`**

Asegúrate de incluir estas dependencias en el archivo `package.xml`:

```xml
<buildtool_depend>ament_cmake</buildtool_depend>

<buildtool_depend>rosidl_default_generators</buildtool_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<exec_depend>rclpy</exec_depend>

<exec_depend>python3-sysreport</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

`python3-sysreport` es un nombre de dependencia ilustrativo: utiliza el nombre real del paquete que proporciona `SysReport` en tu entorno.

**5. Compilación y ejecución**

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

**6. Verificación de la publicación**

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

Frecuencia esperada: 0.5 Hz.

Esto corresponde a una publicación cada dos segundos.

Como siguiente paso, puedo ayudarte a integrar el nodo con el `CMakeLists.txt` y `package.xml` reales de tu paquete `dofbot_telemetry`, evitando conflictos con su configuración actual.

_**Análisis comparativo:**_

| Criterio | Google AI Assistant (Gemma4) | ChatGPT (ChatGPT6) |
|---|---|---|
| Correctitud técnica | Advierte la incompatibilidad entre `ament_python` y los mensajes personalizados; sin embargo, `main()` instancia `RobotTelem()` (la clase del mensaje) en lugar del nodo, por lo que el script falla tal como está. | El código del nodo es coherente, pero asume que `dofbot_telemetry` es `ament_cmake`, cuando el paquete existente es `ament_python`; la configuración propuesta no aplica directamente. |
| Completitud | Cubre mensaje, nodo y notas de integración, pero no entrega `setup.py`, `package.xml` ni `CMakeLists.txt` completos; deja preguntas abiertas. | Cubre mensaje, nodo, `CMakeLists.txt`, `package.xml`, compilación, ejecución y verificación; es la respuesta más completa. |
| Claridad | Estructura numerada y explicaciones útiles, aunque el formato del código está fragmentado y mezcla texto con bloques. | Estructura clara por pasos, con bloques de código bien delimitados y comandos de verificación. |
| Supuestos | Asume que el mensaje debe vivir en el paquete o en un paquete de interfaces nuevo; no verifica la librería `SysReport`. | Asume `ament_cmake`, una clase `SysReport` instanciable y un módulo `sysreport`; no verifica el repositorio. |
| Valor agregado | Preguntas de aclaración y advertencia sobre el tipo de paquete. | Pasos de compilación, ejecución, `ros2 topic echo` y `ros2 topic hz`. |
| Reconocimiento de incertidumbre | Reconoce la ambigüedad del tipo de paquete y pregunta. | Reconoce la suposición sobre `SysReport` en una nota, pero no la del tipo de paquete. |

**Hallazgos clave:**

- Ninguno de los dos modelos usa el paquete `dofbot_interfaces` ni el mensaje `SnapShot.msg` que ya existen en el repositorio.
- Ambos aceptan sin cuestionar la premisa de `SysReport.statdistics_snapshot`; en el repositorio, la función equivalente es `arrg_utils.SysInfo.get_system_snapshot`.
- Gemma4 identifica el conflicto entre `ament_python` y `ament_cmake`, pero su ejemplo no se ejecuta tal como está.
- ChatGPT6 ofrece la respuesta más accionable, pero su configuración parte de una premisa falsa sobre el tipo de paquete.

**Conclusión de la práctica:** Para esta tarea, Gemma4 demuestra mejor criterio al detectar el problema estructural, mientras que ChatGPT6 ofrece mayor completitud y verificabilidad. Ninguna de las dos respuestas es directamente ejecutable sin adaptar el contexto real del repositorio.

---

## Conclusiones

- **Estilo y enfoque.** Gemma4 prioriza el detalle técnico de `rclpy` y formula preguntas de aclaración; ChatGPT6 ofrece una visión más amplia de robótica y soluciones completas con pasos de verificación.
- **Completitud frente a precisión.** ChatGPT6 tiende a entregar respuestas más extensas y accionables; Gemma4 suele ser más cauteloso y detecta mejor los supuestos estructurales.
- **Supuestos implícitos.** Ambos modelos aceptaron sin cuestionar premisas del *prompt*, como la existencia de `SysReport.statdistics_snapshot` y la ubicación del mensaje personalizado.
- **Verificación necesaria.** Las respuestas generadas deben contrastarse con el repositorio: `dofbot_telemetry` es `ament_python`, ya depende de `dofbot_interfaces` y esta interfaz ya define `SnapShot.msg`.
- **Calidad del prompt.** Un *prompt* con el contexto del paquete, las interfaces existentes y la librería real habría reducido la ambigüedad y mejorado la utilidad de ambas respuestas.
- **Conclusión general.** La comparación evidencia que no existe un modelo universalmente mejor: la elección depende de si se prioriza cautela y preguntas de aclaración (Gemma4) o completitud y pasos reproducibles (ChatGPT6).
