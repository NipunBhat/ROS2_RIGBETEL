'''
Draw a square, triangle and a 5 pointer star in a sequence.
This is done in open loop, so no position feedback is required.
'''
import rclpy
from rclpy import Node
from geometry_msgs.msg import Twist, Vector3

class ShapeSequence(Node):
    def __init__(self)-> None:
        try:
            super().__init__("shape_sequence")
            self.__publisher = None
            self.__init_pub()
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __init_pub(self) -> None:
        try:
            self.__publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10, self.__draw_shapes)
            self.create_timer(0.5, self.__draw_shapes)
        except Exception as e:
            self.get_logger(str(e))
    
    def __draw_shapes(self) -> None:
        try:
            self.get_logger().info("Started drawing square")
            self.__draw_square()
            self.__clear_screen()
            self.get_logger().info("Square drawn successfully")
            
            self.get_logger().info("Started drawing traingle")
            self.__draw_triangle()
            self.__clear_screen()
            self.get_logger().info("Triangle drawn successfully")
            
            self.get_logger().info("Started drawing star")
            self.__draw_star()
            self._clear_screen()
            self.get_logger().info("Star drawn successfully")
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __draw_square(self):
        try:
            pass
        except Exception as e:
            self.get_logger().error(str(e))
            
    def __draw_triangle(self):
        try:
            pass
        except Exception as e:
            self.get_logger().error(str(e))
    
    def __draw_star(self):
        try:
            pass
        except Exception as e:
            self.get_logger().error(str(e))
