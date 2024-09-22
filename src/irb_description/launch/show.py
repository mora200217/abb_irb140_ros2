from launch import LaunchDescription
from launch_ros.actions import Node

def generate_description_file(): 
    return LaunchDescription([
        Node(
            package="rviz2", 
            executable="rviz2"
        )
    ])