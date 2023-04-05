#!/usr/bin/env python3
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout

class moto_logic(Node):
  def __init__(self):
    
    super().__init__('motor_logic')
    self.sub = self.create_subscription(Point, '/net_detect/point', self.get_speeds, 10)
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
    self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)
  


    
  def get_speeds(self, point):

    print("time to process the point ("+ str(point.x) + ", " + str(point.y) + ", " + str(point.z) + ")")

    belt, left, right = self.find_speed(point)

    data = [left, right]

    # make the array for the propellers
    multiArrayLayout = MultiArrayLayout()

    multiArrayDimension  = MultiArrayDimension()
    multiArrayDimension.label = "jump label"
    multiArrayDimension.size = 2
    multiArrayDimension.stride = 0
    list = [multiArrayDimension]

    multiArrayLayout.data_offset = 0
    multiArrayLayout.dim = list

    float32MultiArray = Float32MultiArray()
    float32MultiArray.data = data
    float32MultiArray.layout = multiArrayLayout

    # make the Float32 for the belt 
    belt_value = Float32()
    belt_value.data = belt

    #publiish both
    self.pub_move.publish(float32MultiArray)
    print("JUST Moved Propellers!!")
    self.pub_belt.publish(belt_value)
    print("Just publushed the belt value ")


  def find_speed(self, point):

    # value subject to change based off of additional motor info
    MAX_SPEED = 100
    CAMERA_ANGLE_COVERED = 45.21892841 #assume the camera is covering 45 degrees of aread 
    Y_DEADBAND = 5 #can move foward if it is within 5 degrees of x axis
    SCREEN_WIDTH = 640 # complete guess; absolutly subject to change
    MAX_ANGLE_ERROR = CAMERA_ANGLE_COVERED / 2 # how much can the angle be wrong by 

    # assume the x axis is foward, y axis is sideways and z axis is up
    # assume y = 0 is the middle of the screen. If y == 0, then we just need to travel straight
    # if y is very large we must rotate counterclockwise, otherwise we rotate clockwise

    #assume left most of the screen is 0 and right most is SCREEN_WIDTH; roatation_error will
    # be < 0 if we need to rotate counterclockwise, and > 0 if we need to rotate counter clockwise
    rotation_error = ((point.y - (SCREEN_WIDTH/2))*CAMERA_ANGLE_COVERED) / SCREEN_WIDTH
    print("rotation error = " + str(rotation_error))


    # TODO SOME LOGIC to DETERMINE IF WE ARE CLOSE ENOUGH TO RUN THE NET TO PCIK IT UP
    if False: 
      # run the belt logic
      return 50, 0, 0

    else:
      
      if abs(rotation_error) < Y_DEADBAND:
        # if we find ourselves here, we are free to move striaght
        print("going straight: left motor = " + str(MAX_SPEED) + " right motor = " + str(MAX_SPEED))
        return float(MAX_SPEED), float(MAX_SPEED)
      else:
        left_motor = -(rotation_error / MAX_ANGLE_ERROR) * MAX_SPEED
        right_motor = -(rotation_error / MAX_ANGLE_ERROR) * MAX_SPEED
        print("rotating: left motor = " + str(left_motor) + " right motor = " + str(right_motor))
        return 0, left_motor, right_motor

    
def main(args=None):
   rclpy.init(args=args)
   publisher = moto_logic()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()