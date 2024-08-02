#include <iostream>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/bool.hpp>

using namespace rclcpp;
using std::placeholders::_1;

typedef std_msgs::msg::Bool BOOL;

class CStatusSub : public rclcpp::Node
{
public:
    CStatusSub() : Node("NODE3")
    {
        m_hStatusSub = this->create_subscription<BOOL>("TOPIC2", 10, std::bind(&CStatusSub::_declareStatus, this, _1));
    }

    ~CStatusSub()
    {
        //NOP
    }
protected:
    //NOP
private:
    //Functions
    void _declareStatus(const BOOL &status)
    {
        RCLCPP_INFO(this->get_logger(), "Recieved Status '%d'", static_cast<int>(status.data));
    }
    //Members
    std::shared_ptr<Subscription<BOOL>> m_hStatusSub;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CStatusSub>());
    rclcpp::shutdown();
    return 0;
}