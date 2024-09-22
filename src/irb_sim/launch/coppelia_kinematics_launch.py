from launch import LaunchDescription
from launch import actions
from ament_index_python.packages import get_package_share_directory

import os 


def generate_launch_description():
    """
        coppelia_kinematics_launch.py 
        -
        Launc file to open CoppeliaSim with coppelia scenes found in /coppelia folder 
        inside this package (irb_sim). You have to manually add the app_path

        1. For Coppelia instalation, you should already added 'COPPELIASIM_ROOT_DIR'
        environment variable to your system. 
        2. Try to locate where is the app executable according to your working OS.
        Refer to https://manual.coppeliarobotics.com/en/commandLine.htm for more 
        information 

        Note: This example is build for MacOS. but just changing the app_path should 
        work for other OS. (Not tried yet though)

        The sudo pre_command in executeProcess action, is for permission issues. 

        IMPORTANT: Remember to install the simROS2 plugin for your Coppelia version. 

        - Andres 

    """
    current_pkg_dr = get_package_share_directory('irb_sim')
    COPPELIA_PATH = os.environ['COPPELIASIM_ROOT_DIR']  # Env variable from COPPELIA
    
    # Folders location. Check function description 
    scene_path = os.path.join(current_pkg_dr, "coppelia", "irb140.ttt")
    app_path = os.path.join(COPPELIA_PATH, "../MacOS/coppeliaSim")

    return LaunchDescription([
        actions.ExecuteProcess(cmd=["sudo", app_path, scene_path]) # Just open coppelia via CMD with scene
    ])

