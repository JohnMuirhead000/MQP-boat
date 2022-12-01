// This node is the camera node. It subs to img data and outputs the location of the net it detects

#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <geometry_msgs/msg/Point.hpp>
#include "rclcpp/rclcpp.hpp"
#include "navigation/msg/motors.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class speed : public rclcpp::Node
{
  public:
    dest_to_motorInfo()
    : Node("speed")
    {
      self.publisher = this->create_publisher<(const navigation::msg::motors)>("motor_speeds", 10);
      self.subscriber = this->create_subscriber<(const geometry_msgs::msg::Point)>("motor_speeds",10, 
      std::bind(&speed::topic_callback, this, _1));
      
    }
  private:
  void topic_callback(const geometry_msgs::msg::Point point)
  {

    # junk data
    motors = Motors()
    motors.left = 0
    motors.right = 0
    motors.collection = 0

    self.publisher.publish(motors)

  }

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<speed>());
  rclcpp::shutdown();
  return 0;
}