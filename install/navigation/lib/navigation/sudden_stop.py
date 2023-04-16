import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import MultiArrayLayout


class sudden_stop(Node):
    def __init__(self):
    
        super().__init__('sudden_stop')
        self.pub_move = self.create_publisher(Float32MultiArray, 'impeler_move', 10)
        self.pub_belt = self.create_publisher(Float32, 'belt_move', 10)

        waiting = input("enter anythign and the robot stops")

        while (True):
            self.send_val(0, 0)
            self.send_to_motor()
    def send_val(self, left, right):

        data = [float(left), float(right)]
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

        #publiish motor stuff
        self.pub_move.publish(float32MultiArray)

    def send_to_motor(self):
        print("power the motor with 0% ")
        float32 = Float32()
        float32.data = float(0)
        self.pub_belt.publish(float32)



def main(args=None):
   rclpy.init(args=args)
   sudden_stop = sudden_stop()
   rclpy.spin(sudden_stop)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()