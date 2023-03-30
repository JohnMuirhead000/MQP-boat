#!/bin/bash
colcon build
. install/setup.bash
x-terminal-emulator -e ros2 run vision camera_spoofer.py ; x-terminal-emulator -e ros2 run vision net_finder.py
