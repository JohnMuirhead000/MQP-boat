#!/usr/bin/env python3
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout

class state_machine(Node):
  def __init__(self):
    
    super().__init__('state_machine')
    self.sub = self.create_subscription(Point, '/ball_point', self.get_speeds, 10)

def main(args=None):
   rclpy.init(args=args)
   publisher = state_machine()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()