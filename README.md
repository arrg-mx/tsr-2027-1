# Temas Selectos de Robotica 2027-I

## Introduccion

Este repositorio contiene el material del curso **Temas Selectos de Robotica (TSR) 2027-I**, enfocado en el desarrollo de aplicaciones roboticas utilizando **ROS 2 Jazzy Jalisco**.

ROS 2 (Robot Operating System 2) es un marco de trabajo (middleware) distribuido que permite construir sistemas roboticos modulares mediante la comunicacion entre nodos independientes, que se intercambian datos a traves de topics, servicios y acciones.

## Conceptos basicos de ROS 2 Jazzy

- **Nodos**: procesos individuales que realizan una tarea especifica (por ejemplo, controlar un motor o procesar una imagen).
- **Topics**: canales de comunicacion asincrona donde los nodos publican (publisher) o se suscriben (subscriber) a mensajes.
- **Servicios (Services)**: comunicacion sincrona de peticion-respuesta entre nodos.
- **Acciones (Actions)**: comunicación de larga duracion con objetivo, retroalimentacion y resultado.
- **Graph / DDS**: la capa de transporte (Data Distribution Service) que conecta todos los nodos de forma transparente, incluso entre multiples maquinas.
- **Workspace / Packages**: estructura de carpetas (`src`, `build`, `install`, `log`) donde se organizan los paquetes que contienen nodos, librerias y definiciones de interfaces.
- **Launch files**: archivos que permiten iniciar varios nodos y configuraciones de forma conjunta.
- **CLI de ROS 2**: herramientas como `ros2 node list`, `ros2 topic list`, `ros2 topic echo`, `ros2 run`, `ros2 launch`, `colcon build` y `source install/setup.bash`.

## Contenido del curso de TSR

1. Introduccion
1. Contenido
