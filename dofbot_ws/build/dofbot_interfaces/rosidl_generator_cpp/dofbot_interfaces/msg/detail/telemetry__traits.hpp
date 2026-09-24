// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dofbot_interfaces/msg/telemetry.hpp"


#ifndef DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__TRAITS_HPP_
#define DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dofbot_interfaces/msg/detail/telemetry__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'arm_pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace dofbot_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Telemetry & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: arm_pose
  {
    out << "arm_pose: ";
    to_flow_style_yaml(msg.arm_pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Telemetry & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: arm_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "arm_pose:\n";
    to_block_style_yaml(msg.arm_pose, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Telemetry & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace dofbot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use dofbot_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dofbot_interfaces::msg::Telemetry & msg,
  std::ostream & out, size_t indentation = 0)
{
  dofbot_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dofbot_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const dofbot_interfaces::msg::Telemetry & msg)
{
  return dofbot_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<dofbot_interfaces::msg::Telemetry>()
{
  return "dofbot_interfaces::msg::Telemetry";
}

template<>
inline const char * name<dofbot_interfaces::msg::Telemetry>()
{
  return "dofbot_interfaces/msg/Telemetry";
}

template<>
struct has_fixed_size<dofbot_interfaces::msg::Telemetry>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dofbot_interfaces::msg::Telemetry>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dofbot_interfaces::msg::Telemetry>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__TRAITS_HPP_
