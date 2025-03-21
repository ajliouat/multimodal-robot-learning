import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from src.core.vision_language.segmenter import Segmenter

class VisionNode(Node):
    def __init__(self):
        super().__init__("vision_node")
        self.bridge = CvBridge()
        self.segmenter = Segmenter()
        self.subscription = self.create_subscription(Image, "camera/image", self.callback, 10)

    def callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        masks = self.segmenter.segment(cv_image)
        self.get_logger().info(f"Segmented {len(masks)} objects")

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()