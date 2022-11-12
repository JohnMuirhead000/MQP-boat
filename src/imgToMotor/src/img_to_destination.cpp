// This node is the camera node. It subs to img data and outputs the location of the net it detects

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class img_to_dest : public rclcpp::Node
{
public:
  img_to_dest()
  : Node("img_to_dest"), count_(0)
  {
    
  }
private:

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<img_to_dest>());
  rclcpp::shutdown();
  return 0;
}
