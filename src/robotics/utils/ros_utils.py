import rclpy
from rclpy.node import Node

class ROSUtils:
    @staticmethod
    def init_node(node_name):
        rclpy.init()
        return Node(node_name)