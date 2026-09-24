#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "dofbot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__dofbot_interfaces__msg__Telemetry() -> *const std::ffi::c_void;
}

#[link(name = "dofbot_interfaces__rosidl_generator_c")]
extern "C" {
    fn dofbot_interfaces__msg__Telemetry__init(msg: *mut Telemetry) -> bool;
    fn dofbot_interfaces__msg__Telemetry__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Telemetry>, size: usize) -> bool;
    fn dofbot_interfaces__msg__Telemetry__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Telemetry>);
    fn dofbot_interfaces__msg__Telemetry__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Telemetry>, out_seq: *mut rosidl_runtime_rs::Sequence<Telemetry>) -> bool;
}

// Corresponds to dofbot_interfaces__msg__Telemetry
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Dofbot telemetry message
/// Mensaje de interface para telemetria

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Telemetry {
    ///  Asi era antes
    /// string status # Descripcion del estado del robot
    /// float32 pos_x # posicion del efector final en x
    /// float32 pos_y # posicion del efector final en y
    /// float32 pos_z # posicion del efector final en z
    pub status: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub arm_pose: geometry_msgs::msg::rmw::Pose,

}



impl Default for Telemetry {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !dofbot_interfaces__msg__Telemetry__init(&mut msg as *mut _) {
        panic!("Call to dofbot_interfaces__msg__Telemetry__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Telemetry {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dofbot_interfaces__msg__Telemetry__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dofbot_interfaces__msg__Telemetry__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { dofbot_interfaces__msg__Telemetry__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Telemetry {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Telemetry where Self: Sized {
  const TYPE_NAME: &'static str = "dofbot_interfaces/msg/Telemetry";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__dofbot_interfaces__msg__Telemetry() }
  }
}


