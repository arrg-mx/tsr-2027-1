
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <chrono>

using namespace std::chrono_literals;

class MyNode : public rclcpp::Node
{
public:
    MyNode() : Node("pulisher_node"), count_(0)
    {
        publisher_ =this->create_publisher<std_msgs::msg::Int32>("publisher_topic", 10);
        timer_ =this->create_wall_timer(1s, std::bind(&MyNode::timer_callback, this));
    }
private:
    void timer_callback()
    {
        auto message = std_msgs::msg::Int32();
        message.data = 3;
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Publicando '%d'", message.data);
    }
    rclcpp::Publisher<std_msgs::msg::Int32>SharedPtr publisher_;
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
