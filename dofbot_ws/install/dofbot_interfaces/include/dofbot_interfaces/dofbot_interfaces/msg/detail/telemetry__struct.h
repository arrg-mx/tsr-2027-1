// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dofbot_interfaces/msg/telemetry.h"


#ifndef DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_H_
#define DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'status'
#include "rosidl_runtime_c/string.h"
// Member 'arm_pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in msg/Telemetry in the package dofbot_interfaces.
/**
  * Dofbot telemetry message
  * Mensaje de interface para telemetria
 */
typedef struct dofbot_interfaces__msg__Telemetry
{
  ///  Asi era antes
  /// string status # Descripcion del estado del robot
  /// float32 pos_x # posicion del efector final en x
  /// float32 pos_y # posicion del efector final en y
  /// float32 pos_z # posicion del efector final en z
  rosidl_runtime_c__String status;
  geometry_msgs__msg__Pose arm_pose;
} dofbot_interfaces__msg__Telemetry;

// Struct for a sequence of dofbot_interfaces__msg__Telemetry.
typedef struct dofbot_interfaces__msg__Telemetry__Sequence
{
  dofbot_interfaces__msg__Telemetry * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dofbot_interfaces__msg__Telemetry__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_H_
