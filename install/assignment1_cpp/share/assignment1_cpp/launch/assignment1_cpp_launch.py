from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='assignment1_cpp',
            executable='NODE1',
            name='NODE1'
        ),
        Node(
            package='assignment1_cpp',
            executable='NODE2',
            name='NODE2'
        ),
        Node(
            package='assignment1_cpp',
            executable='NODE3',
            name='NODE3',
        )
    ])