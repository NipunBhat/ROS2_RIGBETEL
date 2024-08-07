import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
import random

'''
This node will move the turtle around, random movements with no real end goal
'''
class MoveTurtle(Node):
    def __init__(self) -> None:
        try:
            super().__init__("turtle_mover")
            print("Start of Constructor")
            self.__publisher = None
            self.__initPublisher()
            print("End Of Constructor")
        except Exception as e:
            self.get_logger().error(str(e)) 
    
    def __initPublisher(self) -> None:
        try:
            self.__publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
            self.create_timer(0.5, self.publish_random_motion)
        except Exception as e:
            self.get_logger().error(str(e))
    
    def publish_random_motion(self) -> None:
        try:     
            print("Start of publish random motion")       
            angular_data = Vector3()
            angular_data.x = random.uniform(-1.0, 1.0)
            angular_data.y = 0.0
            angular_data.z = 0.0
            print("Set Angular Data")
    
            
            #Settting linear data
            linear_data = Vector3()
            linear_data.x = random.uniform(0.0, 360.0)
            angular_data.y = 0.0
            angular_data.z = 0.0
            
            #Setting twist data
            motion_data = Twist()
            motion_data.angular = angular_data
            motion_data.linear = linear_data
            
            #Publish prepared data
            self.__publisher.publish(motion_data)
            self.get_logger().info("PUBLISHED DATA TO THE TURTLE")
        except Exception as e:
            self.get_logger().error(str(e))

def main(args = None):
    try:
        rclpy.init(args = args)
        node = MoveTurtle()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()