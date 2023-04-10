#!/bin/bash
colcon build
. install/setup.bash
ros2 run vision camera.py & 
ros2 run vision net_finder.py &
ros2 run navigation state_machine.py
ros2 run navigation motor_action.py