#!/usr/bin/env python3
 
# Import the necessary libraries
import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout
import os
import math

LEFT = 0
RIGHT = 640
BOTTOM = 480
TOP = 0

class state_machine(Node):
  def __init__(self):
    
    super().__init__('state_machine')
    self.sub = self.create_subscription(Point, '/net_detect/point', self.get_speeds, 10)
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
    self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)

  def get_speeds(self, point):
    # step 1, set the STATE variblae according to the memory:

    memoryArray = []
    with open('/home/parallels/git/MQP-boat/src/navigation/scripts/memory.txt', 'r') as f:
      # Read all the lines into a list
      lines = f.readlines()
    for line in lines:
      words = line.split()
      memoryArray.append(words[-1])
    
    # memoryArray should now hold 3 things: 
    # memoryArray = [STATE, NONE, PICKUP]
    # the first thing is what state it is in
    # the second thing is how many frames it has seen no net
    # the third thing is how many frames it has been picking up a net

    state = memoryArray[0]

    print("memory array = " + str(memoryArray))
    print("about to enter the machine")

    
    # -1 indicates no net was found
    if point.z == -1:
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


    if state == 'SEARCHING':
      if no_net:
        # we still have not found a net
        no_net_count = int(memoryArray[1]) + 1
        write_memory('SEARCHING', no_net_count, 0)
        self.move_motors(float(50), float(0))
      else:
        write_memory('MOVE', 0, 0)

    elif state == 'MOVE':

      if no_net:

        print("FOUND NO NET")

        no_net_count = int(memoryArray[1]) + 1

        if no_net_count > 20:
          # in here if we have not seen a net for 10 seconds
          write_memory("SEARCHING", no_net_count, 0)
        else:
          # assume we have a net in target but just missed for a frame
          write_memory('MOVE', no_net_count, 0)

      else:
        no_net_count = int(memoryArray[1]) + 1

        if activate_belt(x_pos, y_pos):
          # if it is time to activate the belt motors
          write_memory('PICKUP', 0, 1)

        else: 
          print("FOUND A NET WHILE MOVING")
          write_memory('MOVE', 0, 0)
          print("x_pos = " + str(x_pos))
          print("y_pos = " + str(y_pos))
          [left_motor, right_motor] = move_logic(x_pos, y_pos)
          self.move_motors(left_motor, right_motor)

    elif state == 'PICKUP':

      if int(memoryArray[2]) < 20: 
        # keep picking up! write to sim motors!
        newPickup = int(memoryArray[2]) + 1
        write_memory("PICKUP", 0, newPickup)
        self.move_motors(0, 0)
        self.move_belt(20)
      else:
        write_memory("SEARCHING", 0, 0)
        self.move_belt(0)


  def move_motors(self, left, right):
    #make the array for the propellers
    multiArrayLayout = MultiArrayLayout()

    multiArrayDimension  = MultiArrayDimension()
    multiArrayDimension.label = "jump label"
    multiArrayDimension.size = 2
    multiArrayDimension.stride = 0
    list = [multiArrayDimension]

    multiArrayLayout.data_offset = 0
    multiArrayLayout.dim = list

    float32MultiArray = Float32MultiArray()
    float32MultiArray.data = [float(left), float(right)]
    float32MultiArray.layout = multiArrayLayout

    self.pub_move.publish(float32MultiArray)

  def move_belt(self, speed):
    #make the array for the propellers
    float32 = Float32()
    float32.data = float(speed)
    self.pub_belt.publish(float32)

# this function takes in the x pos and the y pose and detemrines if we are in the correct place to pick up the NET
def activate_belt(x_pos, y_pos):
  return y_pos >= BOTTOM*.9 and x_pos >= RIGHT * .35 and x_pos <= RIGHT * .65


# this function assumes a net has been found and assumes we are not using the belt rn
def move_logic(x_pos, y_pos):

  print("ACTIVATINF MOVE LOGIX")

  # check if we are close
  if y_pos >= BOTTOM * .9:
    print("IN THE CORNER")
    if x_pos < RIGHT * .35:
      # net in bottom left of screen; just move right side 
      return [0, 30]
    if x_pos > RIGHT * .65:
      return [30, 0]
    else:
      # the code should NEVER be here
      return [10, 10]

    # check if we are not close
  else: 

    if in_middle_quad(x_pos, y_pos):
      # are int the middle slice
      y_from_line = abs(y_pos - BOTTOM*.75)
      print("IN THE MIDDLE QUADD")
      max_y = BOTTOM*.9
      return ([int((100*y_from_line) / max_y), int((100*y_from_line) / max_y)])   

    # we are in the left or right quadrat
    orig_x = RIGHT/2
    orig_y = BOTTOM*.9

    x_from_orig = abs(x_pos - orig_x)
    y_from_orig = abs(y_pos - orig_y)

    x_percent_error = int((100 * x_from_orig) / (RIGHT * .5))
    y_percent_error = int((100 * y_from_orig) / (BOTTOM * .9))

    max_distance = math.sqrt(orig_x * orig_x + orig_y * orig_y)

    actual_distance = math.sqrt(x_from_orig * x_from_orig + y_from_orig * y_from_orig)

    percent_distance_error = int((100 * actual_distance) / max_distance)

    if x_pos < RIGHT / 2:


      right_p = x_percent_error * .5  + 50
      left_p = 100 - right_p
      # the motor speeds sum to the percent_distance_error 

      left = (left_p * percent_distance_error) / 100
      right = (right_p * percent_distance_error) / 100

      print("trying to move left; left = " + str(left) + " right = " + str(right))

    elif x_pos > RIGHT / 2:

      left_p = x_percent_error * .5  + 50
      right_p = 100 - left_p
       # the motor speeds sum to the percent_distance_error 

      left = (left_p * percent_distance_error) / 100
      right = (right_p * percent_distance_error) / 100
      print("trying to move right; left = " + str(left) + " right = " + str(right))

      return [left, right]

    else: 
      print("SHOULD NOT BE HERE")
      # we should never be here!
      return [0, 0] 
        
  return [10, 10]
  # if the belt is within a certian deadband, move foward
  # otherwise turn to the side 


def in_middle_quad(x_pos, y_pos):

  reflection_angle = 10
  in_radians = math.radians(reflection_angle)
  print("in randians = " + str(in_radians))

  orig_x = RIGHT/2
  orig_y = BOTTOM*.9

  

  x_from_orig = abs(x_pos - orig_x)
  y_from_orig = abs(y_pos - orig_y)

  print("orig_x = " + str(orig_x) + " orig_y = " + str(orig_y) + " x_from_orig = " + str(x_from_orig) + " y_from_orig = " + str(y_from_orig))


  # will return true if we are the the middle slice!!!
  return x_from_orig <= math.tan(in_radians) * y_from_orig


def write_memory(state, no_nets, pickups):
  os.remove("/home/parallels/git/MQP-boat/src/navigation/scripts/memory.txt")
  # rewrite the memoru for the nect iteration
  with open("/home/parallels/git/MQP-boat/src/navigation/scripts/memory.txt", 'w') as f:
    f.write('STATE = ' + state + '\n')
    f.write('NONE = ' + str(no_nets) + '\n')
    f.write('PICKUP = ' + str(pickups) + '\n')



def main(args=None):
   rclpy.init(args=args)
   publisher = state_machine()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()