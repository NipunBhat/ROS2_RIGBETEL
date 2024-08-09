#!/usr/bin/env python3
'''
Draw a square, triangle and a 5 pointer star in a sequence.
This is done in open loop, position feedback is collect
'''
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
from turtlesim.msg import Pose
import math
import time

class ShapeSequence(Node):
    def __init__(self)-> None:
        try:
            super().__init__("square_closed_loop")
            
            self.__mover_msg = Twist()
            self.__mover_msg.linear.x = 0.0 # set the linear velocity to 0
            self.__mover_msg.angular.z = 0.0 # set the angular velocity to 0
            
            self.__linear_speed = 2.0
            self.__turn_angle = math.radians(90) # Turn angle (radians)
            self.__turn_speed = self.__turn_angle
            
            # Initialize state variables
            self.__current_side = 1
            self.__moving_forward = True
                                
            self.__publisher = None
            self.__subscriber = None
            self.__start_time = self.get_clock().now()
            
            self.__prev_x = None
            self.__prev_y = None
            self.__prev_theta = None
            
            self.__init_sub() #
            self.__init_pub()
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __init_sub(self)-> None:
        try:
            self.__subscriber = self.create_subscription(Pose, "/turtle1/pose",  self.__logMovement, 10,)
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __init_feedback_vals(self, movement_feedback : Pose) -> None:
        try:
            if self.__prev_x == None: #TODO Is none the best way to check?? not wrong, but not vey nice either
                self.__prev_x = movement_feedback.x
                self.get_logger().info(f"X Starting Point = {self.__prev_x}")
            if self.__prev_y == None:
                self.__prev_y = movement_feedback.y
                self.get_logger().info(f"Y Starting Point = {self.__prev_y}")
            if self.__prev_theta == None:
                self.__prev_theta = movement_feedback.theta
                self.get_logger().info(f"Theta Starting = {math.degrees(self.__prev_theta)}")
        except Exception as e:
            self.get_logger().error(e)

    def __logMovement(self, movement_feedback : Pose) -> None:
        try:
            self.__init_feedback_vals(movement_feedback) #TODO Keep a flag to track if the vals are already initialized, save some time
            self.get_logger().info(f"X Prev: {self.__prev_x}, X Current: {movement_feedback.x}, X Delta: {movement_feedback.x - self.__prev_x}")
            self.__prev_x = movement_feedback.x
            self.get_logger().info(f"Y Prev: {self.__prev_y}, YCurrent: {movement_feedback.y}, Y Delta: {movement_feedback.y - self.__prev_y}")
            self.__prev_y = movement_feedback.y
            self.get_logger().info(f"Theta Prev: {math.degrees(self.__prev_theta)}, Theta Current: {math.degrees(movement_feedback.theta)}, Theta Delta: {math.degrees(movement_feedback.theta) - math.degrees(self.__prev_y)}")
            self.__prev_theta = movement_feedback.theta
        except Exception as e:
            self.get_logger().error(e)
            
    def __init_pub(self) -> None:
        try:
            self.__publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
            time.sleep(1.5)
            self.create_timer(1.01, self.__draw_shapes)
        except Exception as e:
            self.get_logger.error(str(e))
    
    def __draw_shapes(self) -> None:
        try:     
            self.__draw_square()
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
            self.get_logger().info("Moving Forward")
            self.__mover_msg.angular.z = 0.0
            self.__mover_msg.linear.x = self.__linear_speed
            self.__publisher.publish(self.__mover_msg)
            self.__moving_forward = False
            self.get_logger().info("Moving Fowrard Stopped")
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
    
    def __turn_by_degrees(self) -> None:
        try:
            self.get_logger().info("Turing")
            self.__mover_msg.linear.x = 0.0
            self.__mover_msg.angular.z = self.__turn_speed
            self.__publisher.publish(self.__mover_msg)
            self.__moving_forward = True
            self.__current_side += 1
            self.get_logger().info("Turing Stopped")
        except Exception as e:
            self.get_logger().error(str(e))
            self.destroy_node()
            
            
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
