#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class outcomSubscriber(Node):
    def __init__(self) -> None:
        try:
            super().__init__("NODE3")
            self.__sub = None
            
            self.__start_sub()
        except Exception as e:
            self.get_logger().error(str(e))

    def __start_sub(self) -> None:
        try:
            self.create_subscription(Bool, "TOPIC2", self.__log_status, 10)
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __log_status(self, msg) -> None:
        try:
            if msg.data == True:
                self.get_logger().info("Status : ON")
            else:
                self.get_logger().info("Status : OFF")
        except Exception as e:
            self.get_logger().error(str(e))
    
def main(args = None) -> None:
    try:
        rclpy.init(args=args)
        outcome_sub = outcomSubscriber()
        rclpy.spin(outcome_sub)
        outcome_sub.destroy_node()
        rclpy.shutdown()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()