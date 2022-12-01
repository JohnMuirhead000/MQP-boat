// This node is the navigation implement node. It subs to a motor response and it uses GPIO Pi library to send signals out for the Arduino

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class motorInfo_to_GPIO : public rclcpp::Node
{
public:
  motorInfo_to_GPIO()
  : Node("nav_implement")
  {
    
  }
private:

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<motorInfo_to_GPIO>());
  rclcpp::shutdown();
  return 0;
}
