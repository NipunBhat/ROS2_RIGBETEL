#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class CPublisherNode : public rclcpp::Node
{
public:
    CPublisherNode() : Node("HelloWorldPublisherCpp"), m_iCount(0)
    {
        this->m_pPublisher = this->create_publisher<std_msgs::msg::String>("HelloWorldCppTopic" , 10);
        this->m_pTimer = this->create_wall_timer(500ms, std::bind(&CPublisherNode::timerCallback, this));
    }

protected:

private:
    void timerCallback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Hello World From CPP Node " + std::to_string(m_iCount++);
        RCLCPP_INFO(this->get_logger(), "Published: '%s'", message.data.c_str());
        m_pPublisher->publish(message);
        
    }
    std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String>> m_pPublisher;
    size_t m_iCount;
    std::shared_ptr<rclcpp::TimerBase> m_pTimer;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CPublisherNode>());
    rclcpp::shutdown();
    return 0;
}