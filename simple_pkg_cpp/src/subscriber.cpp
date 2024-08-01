#include <memory>
#include "rclcpp/rclcpp.hpp"

#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

using namespace std::chrono_literals;

class CSubscriberNode : public rclcpp::Node
{
public:
    CSubscriberNode() : Node("HelloWorldSubscriberCpp")
    {
        this->m_pSubscription = this->create_subscription<std_msgs::msg::String>("HelloWorldCppTopic", 10, std::bind(&CSubscriberNode::topic_callback, this, _1));
    }

protected:
//NOP
private:
    void topic_callback(const std::shared_ptr<std_msgs::msg::String> msg)
    {
        RCLCPP_INFO(this->get_logger(), "Recieved value '%s'", msg->data.c_str());
    }
    std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String>> m_pSubscription;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CSubscriberNode>());
    rclcpp::shutdown();
    return 0;
}
