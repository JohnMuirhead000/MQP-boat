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


import rclpy # Python library for ROS
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class CamPub(Node):
  def __init__(self):

    
    super().__init__('camera_net')
    self.pub = self.create_publisher(Image, 'video_frames', 10)
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

    
  def timer_callback(self):
    cap = cv2.VideoCapture(2)
     # Used to convert between ROS and OpenCV images
    br = CvBridge()
    counter = 0
    while counter < 50:
      ret, frame = cap.read()
      counter = counter + 1
    if ret == True:
        # Print debugging information to the terminal
        # Publish the image.
        # The 'cv2_to_imgmsg' method converts an OpenCV
        # image to a ROS image message
        print("sending over image")
        self.pub.publish(br.cv2_to_imgmsg(frame))

def main(args=None):
   rclpy.init(args=args)
   publisher = CamPub()
   rclpy.spin(publisher)
   publisher.destroy_node()
   rclpy.shutdown

         
if __name__ == '__main__':
    main()