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

class state_machine(Node):
  def __init__(self):
    
    super().__init__('state_machine')
    self.sub = self.create_subscription(Point, '/net_detect/point', self.get_speeds, 10)
    self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)

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

    print("poop")
    
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
      print("in the searching state")
      if no_net:
        print("found no net in the searching state, moving in a circle")
        # we still have not found a net
        no_net_count = int(memoryArray[1]) + 1
        write_memory('SEARCHING', no_net_count, 0)
        self.circle_move()
      else:
        print("found a net in searching state")
        write_memory('MOVE', 0, 0)

    elif state == 'MOVE':

      if no_net:

        print("found no net in the moving state")
        no_net_count = int(memoryArray[1]) + 1

        if no_net_count > 20:
          print("we are moiving, but have not seen a net for 100 frames; back to searching")
          # in here if we have not seen a net for 10 seconds
          write_memory("SEARCHING", no_net_count, 0)
        else:
          print("we are moiving, but have not seen a net, but will assume we just missed a frame")
          # assume we have a net in target but just missed for a frame
          write_memory('MOVE', no_net_count, 0)

      else:
        print("found a net in the move state ")
        no_net_count = int(memoryArray[1]) + 1

        if activate_belt(x_pos, y_pos):
          print("was moving now its time to pick up the NET")
          # if it is time to activate the belt motors
          write_memory('PICKUP', 0, 1)
          # TODO write code to start belt motors. STOP the other motors
        else: 
          print("found a net while moving. Will keep moving")
          write_memory('MOVE', 0, 0)
          speeds = [left_motor, right_motor] = move_logic(x_pos, y_pos)
          # TODO write code to naviagte the bot to the net

    elif state == 'PICKUP':

      if memoryArray[2] < 100: 
        print("still picking up")
        # keep picking up! write to sim motors!
        newPickup = int(memoryArray[2]) + 1
        write_memory("PICKUP", 0, newPickup)
      else:
        print("we have beem picking up for 100 frames")
        write_memory("SEARCHING", 0, 0)
        # we have been running this for 10 seconds. 
        # stop the sim motors and go to the searching state


  def circle_move(self):
    print("cirlce ityme")
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
    float32MultiArray.data = [float(50), float(0)]
    float32MultiArray.layout = multiArrayLayout

    self.pub_move.publish(float32MultiArray)

# this function takes in the x pos and the y pose and detemrines if we are in the correct place to pick up the NET
def activate_belt(x_pos, y_pos):
  print("send code to run the belt")
  # if we are close enough to the net, return True
  # otherwise return false!


# this function assumes a net has been found and assumes we are not using the belt rn
def move_logic(x_pos, y_pos):
  print("send code to move to TRASH")
  return [10, 10]
  # if the belt is within a certian deadband, move foward
  # otherwise turn to the side 


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