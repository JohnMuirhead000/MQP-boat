// This node is the camera logic / ai node. It subs to img data and outputs the location of the net it detects

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class camera : public rclcpp::Node
{
public:
  camera()
  : Node("camera")
  {
    
  }
private:

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<camera>());
  rclcpp::shutdown();
  return 0;
}
