import rclpy
import threading

from rclpy.node import Node
from std_msgs.msg import Float32
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from ublox_msgs.msg import NavPVT
from rclpy.qos import QoSProfile
from sensor_msgs.msg import NavSatFix
class heading_node(Node):
    def __init__(self):
        super().__init__('gps_processing_node')
        qos = QoSProfile(depth=10)
        self.create_subscription(NavSatFix, 'ublox_gps_node/fix', self.gps_callback, 10, callback_group=ReentrantCallbackGroup())

        self.executor_ = MultiThreadedExecutor(num_threads=4)
        self.executor_.add_node(self)
        self.spin_thread = threading.Thread(target=self.spin)
        self.spin_thread.start()

        self.is_ready = False
        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0

    def gps_callback(self, msg):
        self.lat = msg.latitude
        self.lon = msg.longitude
        self.alt = msg.altitude
        self.is_ready = True
        
        # print("lat: ", self.lat)
        # print("lon: ", self.lon)
        # print("alt: ", self.alt)
    def spin(self):
        try:
            while rclpy.ok():
                rclpy.spin_once(self, timeout_sec=0.1)
        except KeyboardInterrupt:
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = heading_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
