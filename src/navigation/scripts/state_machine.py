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

def get_speeds(point):
  # step 1, set the STATE variblae according to the memory:

  memoryArray = []
  with open('myfile.txt', 'r') as f:
    # Read all the lines into a list
    lines = f.readlines()
  for line in line:
    words = line.split()
    memoryArray.append(words[-1])
  
  # memoryArray should now hold 3 things: 
  # memoryArray = [STATE, NONE, PICKUP]
  # the first thing is what state it is in
  # the second thing is how many frames it has seen no net
  # the third thing is how many frames it has been picking up a net

  state = memoryArray[0]

  
  # -1 indicates no net was found
  if point.z = -1:
    no_net = True
  else:
    no_net = False
    x_pos = point.x
    y_pos = point.y

  
  

  
  # step 2, enter the state machine and update it according to the point

  # STATE MACHINE: 

  # Searching: 
    # if it is searching and it detects NO point, update the memory and
    # write to the motors to keep going in a circle

  # Move: 
    # if it is moving and it detects NO point, assume it just missed a frame
    # and keep moving. still update the memory. Actually, check the memory and
    # see if the new NO POINT dictates that it should be in searching mode
    # if it does detect a point, determine if we should move the bot straight or 
    # if should rotate it. Also, if net is close enough, move to the PICKUP state

  # Pickup: 
    # if it is in this state, update a memory saying how many frames it has been picking up
    # if it has been picking it up for enough frames (maybe 100) assume the item is picked up
    # and enter the searching state. Otherwise, go fuck urself hahaha but srsly otherwise keep 
    # moving the belt motors. keep writing STOP to the 

    if state == "SEARCHING":

      if no_net:
        # we still have not found a net
        new_none = int(memoryArray[1]) + 1
        # keep spinning and update the memory with the new NONE value

      else:
        # we found the NET!
        # move according to the move logic
        # update the memory NONE as 0
        # update the state to MOVE

      print("searching logic")

    elif state == "MOVE":

      if no_net:
        # assume we are only here because we missed a frame
        # dont write anyhting to the motors, use the last value
      else:
        # move according to the move logic

      print("move logic")

    elif state == "PICKUP":

      if memoryArray[2] < 100: 
        # keep picking up! write to sim motors!
        newPickup = int(memoryArray[2]) + 1
        # also wite the newPickup to the memory file
      else:
        # we have been running this for 10 seconds. 
        # stop the sim motors and go to the searching state

      print("pickup logic")


def main(args=None):
   rclpy.init(args=args)
   publisher = state_machine()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()