
#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

using namespace std::chrono_literals;

class MyNode : public rclcpp::Node
{
public:
    MyNode() : Node("publicador_cpp"), count_(0)
    {
        publisher_ = this->create_publisher<std_msgs::msg::Int32>("publisher_topic", 10);
        timer_ = this->create_wall_timer(1s, std::bind(&MyNode::timer_callback, this));
    }

private:
    void timer_callback()
    {
        auto message = std_msgs::msg::Int32();
        message.data = 3;
        RCLCPP_INFO(this->get_logger(), "Publicando '%d'", message.data);
        publisher_->publish(message);

    }

    rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    size_t count_;   
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyNode>());
    rclcpp::shutdown();
    return 0;
}


