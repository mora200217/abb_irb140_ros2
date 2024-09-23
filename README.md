# abb_irb140_ros2
ROS2 ABB IRB 140 Packages for basic control. Developed by Unviersidad Nacional de Colombia - Bogotá at LABSIR (Laboratorio de sistemas inteligentes robotizados)

### Summary 
This project encapsules all the packages needed for trajectory planning applicacions using the industrial ABB IRB 140 Manipulator. The project runs with **ROS2** Humble distro and contains the following packages. 

- `/irb_description`: URDF and robot vizualization routines.
- `/irb_coppelia`: Configuration for simple simulation launch files using Coppelia with `simROS2` Coppelia Plugin. 
- `/irb_control`: Low level control implementation with ros_control pkgs 
- `/irb_vision`: Computer vision algorithms for robot perception with RGB-D cameras
- `/irb_moveit`: Moveit2 implementation for trajectory planning. 
- `/irb_msgs`: Some custom msgs  

## irb_description 
### Show URDF in Rviz2 
Just launch the `state_publisher_launch.py` file. This will open RVIZ with the custom config. 
```bash
ros2 launch irb_description state_publisher_launch.py
```


If you are are a ros2 newbie: the URDF file is loaded and published via `robot_state_publisher`node to `/robot_description` this will be the topic referenced by rviz2 to display de model. The TF are calculated from `/joint_states` pusblished by the `joint_state_publisher`node, which takes the transforms relationships, to build the geometric model of the robot. 

<img src="https://github.com/mora200217/abb_irb140_ros2/blob/dev/docs/irb_description_rviz_simple_launch_view.png"  alt="rviz2 ABB IRB 140 show"/>






#### Author 
Andrés M. Morales Martínez. Mechatronics engineering and Physics student at UNAL. (amoralesma@unal.edu.co)

