'''
Draw a square, triangle and a 5 pointer star in a sequence.
This is done in open loop, so no position feedback is required.
'''
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
import math
import time

class ShapeSequence(Node):
    def __init__(self)-> None:
        try:
            super().__init__("shape_sequence")
            
            self.__mover_msg = Twist()
            self.__mover_msg.linear.x = 0.0 # set the linear velocity to 0
            self.__mover_msg.angular.z = 0.0 # set the angular velocity to 0
            
            self.__speed = 1.0
            self.__side_length = 2.0  # Length of each side of the square (meters)
            
            self.__turn_angle = math.radians(90) # Turn angle (radians)
            self.__turn_speed = self.__turn_angle
            self.__turn_duration = (self.__turn_angle / self.__turn_speed) * 1e9
            
            # Initialize state variables
            self.__current_side = 1
            self.__moving_forward = True
            self.__moving_time = (self.__side_length / self.__speed)
                                
            self.__publisher = None
            self.__start_time = self.get_clock().now()

            self.__init_pub()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __init_pub(self) -> None:
        try:
            self.__publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
            self.create_timer(0.1, self.__draw_shapes)
        except Exception as e:
            self.get_logger.error(str(e))
    
    def __draw_shapes(self) -> None:
        try:     
            self.__draw_square()
            self.__clear_screen()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __draw_square(self):
        try:
            if self.__moving_forward == True and self.__current_side <= 4:
                self.__draw_straight_line()
            elif self.__moving_forward == False and self.__current_side <= 4:
                self.__turn_by_degrees()
            else:
                self.destroy_node()
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __draw_straight_line(self) -> None:
        try:
            elapsed_time = (self.get_clock().now() - self.__start_time).to_msg()
            if elapsed_time.sec < self.__moving_time:
                self.__mover_msg.linear.x = self.__speed
                self.__publisher.publish(self.__mover_msg)
            else:
                # Stop moving forward
                self.__mover_msg.linear.x = 0.0
                self.__publisher.publish(self.__mover_msg)
                self.__start_time = self.get_clock().now()
                self.__moving_forward = False
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
    
    def __turn_by_degrees(self) -> None:
        try:
            elapsed_time = (self.get_clock().now() - self.__start_time).to_msg()
            elapsed_time_ns = elapsed_time.sec * 1e9
            if elapsed_time_ns < self.__turn_duration:
                self.__mover_msg.angular.z = self.__turn_speed
                self.__publisher.publish(self.__mover_msg)
            else:
                # Stop turning
                self.__mover_msg.angular.z = 0.0
                self.__publisher.publish(self.__mover_msg)
                self.__start_time = self.get_clock().now()
                self.__moving_forward = True
                self.__current_side += 1
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
            
    def __clear_screen(self) -> None:
        try:
            pass
        except Exception as e:
            self.get_logger().error(str(e))
            
def main(args = None):
    try:
        rclpy.init(args = args)
        shapes = ShapeSequence()
        rclpy.spin(shapes)
        rclpy.shutdown()
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()
