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
CMAKE_SOURCE_DIR = /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor

# Include any dependencies generated for this target.
include CMakeFiles/nav_logic.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/nav_logic.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/nav_logic.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/nav_logic.dir/flags.make

CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o: CMakeFiles/nav_logic.dir/flags.make
CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o: /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor/src/dest_to_motorInfo.cpp
CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o: CMakeFiles/nav_logic.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o -MF CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o.d -o CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o -c /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor/src/dest_to_motorInfo.cpp

CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor/src/dest_to_motorInfo.cpp > CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.i

CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor/src/dest_to_motorInfo.cpp -o CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.s

# Object files for target nav_logic
nav_logic_OBJECTS = \
"CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o"

# External object files for target nav_logic
nav_logic_EXTERNAL_OBJECTS =

nav_logic: CMakeFiles/nav_logic.dir/src/dest_to_motorInfo.cpp.o
nav_logic: CMakeFiles/nav_logic.dir/build.make
nav_logic: /opt/ros/humble/lib/librclcpp.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_generator_py.so
nav_logic: /opt/ros/humble/lib/liblibstatistics_collector.so
nav_logic: /opt/ros/humble/lib/librcl.so
nav_logic: /opt/ros/humble/lib/librmw_implementation.so
nav_logic: /opt/ros/humble/lib/libament_index_cpp.so
nav_logic: /opt/ros/humble/lib/librcl_logging_spdlog.so
nav_logic: /opt/ros/humble/lib/librcl_logging_interface.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_generator_py.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/librcl_interfaces__rosidl_generator_c.so
nav_logic: /opt/ros/humble/lib/librcl_yaml_param_parser.so
nav_logic: /opt/ros/humble/lib/libyaml.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_generator_py.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/librosgraph_msgs__rosidl_generator_c.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_generator_py.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/libstatistics_msgs__rosidl_generator_c.so
nav_logic: /opt/ros/humble/lib/libtracetools.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_fastrtps_c.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_fastrtps_cpp.so
nav_logic: /opt/ros/humble/lib/libfastcdr.so.1.0.24
nav_logic: /opt/ros/humble/lib/librmw.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_introspection_cpp.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_introspection_c.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_cpp.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/libstd_msgs__rosidl_generator_c.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_generator_py.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/libbuiltin_interfaces__rosidl_generator_c.so
nav_logic: /opt/ros/humble/lib/librosidl_typesupport_c.so
nav_logic: /opt/ros/humble/lib/librcpputils.so
nav_logic: /opt/ros/humble/lib/librosidl_runtime_c.so
nav_logic: /opt/ros/humble/lib/librcutils.so
nav_logic: /usr/lib/x86_64-linux-gnu/libpython3.10.so
nav_logic: CMakeFiles/nav_logic.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable nav_logic"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/nav_logic.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/nav_logic.dir/build: nav_logic
.PHONY : CMakeFiles/nav_logic.dir/build

CMakeFiles/nav_logic.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/nav_logic.dir/cmake_clean.cmake
.PHONY : CMakeFiles/nav_logic.dir/clean

CMakeFiles/nav_logic.dir/depend:
	cd /home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor /home/parallels/ROS_Workspaces/boat_workspace/src/imgToMotor /home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor /home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor /home/parallels/ROS_Workspaces/boat_workspace/build/imgToMotor/CMakeFiles/nav_logic.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/nav_logic.dir/depend

