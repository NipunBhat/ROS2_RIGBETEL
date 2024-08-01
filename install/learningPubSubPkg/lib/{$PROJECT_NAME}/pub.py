#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg._string import String

class HelloWorldPubliser(Node):
    def __init__(self) -> None:
        try:
            self.publisher = None
            self.iter = 0

            self.__initNode()    # Init Node
        except Exception as e:
            self.get_logger().error(str(e))
        
    def __initNode(self) -> None:
        try:
            super().__init__("HelloWorldPublisher")
            self.publisher = self.create_publisher(String, 'topic', 10)
            timerPeriod = 0.5 #make this an externally configurable param later. 
            self.create_timer(timerPeriod, self.callBackFunction)
            self.get_logger().info("Initialised Publisher")
        except Exception as e:
            self.get_logger().error(str(e))

    def callBackFunction(self) -> None:
        try:
            msg = String()
            msg.data = f"Hello World {self.iter}"
            self.publisher.publish(msg)
            self.get_logger().info(f"Published Message : {msg.data}")
            self.iter += 1
        except Exception as e:
            self.get_logger().error(str(e))

def main(args) -> None:
    try:
        rclpy.init(args=args)
        publisherNode = HelloWorldPubliser()
        rclpy.spin(publisherNode)
    except Exception as e:
        print(f"Error:{str(e)}")
    finally:
        publisherNode.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main(None)


 