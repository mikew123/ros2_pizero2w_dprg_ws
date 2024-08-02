import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from gpiozero import DistanceSensor

class Hcsr04dNode(Node):
    """
    A node with HC-SR04 distance sensor and publisher
    trigger from GPIO12 (must be PWM capable)
    echo to GPIO6 (must have 1:2 res divider to reduce 5V to 3.3V)
    """

    hcsr04_rateHz = 4.0

    def __init__(self):
        super().__init__('hcsr04_node')
        
        self.hcsr04 = DistanceSensor(echo=6, trigger=12, threshold_distance=0.99, queue_len=4)
        self.hcsr04_pub = self.create_publisher(Float32, 'hcsr04_msg', 10)
        self.timer = self.create_timer((1/self.hcsr04_rateHz), self.timer_callback)
        
        self.get_logger().info("hcsr04_node started")

    def timer_callback(self):
        #self.get_logger().info("hcsr04_node timer")
        distance = self.hcsr04.distance # meters
        msg = Float32()
        msg.data = distance
        self.hcsr04_pub.publish(msg)
        self.get_logger().info(f"{distance=}m")

def main(args=None):

    rclpy.init(args=args)
    
    node = Hcsr04dNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    # Runs a listener node when this script is run directly (not through an entrypoint)
    main()
