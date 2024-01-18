import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='data_processing',
            executable='gps_processing',
            namespace='processing',
            output='screen'
            ),
        ])