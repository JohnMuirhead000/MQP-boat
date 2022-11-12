cmake_minimum_required(VERSION 3.8)
project(vision)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)


# 
add_executable(cam_driver src/world_to_img.cpp)
ament_target_dependencies(cam_driver rclcpp std_msgs)

add_executable(cam_logic src/img_to_destination.cpp)
ament_target_dependencies(cam_logic rclcpp std_msgs)

install(TARGETS
  cam_driver
  cam_logic
  DESTINATION lib/${PROJECT_NAME})



ament_package()
