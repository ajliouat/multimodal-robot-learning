#!/bin/bash

# Start ROS2 nodes
ros2 run multimodal_robot_learning vision_node &
ros2 run multimodal_robot_learning control_node &