import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from geometry_msgs.msg import Twist

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        #self._last_received = rclpy.get_time()
        self._timeout = 2 #rclpy.get_param('~timeout', 2)
        self._rate = 10 #rclpy.get_param('~rate', 10)
        self._max_speed = 0.5 #rclpy.get_param('~max_speed', 0.5)
        self._wheel_base = 0.91 #rclpy.get_param('~wheel_base', 0.091) 

        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg)

        #self._last_received = rclpy.get_time()

        # From https://snapcraft.io/blog/your-first-robot-the-driver-4-5
        # Extract linear and angular velocities from the message
        linear = msg.linear.x
        angular = msg.angular.z

        # Calculate wheel speeds in m/s
        left_speed = linear - angular*self._wheel_base/2
        right_speed = linear + angular*self._wheel_base/2

        # Ideally we'd now use the desired wheel speeds along
        # with data from wheel speed sensors to come up with the
        # power we need to apply to the wheels, but we don't have
        # wheel speed sensors. Instead, we'll simply convert m/s
        # into percent of maximum wheel speed, which gives us a
        # duty cycle that we can apply to each motor.
        self._left_speed_percent = (100 * left_speed/self._max_speed)
        self._right_speed_percent = (100 * right_speed/self._max_speed)
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
