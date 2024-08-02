#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='assignment1',
            executable='NODE1',
            name='NODE1'
        ),
        Node(
            package='assignment1',
            executable='NODE2',
            name='NODE2'
        ),
        Node(
            package='assignment1',
            executable='NODE3',
            name='NODE3',
        )
    ])