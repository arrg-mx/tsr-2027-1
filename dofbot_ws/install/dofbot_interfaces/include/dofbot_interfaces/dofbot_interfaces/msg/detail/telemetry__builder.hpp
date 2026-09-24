// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dofbot_interfaces/msg/telemetry.hpp"


#ifndef DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__BUILDER_HPP_
#define DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dofbot_interfaces/msg/detail/telemetry__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dofbot_interfaces
{

namespace msg
{

namespace builder
{

class Init_Telemetry_arm_pose
{
public:
  explicit Init_Telemetry_arm_pose(::dofbot_interfaces::msg::Telemetry & msg)
  : msg_(msg)
  {}
  ::dofbot_interfaces::msg::Telemetry arm_pose(::dofbot_interfaces::msg::Telemetry::_arm_pose_type arg)
  {
    msg_.arm_pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dofbot_interfaces::msg::Telemetry msg_;
};

class Init_Telemetry_status
{
public:
  Init_Telemetry_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Telemetry_arm_pose status(::dofbot_interfaces::msg::Telemetry::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Telemetry_arm_pose(msg_);
  }

private:
  ::dofbot_interfaces::msg::Telemetry msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::dofbot_interfaces::msg::Telemetry>()
{
  return dofbot_interfaces::msg::builder::Init_Telemetry_status();
}

}  // namespace dofbot_interfaces

#endif  // DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__BUILDER_HPP_
