// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice
#ifndef DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "dofbot_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "dofbot_interfaces/msg/detail/telemetry__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
bool cdr_serialize_dofbot_interfaces__msg__Telemetry(
  const dofbot_interfaces__msg__Telemetry * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
bool cdr_deserialize_dofbot_interfaces__msg__Telemetry(
  eprosima::fastcdr::Cdr &,
  dofbot_interfaces__msg__Telemetry * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
size_t get_serialized_size_dofbot_interfaces__msg__Telemetry(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
size_t max_serialized_size_dofbot_interfaces__msg__Telemetry(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
bool cdr_serialize_key_dofbot_interfaces__msg__Telemetry(
  const dofbot_interfaces__msg__Telemetry * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
size_t get_serialized_size_key_dofbot_interfaces__msg__Telemetry(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
size_t max_serialized_size_key_dofbot_interfaces__msg__Telemetry(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dofbot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dofbot_interfaces, msg, Telemetry)();

#ifdef __cplusplus
}
#endif

#endif  // DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
