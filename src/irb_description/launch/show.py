from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os 
# from irb_description.launch.load_irb140 import get_state_publisher_node

def generate_launch_description(): 

    return LaunchDescription([
        get_state_publisher_node() , 
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher'
        ),
         Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package="rviz2", 
            executable="rviz2",
            name="rviz",
            arguments=["-d", os.path.join(get_package_share_directory('irb_description'), 'config', 'simple_robot.rviz')]
        )
    ])

def get_state_publisher_node():
    bringup_dir = get_package_share_directory('irb_description')
    urdf_path = os.path.join(bringup_dir, 'urdf', 'irb140.urdf')
    urdf = open(urdf_path).read()
    node = Node(
                name='robot_state_publisher',
                package='robot_state_publisher',
                executable='robot_state_publisher',
                parameters=[{'robot_description': urdf}],
        )

    return node
