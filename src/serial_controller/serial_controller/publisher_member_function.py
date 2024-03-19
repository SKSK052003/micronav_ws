import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'data_topic', 10)
        self.timer_period = 0.5  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        user_input = input("Enter your message: ")  # Read user input
        msg = String()  # Create a message of type std_msgs/String
        msg.data = user_input  # Set the message data to user input
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
