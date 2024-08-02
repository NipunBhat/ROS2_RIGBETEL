#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

'''
    This Node will send a random float temperature to analysis node.
'''
class TempPub(Node):
    def __init__(self) -> None:
        try:
            super().__init__("temp_pub")
            self.__publisher = None
            self.__start_publisher()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __start_publisher(self) -> None:
        try:
            
            self.__publisher = self.create_publisher(Float32, "Topic1", 10)
            self.create_timer(0.5, self.__publishTemperature)
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __publishTemperature(self) -> None:
        try:
            temp = Float32()
            temp.data = random.uniform(1.0, 2.0)
            self.__publisher.publish(temp)
            self.get_logger().info(f"Temperature is {temp.data}")
        except Exception as e:
            self.get_logger().error(str(e))

def main(args = None):
    try:
        rclpy.init(args = args)
        tempNode = TempPub()
        rclpy.spin(tempNode)
        tempNode.destroy_node()
        rclpy.shutdown()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    