#!/bin/bash
colcon build
. install/setup.bash
ros2 run vision camera.py & 
ros2 run vision net_finder.py &
ros2 run navigation motor_logic.py &
ros2 run navigation motor_action.py