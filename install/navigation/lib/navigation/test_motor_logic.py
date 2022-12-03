#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout

#MAX_SPEED 100

class moto_logic(Node):
  def __init__(self):
    
    super().__init__('camera')
    self.publusher = self.create_publisher(Point, 'destination_coords', 10)

    while True:
        x_pos = float(input("Trash X: "))
        y_pos = float(input("Trash Y: "))

        point = Point()
        point.z = float(0)
        point.x = x_pos
        point.y = y_pos

        self.publusher.publish(point)

  
    
def main(args=None):
   rclpy.init(args=args)
   publisher = moto_logic()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()