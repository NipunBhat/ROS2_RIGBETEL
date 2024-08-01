#include <iostream>
#include <memory>
#include <random>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/float32.hpp>
#include <std_msgs/msg/bool.hpp>
#include <chrono>

using std::placeholders::_1;

static std::unordered_map<int, std::string> topics = {{1 , "Topic1"}, {2, "Topic2"},};

typedef std_msgs::msg::Bool BOOL;
typedef std_msgs::msg::Float32 FLOAT32;

class CTempPub : public rclcpp::Node
{
public:
    CTempPub() : rclcpp::Node("temp_node")
    {
        m_pPub = this->create_publisher<BOOL>(topics[2], 10);
        m_pSub = this->create_subscription<FLOAT32>(topics[1] , 10, std::bind(&CTempPub::_analyseTemp, this, _1));
    }
protected:
    // NOP
private:

    //Functions
    void _analyseTemp(const FLOAT32 temp)
    {
        float f_temp = static_cast<float>(temp.data);
        auto status = BOOL();

        RCLCPP_INFO(this->get_logger(), "Recieved temperature '%f'", f_temp);

        if(f_temp > 1.5)
        {
            status.data = false;
        }
        else
        {
            status.data = true;
        }

        _publishStatus(status);
    }

    void _publishStatus(const BOOL &status)
    {
        this->m_pPub->publish(status);
        RCLCPP_INFO(this->get_logger(), "Published Status '%d'", static_cast<int>(status.data));
    }

    //Members
    std::shared_ptr<rclcpp::Publisher<BOOL>> m_pPub;
    std::shared_ptr<rclcpp::Subscription<FLOAT32>> m_pSub;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CTempPub>());
    rclcpp::shutdown();
    return 0;
}

