cmake_minimum_required(VERSION 3.8)
project(navigation)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)


add_executable(nav_logic src/dest_to_motorInfo.cpp)
ament_target_dependencies(nav_logic rclcpp std_msgs)

add_executable(nav_do src/motorInfo_to_GPIO.cpp)
ament_target_dependencies(nav_do rclcpp std_msgs)

install(TARGETS
  nav_logic
  nav_do
  DESTINATION lib/${PROJECT_NAME})



ament_package()
