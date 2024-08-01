#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HellWorldSubscriber(Node):
    def __init__(self) -> None:
        try:
            super().__init__("HelloWorldSubscriber")
            self.__subscriber = None
            self.__initSubscriber()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __initSubscriber(self) -> None:
        try:
            self.__subscriber = self.create_subscription(String, "HelloWorldTopic", self.__listenerCallBack, 10)
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __listenerCallBack(self, msg) -> None:
        try:
            self.get_logger().info(f"Recieved {msg.data}")
        except Exception as e:
            self.get_logger().error(str(e))
            
def main(args = None) -> None:
    try:
        rclpy.init(args = args)
        subscriberNode = HellWorldSubscriber()
        rclpy.spin(subscriberNode)
    except Exception as e:
        print(str(e))
    finally:
        subscriberNode.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()