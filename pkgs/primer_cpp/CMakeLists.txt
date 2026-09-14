cmake_minimum_required(VERSION 3.8)
project(primer_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(publisher_cpp src/publisher.cpp)
ament_target_dependencies(publisher_cpp rclcpp std_msgs)

add_executable(ejm1_cpp src/ejemplo_1.cpp)
ament_target_dependencies(ejm1_cpp rclcpp std_msgs)

add_executable(ejm2_cpp src/ejemplo_2.cpp)
ament_target_dependencies(ejm2_cpp rclcpp std_msgs)

install(TARGETS
    publisher_cpp
    ejm1_cpp
    ejm2_cpp
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
