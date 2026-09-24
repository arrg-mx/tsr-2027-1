#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class MiSuscriptor : public rclcpp::Node
{
public:
    MiSuscriptor() : Node("suscriptor_cpp")
    {
        // Suscripción al tópico: (Nombre del topic, Calidad de servicio QoS, Callback)
        subscription_ = this->create_subscription<std_msgs::msg::Int32>(
            "publisher_topic",
            10,
            std::bind(&MiSuscriptor::topic_callback, this, std::placeholders::_1)
        );

        RCLCPP_INFO(this->get_logger(), "Nodo suscriptor C++ listo y escuchando.");
    }

private:
    void topic_callback(const std_msgs::msg::Int32::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(), "Mensaje recibido: %d", msg->data);
    }

    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MiSuscriptor>());
    rclcpp::shutdown();
    return 0;
}