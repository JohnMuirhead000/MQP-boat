#!/usr/bin/env python3
# Basics ROS program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com

import rclpy # Python library for ROS
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class find_net(Node):
  def __init__(self):

    
    super().__init__('net_finder')
    self.pub = self.create_publisher(Point, 'destination_coords', 10)
    self.sub = self.create_subscription(Image, 'video_frames', self.pub_coords, 10)
    
  def pub_coords(self, msg):
    point = self.perform_ai(msg)
    self.pub.publish(point)

  # takes in an image and returns the point of the object we want
  def perform_ai(self, image):
    point = Point()

    # junk data
    point.x = float(10)
    point.y = float(10)
    point.z = float(10)

    print("returning point")
    return point

def main(args=None):
   rclpy.init(args=args)
   net_node = find_net()
   rclpy.spin(net_node)
   net_node.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()

# // // This node is the camera node. It subs to img data and outputs the location of the net it detects

# // #include <chrono>
# // #include <functional>
# // #include <memory>
# // #include <string>

# // // on the pi, make sure u have installed image stuff  - sudo apt-get install -y ros-sensor-msgs
# // #include <sensor_msgs/Image.h>
# // #include <geometry_msgs/msg/point.hpp>
# // #include "rclcpp/rclcpp.hpp"

# // using namespace std::chrono_literals;

# // /* This example creates a subclass of Node and uses std::bind() to register a
# //  * member function as a callback from the timer. */

# // class NetFinder : public rclcpp::Node
# // {
# //   public:
# //     NetFinder()
# //     : Node("NetFinder")
# //     {
# //       def __init__(self):
# //       super().__init__('NetFinder')
# //       sub = this->create_subscription<sensor_msgs::msg::Image>(
# //         "video_frames", 10, std::bind(&NetFinder::topic_callback, this, _1));

# //       pub = this->create_publisher<geometry_msgs::msg::Point>("coordinates", 10);
      
# //     }
# //   private:
# //   topic_callback(const sensor_msgs::msg::Image: image)
# //   {
# //     point = find_point(image)
# //     pub->publush(point)
# //   }

# //   find_point(sensor_msgs::msg::Image: image)
# //   {
# //     // giveen an image, find the point (look up geometry_msgs/Point.msg) which represents some objects location and return it. 


# //     //default point because who gives a fuck
# //     geometry_msgs::msg::Point point = Point()
# //     point->x = 10;
# //     point->y = 10;
# //     point->z = 10;
# //     return point
# //   }

# // };

# // int main(int argc, char * argv[])
# // {
# //   rclcpp::init(argc, argv);
# //   rclcpp::spin(std::make_shared<NetFinder>());
# //   rclcpp::shutdown();
# //   return 0;
# // }