// generated from rosidl_generator_cpp/resource/rosidl_generator_cpp__visibility_control.hpp.in
// generated code does not contain a copyright notice

#ifndef DOFBOT_INTERFACES__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
#define DOFBOT_INTERFACES__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_CPP_EXPORT_dofbot_interfaces __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_CPP_IMPORT_dofbot_interfaces __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_CPP_EXPORT_dofbot_interfaces __declspec(dllexport)
    #define ROSIDL_GENERATOR_CPP_IMPORT_dofbot_interfaces __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_CPP_BUILDING_DLL_dofbot_interfaces
    #define ROSIDL_GENERATOR_CPP_PUBLIC_dofbot_interfaces ROSIDL_GENERATOR_CPP_EXPORT_dofbot_interfaces
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_dofbot_interfaces ROSIDL_GENERATOR_CPP_IMPORT_dofbot_interfaces
  #endif
#else
  #define ROSIDL_GENERATOR_CPP_EXPORT_dofbot_interfaces __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_CPP_IMPORT_dofbot_interfaces
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_CPP_PUBLIC_dofbot_interfaces __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_dofbot_interfaces
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // DOFBOT_INTERFACES__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
