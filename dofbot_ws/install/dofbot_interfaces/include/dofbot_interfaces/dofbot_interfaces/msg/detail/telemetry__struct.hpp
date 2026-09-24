// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dofbot_interfaces/msg/telemetry.hpp"


#ifndef DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_HPP_
#define DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'arm_pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__dofbot_interfaces__msg__Telemetry __attribute__((deprecated))
#else
# define DEPRECATED__dofbot_interfaces__msg__Telemetry __declspec(deprecated)
#endif

namespace dofbot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Telemetry_
{
  using Type = Telemetry_<ContainerAllocator>;

  explicit Telemetry_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : arm_pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = "";
    }
  }

  explicit Telemetry_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : status(_alloc),
    arm_pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = "";
    }
  }

  // field types and members
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;
  using _arm_pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _arm_pose_type arm_pose;

  // setters for named parameter idiom
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__arm_pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->arm_pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    dofbot_interfaces::msg::Telemetry_<ContainerAllocator> *;
  using ConstRawPtr =
    const dofbot_interfaces::msg::Telemetry_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dofbot_interfaces::msg::Telemetry_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dofbot_interfaces::msg::Telemetry_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dofbot_interfaces__msg__Telemetry
    std::shared_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dofbot_interfaces__msg__Telemetry
    std::shared_ptr<dofbot_interfaces::msg::Telemetry_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Telemetry_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->arm_pose != other.arm_pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const Telemetry_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Telemetry_

// alias to use template instance with default allocator
using Telemetry =
  dofbot_interfaces::msg::Telemetry_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace dofbot_interfaces

#endif  // DOFBOT_INTERFACES__MSG__DETAIL__TELEMETRY__STRUCT_HPP_
