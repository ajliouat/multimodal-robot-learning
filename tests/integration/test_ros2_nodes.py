import rclpy
from src.robotics.ros2_nodes.vision_node import VisionNode

def test_vision_node():
    rclpy.init()
    node = VisionNode()
    assert node is not None
    rclpy.shutdown()

if __name__ == "__main__":
    test_vision_node()