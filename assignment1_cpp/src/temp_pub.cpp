#include <iostream>
#include <memory>
#include <random>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/float32.hpp>
#include <chrono>

using namespace std::chrono_literals;
typedef std_msgs::msg::Float32 FLOAT32;

class CTempPub : public rclcpp::Node
{
public:
    CTempPub() : Node("temp_pub")
    {
        m_pPub = this->create_publisher<FLOAT32>("Topic1", 10);
        m_pTimer = this->create_wall_timer(500ms, std::bind(&CTempPub::timer_callback, this));
    }
    ~CTempPub()
    {
        //NOP
    }

protected:

private:
    void timer_callback()
    {
        auto temp = FLOAT32(); 

        std::random_device rd;
        std::mt19937 gen(rd());

        // Define the range [1, 2]
        std::uniform_real_distribution<> dis(1.0, 2.0);
        // Generate a random number in the range
        temp.data = dis(gen);
        RCLCPP_INFO(this->get_logger(), "Published Temperature '%f'", temp.data);
        m_pPub->publish(temp);
    }

    //Member Variables
    std::shared_ptr<rclcpp::Publisher<FLOAT32>> m_pPub;
    std::shared_ptr<rclcpp::TimerBase> m_pTimer;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CTempPub>());
    rclcpp::shutdown();
    return 0;
}