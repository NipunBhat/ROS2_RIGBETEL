#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPub(Node):
    def __init__(self) -> None:
        try:
            super().__init__("HelloWorldPublisher")
            self.__publisher = None
            self.__counter = 0
            
            self.__initPublisher() 
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __initPublisher(self) -> None:
        try:
            self.__publisher = self.create_publisher(String, "HelloWorldTopic", 10)
            self.create_timer(0.5, self.publishData)
        except Exception as e:
            self.get_logger().error(str(e))
    
    def publishData(self) -> None:
        try:
            msg = String()
            msg.data = f"Hello from publisher {self.__counter}"
            self.__publisher.publish(msg)
            self.get_logger().info(f"Published : {msg.data}")
            self.__counter += 1
        except Exception as e:
            self.get_logger().error(str(e))
            
def main(args = None):
    publisherNode = None
    try:
        rclpy.init(args=args)
        publisherNode = HelloWorldPub()
        rclpy.spin(publisherNode)
    except Exception as e:
        print(str(e))
    finally:
        publisherNode.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
