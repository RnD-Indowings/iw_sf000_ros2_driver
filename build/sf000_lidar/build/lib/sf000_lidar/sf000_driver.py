# sf000_lidar/sf000_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import smbus2

class SF000LidarNode(Node):
    def __init__(self):
        super().__init__('sf000_lidar_node')

        self.bus = smbus2.SMBus(1)
        self.addr = 0x66  # SF000/B I2C address

        self.publisher = self.create_publisher(Range, 'sf000/range', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.frame_id = "sf000_frame"
        self.fov = 0.0349  # radians (~2 degrees)
        self.min_range = 0.01
        self.max_range = 6.0

        self.get_logger().info("SF000 LiDAR I2C Node Started.")

    def timer_callback(self):
        try:
            data = self.bus.read_i2c_block_data(self.addr, 0x00, 2)
            dist_cm = (data[0] << 8) + data[1]
            dist_m = dist_cm / 100.0

            msg = Range()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = self.frame_id
            msg.radiation_type = Range.INFRARED
            msg.field_of_view = self.fov
            msg.min_range = self.min_range
            msg.max_range = self.max_range
            msg.range = dist_m

            self.publisher.publish(msg)
        except Exception as e:
            self.get_logger().error(f"Failed to read SF000: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = SF000LidarNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
