# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/parallels/ROS_Workspaces/boat_workspace/src/vision

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/parallels/ROS_Workspaces/boat_workspace/build/vision

# Include any dependencies generated for this target.
include CMakeFiles/camera.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/camera.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/camera.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/camera.dir/flags.make

CMakeFiles/camera.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/camera.dir/cmake_clean.cmake
.PHONY : CMakeFiles/camera.dir/clean

CMakeFiles/camera.dir/depend:
	cd /home/parallels/ROS_Workspaces/boat_workspace/build/vision && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/parallels/ROS_Workspaces/boat_workspace/src/vision /home/parallels/ROS_Workspaces/boat_workspace/src/vision /home/parallels/ROS_Workspaces/boat_workspace/build/vision /home/parallels/ROS_Workspaces/boat_workspace/build/vision /home/parallels/ROS_Workspaces/boat_workspace/build/vision/CMakeFiles/camera.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/camera.dir/depend

