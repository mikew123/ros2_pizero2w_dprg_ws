import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from gpiozero import LED


class LedNode(Node):
    """
    A node with a single subscriber and drives an LED.

    """
    led = LED(4)

    def __init__(self):
        super().__init__('led_node')
        self.led_msg_sub = self.create_subscription(String, 'led_msg', self.led_msg_callback, 10)
        self.timer = self.create_timer((1.0), self.timer_callback)

        self.led.on()

        self.get_logger().info("led_node started")

    def led_msg_callback(self, msg):
        self.get_logger().info('LED msg: "%s"' % msg.data)

    def timer_callback(self):
        self.get_logger().info("led_node timer")
        #self.led.toggle()
        self.led.blink(0.5, 0, 1)

def main(args=None):

    rclpy.init(args=args)
    
    node = LedNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    # Runs a listener node when this script is run directly (not through an entrypoint)
    main()
