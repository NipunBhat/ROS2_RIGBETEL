#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool

class AnalysisNode(Node):
    def __init__(self) -> None:
        try:
            super().__init__("temp_analysis")
            self.__temp_sub = None
            self.__status_pub = None
            
            self.__init_status_pub()
            self.__start_sub()
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __init_status_pub(self) -> None:
        try:
            self.__status_pub = self.create_publisher(Bool, "Topic2", 10)
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __start_sub(self) -> None:
        try:
            self.create_subscription(Float32, "Topic1", self.__analyse_temp, 10)
        except Exception as e:
            self.get_logger(str(e))
    
    def __analyse_temp(self , temp) -> None:
        try:
            temperature = temp.data
            self.get_logger().info(f"Recieved temperature {temp.data}")
            on_off = Bool()
            if temperature > 1.5:
                on_off.data = False
            else:
                on_off.data = True
            self.__status_pub.publish(on_off)
            self.get_logger().info(f"Published Status : {on_off}")
        except Exception as e:
            self.get_logger().error(str(e))

def main(args = None):
    try:
        rclpy.init(args = args)
        analysis_node = AnalysisNode()
        rclpy.spin(analysis_node)
        analysis_node.destroy_node()
        rclpy.shutdown()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()