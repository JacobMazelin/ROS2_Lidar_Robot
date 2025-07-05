import rclpy
from rclpy.node import Node
from lidar_bot.drivebase import DriveBase
from geometry_msgs.msg import Twist


class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_to_pwm_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.drivebase = DriveBase()

    def cmd_to_pwm_callback(self, msg):
        right_wheel_vel = (msg.linear.x + msg.angular.z) * 0.5
        left_wheel_vel =  (msg.linear.x - msg.angular.z) * 0.5
        
        print(f"Right wheel velocity: {right_wheel_vel}, Left wheel velocity: {left_wheel_vel}")
        self.drivebase.move(left_wheel_vel, right_wheel_vel)

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()