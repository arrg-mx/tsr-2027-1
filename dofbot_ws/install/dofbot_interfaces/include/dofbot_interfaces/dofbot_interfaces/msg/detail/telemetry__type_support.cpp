// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "dofbot_interfaces/msg/detail/telemetry__functions.h"
#include "dofbot_interfaces/msg/detail/telemetry__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace dofbot_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Telemetry_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) dofbot_interfaces::msg::Telemetry(_init);
}

void Telemetry_fini_function(void * message_memory)
{
  auto typed_message = static_cast<dofbot_interfaces::msg::Telemetry *>(message_memory);
  typed_message->~Telemetry();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Telemetry_message_member_array[2] = {
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dofbot_interfaces::msg::Telemetry, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "arm_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::Pose>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dofbot_interfaces::msg::Telemetry, arm_pose),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Telemetry_message_members = {
  "dofbot_interfaces::msg",  // message namespace
  "Telemetry",  // message name
  2,  // number of fields
  sizeof(dofbot_interfaces::msg::Telemetry),
  false,  // has_any_key_member_
  Telemetry_message_member_array,  // message members
  Telemetry_init_function,  // function to initialize message memory (memory has to be allocated)
  Telemetry_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Telemetry_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Telemetry_message_members,
  get_message_typesupport_handle_function,
  &dofbot_interfaces__msg__Telemetry__get_type_hash,
  &dofbot_interfaces__msg__Telemetry__get_type_description,
  &dofbot_interfaces__msg__Telemetry__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace dofbot_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<dofbot_interfaces::msg::Telemetry>()
{
  return &::dofbot_interfaces::msg::rosidl_typesupport_introspection_cpp::Telemetry_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, dofbot_interfaces, msg, Telemetry)() {
  return &::dofbot_interfaces::msg::rosidl_typesupport_introspection_cpp::Telemetry_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
