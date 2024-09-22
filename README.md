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


#### Author 
Andrés M. Morales Martínez. Mechatronics engineering and Physics student at UNAL. (amoralesma@unal.edu.co)

