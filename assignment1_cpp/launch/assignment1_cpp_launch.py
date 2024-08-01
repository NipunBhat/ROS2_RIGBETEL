from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='assignment1_cpp',
            executable='temp_pub',
            name='temp_pub'
        ),
        Node(
            package='assignment1_cpp',
            executable='temp_analysis',
            name='temp_analysis'
        ),
        Node(
            package='assignment1',
            executable='status_sub',
            name='status_sub',
        )
    ])