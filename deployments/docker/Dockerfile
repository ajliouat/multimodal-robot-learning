FROM nvidia/cuda:11.8.0-base

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    ros-humble-ros-base \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the project
COPY . /app
WORKDIR /app

# Start ROS2 nodes
CMD ["./scripts/start_ros2_nodes.sh"]