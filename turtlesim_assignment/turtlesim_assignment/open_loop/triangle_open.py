#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
import math
import time
class TriangleClosedLoop(Node):
    def __init__(self)-> None:
        try:
            super().__init__("triangle_open_loop")
            
            self.__mover_msg = Twist()
            self.__mover_msg.linear.x = 0.0 # set the linear velocity to 0
            self.__mover_msg.angular.z = 0.0 # set the angular velocity to 0
            
            self.__linear_speed = 4.0
            self.__turn_speed = math.radians(120)
                        
            # Initialize state variables
            self.__current_side = 1
            self.__moving_forward = True
                                
            self.__publisher = None
            self.__start_time = self.get_clock().now()

            self.__init_pub()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __init_pub(self) -> None:
        try:
            self.__publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
            time.sleep(1)
            self.create_timer(1.01, self.__draw_triangle) #1.01 was pure luck
        except Exception as e:
            self.get_logger.error(str(e))
            
    def __draw_triangle(self) -> None:
        try:
            if self.__moving_forward == True and self.__current_side <= 3:
                self.__draw_straight_line()
            elif self.__moving_forward == False and self.__current_side <= 3:
                self.__turn_by_degrees()
            else:
                self.destroy_node()
        except Exception as e:
            self.get_logger().error(str(e))

    def __draw_straight_line(self) -> None:
        try:
            self.__mover_msg.angular.z = 0.0
            self.__mover_msg.linear.x = self.__linear_speed
            self.__publisher.publish(self.__mover_msg)
            self.__moving_forward = False
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
    
    def __turn_by_degrees(self) -> None:
        try:
            self.__mover_msg.linear.x = 0.0
            self.__mover_msg.angular.z = self.__turn_speed
            self.__publisher.publish(self.__mover_msg)
            self.__moving_forward = True
            self.__current_side += 1
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
            
def main(args = None):
    try:
        rclpy.init(args = args)
        shapes = TriangleClosedLoop()
        rclpy.spin(shapes)
        rclpy.shutdown()
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()