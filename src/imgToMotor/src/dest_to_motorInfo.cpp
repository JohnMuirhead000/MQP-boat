// This node is the camera node. It subs to img data and outputs the location of the net it detects

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class dest_to_motor : public rclcpp::Node
{
public:
  dest_to_motor()
  : Node("dest_to_motor")
  {
    
  }
private:

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<dest_to_motor>());
  rclcpp::shutdown();
  return 0;
}