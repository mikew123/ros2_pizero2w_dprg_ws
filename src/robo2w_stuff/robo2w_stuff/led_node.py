import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from gpiozero import LED



class LedNode(Node):
    """
    A node with a single subscriber and drives an LED.

    """
    
    def __init__(self):
        super().__init__('led_node')

        self.led = LED(4)

        self.hcsr04_msg_sub = self.create_subscription(Float32, 'hcsr04_msg', self.hcsr04_msg_callback, 10)
        self.timer = self.create_timer((1/4.0), self.timer_callback)

        self.led.on()

        self.get_logger().info("led_node started")

    def hcsr04_msg_callback(self, msg):
        distance = msg.data
        blink_on = (1 - distance)/4
        self.led.blink(blink_on, 0, 1)

        self.get_logger().info(f"{distance=}")

    def timer_callback(self):
        #self.get_logger().info("led_node timer")
        #self.led.toggle()
        #self.led.blink(0.1, 0, 1)
        pass

def main(args=None):

    rclpy.init(args=args)
    
    node = LedNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    # Runs a listener node when this script is run directly (not through an entrypoint)
    main()
