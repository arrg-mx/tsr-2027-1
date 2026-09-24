#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to dofbot_interfaces__msg__Telemetry
/// Dofbot telemetry message
/// Mensaje de interface para telemetria

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Telemetry {
    ///  Asi era antes
    /// string status # Descripcion del estado del robot
    /// float32 pos_x # posicion del efector final en x
    /// float32 pos_y # posicion del efector final en y
    /// float32 pos_z # posicion del efector final en z
    pub status: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub arm_pose: geometry_msgs::msg::Pose,

}



impl Default for Telemetry {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Telemetry::default())
  }
}

impl rosidl_runtime_rs::Message for Telemetry {
  type RmwMsg = super::msg::rmw::Telemetry;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        status: msg.status.as_str().into(),
        arm_pose: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Owned(msg.arm_pose)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        status: msg.status.as_str().into(),
        arm_pose: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Borrowed(&msg.arm_pose)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      status: msg.status.to_string(),
      arm_pose: geometry_msgs::msg::Pose::from_rmw_message(msg.arm_pose),
    }
  }
}


