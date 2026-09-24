# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target dofbot_interfaces::dofbot_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${dofbot_interfaces_TARGETS}.
if(dofbot_interfaces_TARGETS AND NOT TARGET dofbot_interfaces::dofbot_interfaces)
  add_library(dofbot_interfaces::dofbot_interfaces INTERFACE IMPORTED)
  set_target_properties(dofbot_interfaces::dofbot_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${dofbot_interfaces_TARGETS}")
endif()
