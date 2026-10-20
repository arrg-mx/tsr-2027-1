#-------- Etapa1 : Construccion (Builder)
# 1. Toma como base una imagne ya existente para crear la
# nueva imagen
FROM dustynv/ros:jazzy-ros-base-r36.4.0-cu128-24.04

# Solucion a la migracion de llaves de ROS2 
# Issue: https://discourse.openrobotics.org/t/ros-signing-key-migration-guide/43937/30
# jetson-sontainers issue solved: 
# https://github.com/dusty-nv/jetson-containers/issues/1124    
RUN curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# 2. Instalar las librerias de construccion necesarias a nivel
# Sistema Operativo (Ubuntu/linux)
RUN apt-get update && \
    apt-get install python3-pip python3-dev python3-smbus python3-smbus2 python3-pil i2c-tools -y && \
    apt install ros-jazzy-rmw-cyclonedds-cpp -y && \
    rm -rf /var/lib/apt/list/*

#---------- Stage 2: Runtime ------------
# Cambiamos la ejecución al usuario ubuntu
USER ubuntu
# Asignamos el directorio de trabajo del usuario
WORKDIR /home/ubuntu

# Agregamos dos variables de entorno en el contenedor
ENV ROS_DOMAIN_ID=10
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

CMD ["bash"]
