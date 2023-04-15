cmake_minimum_required(VERSION 3.8)
project(navigation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)


ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  scripts/motor_action.py
  scripts/motor_logic.py
  scripts/state_machine.py
  scripts/remote_control.py
  scripts/test_motor_logic.py
  scripts/test_motor_action.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
