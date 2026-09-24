// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "dofbot_interfaces/msg/detail/telemetry__rosidl_typesupport_introspection_c.h"
#include "dofbot_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "dofbot_interfaces/msg/detail/telemetry__functions.h"
#include "dofbot_interfaces/msg/detail/telemetry__struct.h"


// Include directives for member types
// Member `status`
#include "rosidl_runtime_c/string_functions.h"
// Member `arm_pose`
#include "geometry_msgs/msg/pose.h"
// Member `arm_pose`
#include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  dofbot_interfaces__msg__Telemetry__init(message_memory);
}

void dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_fini_function(void * message_memory)
{
  dofbot_interfaces__msg__Telemetry__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dofbot_interfaces__msg__Telemetry, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "arm_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dofbot_interfaces__msg__Telemetry, arm_pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_members = {
  "dofbot_interfaces__msg",  // message namespace
  "Telemetry",  // message name
  2,  // number of fields
  sizeof(dofbot_interfaces__msg__Telemetry),
  false,  // has_any_key_member_
  dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array,  // message members
  dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_init_function,  // function to initialize message memory (memory has to be allocated)
  dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle = {
  0,
  &dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_members,
  get_message_typesupport_handle_function,
  &dofbot_interfaces__msg__Telemetry__get_type_hash,
  &dofbot_interfaces__msg__Telemetry__get_type_description,
  &dofbot_interfaces__msg__Telemetry__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_dofbot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dofbot_interfaces, msg, Telemetry)() {
  dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  if (!dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle.typesupport_identifier) {
    dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &dofbot_interfaces__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
