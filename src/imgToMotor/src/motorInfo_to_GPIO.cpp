// This node is the navigation implement node. It subs to a motor response and it uses GPIO Pi library to send signals out for the Arduino

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class nav_implement : public rclcpp::Node
{
public:
  nav_implement()
  : Node("nav_implement"), count_(0)
  {
    
  }
private:

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<nav_implement>());
  rclcpp::shutdown();
  return 0;
}
