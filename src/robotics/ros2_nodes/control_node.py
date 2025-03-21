import rclpy
from rclpy.node import Node

class ControlNode(Node):
    def __init__(self):
        super().__init__("control_node")
        self.get_logger().info("Control node started")

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()