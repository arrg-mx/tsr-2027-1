# VibeCoding - Lección 1: Tarea

| Campo | Valor |
|---|---|
| Fecha de la sesión | `[completar]` |
| Entorno | Ubuntu 24.04, ROS 2 Jazzy Jalisco |
| Asistentes | Google AI Assistant (Gemma4) y ChatGPT (ChatGPT6) |
| Tipo de acceso | `[completar]` |
| Prompts comparados | 1 |
| Tipo de comparación | Cualitativa |

## Introducción

Esta tarea retoma el ejercicio de comparación de modelos de la **Lección 1** y lo aplica a un caso de mayor complejidad: diseñar e integrar un servicio de ROS 2 y su interfaz `.srv` en dos paquetes existentes del repositorio.

### Propósito

Evidenciar cómo dos modelos de lenguaje responden a un mismo *prompt* técnico cuando la tarea exige coordinar un paquete `ament_python` (`dofbot_services`) con un paquete `ament_cmake` de interfaces (`dofbot_interfaces`).

### Objetivo

Comparar las respuestas de Google AI Assistant (Gemma4) y ChatGPT (ChatGPT6) ante el mismo *prompt*, identificando diferencias en precisión técnica, completitud, claridad, supuestos implícitos y valor agregado.

### Material de partida

- `reporte_demo.json`: salida de `arrg_utils.SysInfo.get_system_report()`.
- `dofbot_services`: paquete `ament_python` con ejemplos de servidor y cliente.
- `dofbot_interfaces`: paquete `ament_cmake` que ya define `srv/GetStatus.srv`.

### Metodología

1. Copiar el prompt de la sección **Prompt de la tarea** sin modificarlo.
2. Enviarlo al mismo par de asistentes: Google AI Assistant (Gemma4) y ChatGPT (ChatGPT6).
3. Registrar las respuestas completas en las secciones correspondientes.
4. Analizarlas con los criterios de comparación y responder las preguntas guía.
5. Redactar las conclusiones.

> Es importante conservar el prompt intacto y registrar las respuestas sin editar su contenido técnico, para que la comparación sea válida.

### Criterios de comparación

- **Correctitud técnica:** validez del código, de la interfaz `.srv` y de la configuración de ambos paquetes.
- **Completitud:** cobertura de todos los requisitos del prompt.
- **Claridad:** organización, estructura y legibilidad.
- **Supuestos:** decisiones tomadas sin información suficiente y riesgos asociados.
- **Valor agregado:** explicaciones, advertencias, pasos de compilación y verificación.
- **Reconocimiento de incertidumbre:** cómo maneja el modelo lo que no sabe o no puede verificar.

### Entregables

- Respuestas íntegras de ambos modelos.
- Análisis comparativo.
- Conclusiones.
- Opcional: evidencia de compilación y ejecución del servicio.

## Prompt de la tarea

````text
El siguiente texto corresponde al contenido de reporte_demo.json, generado por la función get_system_report() de la librería arrg_utils (clase SysInfo) en Python:

```json
{
  "host": "dofbotx-os",
  "platform": {
    "system": "Linux",
    "machine": "aarch64",
    "additional_info": {
      "id": "ubuntu",
      "name": "Ubuntu",
      "pretty_name": "Ubuntu 24.04.1 LTS",
      "version_id": "24.04",
      "version": "24.04.1 LTS (Noble Numbat)",
      "version_codename": "noble",
      "id_like": "debian",
      "ubuntu_codename": "noble"
    }
  },
  "ip": "172.16.8.136",
  "date": "22/10/2026",
  "time": "13:51:17",
  "cpu_stats": [
    {
      "id": 0,
      "label": "cpu",
      "type": "total",
      "core": -1,
      "user": 17394,
      "nice:": 1084,
      "system": 16347,
      "idle": 880262,
      "usaged": 3.6915633756125525
    },
    {
      "id": 1,
      "label": "cpu0",
      "type": "core",
      "core": 0,
      "user": 3462,
      "nice:": 374,
      "system": 5640,
      "idle": 217526,
      "usaged": 4.0162733642797885
    },
    {
      "id": 2,
      "label": "cpu1",
      "type": "core",
      "core": 1,
      "user": 5541,
      "nice:": 89,
      "system": 5236,
      "idle": 217871,
      "usaged": 4.7133585248941605
    },
    {
      "id": 3,
      "label": "cpu2",
      "type": "core",
      "core": 2,
      "user": 4765,
      "nice:": 463,
      "system": 3036,
      "idle": 221209,
      "usaged": 3.406401467184839
    },
    {
      "id": 4,
      "label": "cpu3",
      "type": "core",
      "core": 3,
      "user": 3624,
      "nice:": 157,
      "system": 2434,
      "idle": 223654,
      "usaged": 2.637215295674584
    }
  ],
  "disk": {
    "size": 59,
    "used": 23,
    "available": 34
  },
  "ram": {
    "total": 3.9,
    "used": 1.4,
    "free": 1.5,
    "available": 2.5
  },
  "network": [],
  "ros": {
    "version": 2,
    "distro": "jazzy",
    "domain_id": 10,
    "localhost_only": true
  }
}
```

El formato del reporte está compuesto por:
- "host": nombre del equipo, tipo string.
- "platform": diccionario con "system", "machine" y "additional_info"; este último contiene los datos de la distribución Ubuntu.
- "ip": dirección IP, tipo string.
- "date": fecha del reporte, tipo string.
- "time": hora del reporte, tipo string.
- "cpu_stats": lista de diccionarios; el primero representa el total y los siguientes, cada núcleo. Cada elemento contiene "id" (entero), "label" (string), "type" (string), "core" (entero), "user", "nice:", "system", "idle" (enteros) y "usaged" (flotante).
- "disk": diccionario con "size", "used" y "available", tipo flotante.
- "ram": diccionario con "total", "used", "free" y "available", tipo flotante.
- "network": lista de interfaces de red; puede estar vacía.
- "ros": diccionario con "version" (entero), "distro" (string), "domain_id" (entero) y "localhost_only" (booleano).

Como referencia, el paquete dofbot_interfaces ya contiene la interfaz srv/GetStatus.srv con el siguiente formato:

```text
bool is_robot_active
---
bool is_active
bool success
string string_status_message
```

Meta: Escribe un nuevo servicio de ROS 2 con las siguientes características:
- El servidor debe implementarse en el paquete existente dofbot_services, que es de tipo ament_python.
- La interfaz .srv debe crearse en el paquete existente dofbot_interfaces, que es de tipo ament_cmake, e integrarse en su CMakeLists.txt y package.xml.
- El servicio debe llamarse "system_report_srv" y usar una interfaz llamada "GetSystemReport.srv".
- La respuesta debe incluir, como mínimo: host, ip, fecha, hora, uso total de CPU, uso por núcleo, memoria RAM, disco y entorno ROS.
- El servidor debe obtener el reporte en tiempo de ejecución mediante arrg_utils.SysInfo().get_system_report(); el JSON anterior es solo una muestra del formato.
- Diseña la interfaz .srv con los campos necesarios; puedes aplanar la estructura o usar mensajes anidados, pero documenta tu decisión.
- Incluye un cliente de prueba en dofbot_services que invoque el servicio y muestre la respuesta.
- Registra el ejecutable del servidor como "system_report_srv" y el del cliente como "system_report_client" en setup.py.
- Actualiza setup.py y package.xml de dofbot_services para registrar ambos ejecutables y la dependencia de dofbot_interfaces.
- Explica brevemente cómo compilar y ejecutar el servicio con colcon y ros2 run, y cómo verificarlo con ros2 service list, ros2 service type y ros2 service call.
````

## Respuestas

### Respuesta de Google AI Assistant (Gemma4)

> `[Pegar aquí la respuesta completa de Gemma4.]`

### Respuesta de ChatGPT (ChatGPT6)

> `[Pegar aquí la respuesta completa de ChatGPT6.]`

## Análisis comparativo

| Criterio | Google AI Assistant (Gemma4) | ChatGPT (ChatGPT6) |
|---|---|---|
| Correctitud técnica | | |
| Completitud | | |
| Claridad | | |
| Supuestos | | |
| Valor agregado | | |
| Reconocimiento de incertidumbre | | |

### Preguntas guía

- ¿El modelo detectó que `dofbot_services` es `ament_python` y `dofbot_interfaces` es `ament_cmake`?
- ¿Actualizó correctamente `CMakeLists.txt`, `package.xml` y `setup.py`?
- ¿La interfaz `.srv` cubre los campos del reporte?
- ¿El servidor usa `arrg_utils.SysInfo.get_system_report()` en tiempo de ejecución?
- ¿El cliente de prueba es coherente con la interfaz?
- ¿Incluyó comandos de compilación, ejecución y verificación?
- ¿Qué supuestos hizo y cuáles son riesgosos?

## Conclusiones

`[Redactar aquí las conclusiones de la comparación.]`

## Verificación sugerida

```console
cd ~/ros2_ws
colcon build --packages-select dofbot_interfaces dofbot_services
source install/setup.bash
ros2 interface show dofbot_interfaces/srv/GetSystemReport
ros2 run dofbot_services system_report_srv
```

En otra terminal:

```console
ros2 service list
ros2 service type /system_report_srv
ros2 service call /system_report_srv dofbot_interfaces/srv/GetSystemReport "{...}"
```

> La petición YAML debe ajustarse a la interfaz `.srv` que haya diseñado el modelo. Si el servicio no aparece, verifica que el paquete `dofbot_services` se haya compilado y que el ejecutable esté registrado en `setup.py`.
