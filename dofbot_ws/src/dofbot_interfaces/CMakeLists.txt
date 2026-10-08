cmake_minimum_required(VERSION 3.8)
project(dofbot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
# 1a. Si se incluye mensajes ya existentes hay que incluir la refrencia al 
# paquete del mensaje
find_package(geometry_msgs REQUIRED)


# 2. Localizacion de descriptores de mensajes
rosidl_generate_interfaces(${PROJECT_NAME}
  # Aqui se colocan los archivos de descripcion de los mensajes a generar
  "msg/Telemetry.msg"
  "srv/GetStatus.srv"
  # Dependenias de otros mensajes que esten incluidos en el mensaje
  #  personalizado a generar
  DEPENDENCIES geometry_msgs
)

# 3. Exportar el resultado de la genracion 
ament_export_dependencies(rosidl_default_runtime)

ament_package()
