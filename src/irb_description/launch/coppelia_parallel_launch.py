from launch import LaunchDescription
from launch import InvalidLaunchFileError
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os 


def generate_launch_description(): 
    """
        Check: https://answers.ros.org/question/306935/ros2-include-a-launch-file-from-a-launch-file/
    """
    irb_sim_path = None
    _simulation_pkg = 'irb_sim'
    
    # Check if irb_sim package exists 
    try: 
        irb_sim_path = get_package_share_directory(_simulation_pkg)
        
    except: 
        raise InvalidLaunchFileError("There is no %s package found. Try to source the ros env!" % (_simulation_pkg))
    
    # Include the imported launch file
    coppelia_simple_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
                os.path.join(irb_sim_path, "launch", "coppelia_kinematics_launch.py")
                )
    )

    state_publisher_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('irb_description'), "launch", "state_publisher_launch.py")
        )
    )
    

    return LaunchDescription([coppelia_simple_launch, state_publisher_launch])