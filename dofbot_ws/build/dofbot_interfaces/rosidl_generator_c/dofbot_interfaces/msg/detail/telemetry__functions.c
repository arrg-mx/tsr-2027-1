// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from dofbot_interfaces:msg/Telemetry.idl
// generated code does not contain a copyright notice
#include "dofbot_interfaces/msg/detail/telemetry__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `status`
#include "rosidl_runtime_c/string_functions.h"
// Member `arm_pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
dofbot_interfaces__msg__Telemetry__init(dofbot_interfaces__msg__Telemetry * msg)
{
  if (!msg) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    dofbot_interfaces__msg__Telemetry__fini(msg);
    return false;
  }
  // arm_pose
  if (!geometry_msgs__msg__Pose__init(&msg->arm_pose)) {
    dofbot_interfaces__msg__Telemetry__fini(msg);
    return false;
  }
  return true;
}

void
dofbot_interfaces__msg__Telemetry__fini(dofbot_interfaces__msg__Telemetry * msg)
{
  if (!msg) {
    return;
  }
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // arm_pose
  geometry_msgs__msg__Pose__fini(&msg->arm_pose);
}

bool
dofbot_interfaces__msg__Telemetry__are_equal(const dofbot_interfaces__msg__Telemetry * lhs, const dofbot_interfaces__msg__Telemetry * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // arm_pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->arm_pose), &(rhs->arm_pose)))
  {
    return false;
  }
  return true;
}

bool
dofbot_interfaces__msg__Telemetry__copy(
  const dofbot_interfaces__msg__Telemetry * input,
  dofbot_interfaces__msg__Telemetry * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // arm_pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->arm_pose), &(output->arm_pose)))
  {
    return false;
  }
  return true;
}

dofbot_interfaces__msg__Telemetry *
dofbot_interfaces__msg__Telemetry__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dofbot_interfaces__msg__Telemetry * msg = (dofbot_interfaces__msg__Telemetry *)allocator.allocate(sizeof(dofbot_interfaces__msg__Telemetry), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(dofbot_interfaces__msg__Telemetry));
  bool success = dofbot_interfaces__msg__Telemetry__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
dofbot_interfaces__msg__Telemetry__destroy(dofbot_interfaces__msg__Telemetry * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    dofbot_interfaces__msg__Telemetry__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
dofbot_interfaces__msg__Telemetry__Sequence__init(dofbot_interfaces__msg__Telemetry__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dofbot_interfaces__msg__Telemetry * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(dofbot_interfaces__msg__Telemetry)) {
      return false;
    }
    data = (dofbot_interfaces__msg__Telemetry *)allocator.zero_allocate(size, sizeof(dofbot_interfaces__msg__Telemetry), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = dofbot_interfaces__msg__Telemetry__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        dofbot_interfaces__msg__Telemetry__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
dofbot_interfaces__msg__Telemetry__Sequence__fini(dofbot_interfaces__msg__Telemetry__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      dofbot_interfaces__msg__Telemetry__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

dofbot_interfaces__msg__Telemetry__Sequence *
dofbot_interfaces__msg__Telemetry__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dofbot_interfaces__msg__Telemetry__Sequence * array = (dofbot_interfaces__msg__Telemetry__Sequence *)allocator.allocate(sizeof(dofbot_interfaces__msg__Telemetry__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = dofbot_interfaces__msg__Telemetry__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
dofbot_interfaces__msg__Telemetry__Sequence__destroy(dofbot_interfaces__msg__Telemetry__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    dofbot_interfaces__msg__Telemetry__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
dofbot_interfaces__msg__Telemetry__Sequence__are_equal(const dofbot_interfaces__msg__Telemetry__Sequence * lhs, const dofbot_interfaces__msg__Telemetry__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!dofbot_interfaces__msg__Telemetry__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
dofbot_interfaces__msg__Telemetry__Sequence__copy(
  const dofbot_interfaces__msg__Telemetry__Sequence * input,
  dofbot_interfaces__msg__Telemetry__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(dofbot_interfaces__msg__Telemetry)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(dofbot_interfaces__msg__Telemetry);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    dofbot_interfaces__msg__Telemetry * data =
      (dofbot_interfaces__msg__Telemetry *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!dofbot_interfaces__msg__Telemetry__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          dofbot_interfaces__msg__Telemetry__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!dofbot_interfaces__msg__Telemetry__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
