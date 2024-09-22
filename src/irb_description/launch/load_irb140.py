
from ament_index_python import get_package_share_directory

import os 
import launch_ros

def get_state_publisher_node():
    bringup_dir = get_package_share_directory('irb_description')
    urdf_path = os.path.join(bringup_dir, 'urdf', 'irb140.urdf')
    urdf = open(urdf_path).read()

    node = launch_ros.actions.Node(
                name='robot_state_publisher',
                package='robot_state_publisher',
                executable='robot_state_publisher',
                parameters=[{'robot_description': urdf}],
        ),

    return node
