# Assignment 2

The following procedure was followed:
- A custom model named `custom_model` was created with specification in `model.sdf`.
- A `demo_world.world` world file was created. All the requirements of part (a) where added to it.
- The `demo.launch` file was created as specified in part (b).
- `demo_description` package was created to keep all the files related to robot separate from simulation.
- The files `demo.xacro`, `gazebo.xacro`, `materials.xacro` and `transmissions.xacro` were added to describe the model and its plugins.
- A `rviz.config` file was added to store rviz configuration.
- `demo_control` package was created to store the configuration file for the differential drive controller package in ROS.
- The `teleop_twist_keyboard` package is used for moving the robot.

Video link: https://youtu.be/IVxKLhyHCWo

# Assignment 3

The following procedure was followed:
- The `demo.xacro` file was updated to add links for the requisite sensors.
- `gazebo.xacro` was updated to add the requisite sensor plugins.
- Displays where added to `rviz` to visualise sensor outputs and the congiguration was saved.
- Added the gmapping node in the launch file with appropriate laser scan topic.
- Moved the robot enough to generate a reasonable map and saved the image using `map_server`.

Video link: https://youtu.be/Ku02XGi6bl0

## Running the package

1. Make sure you have sourced the setup file of ROS:
```source /opt/ros/noetic/setup.bash```
2. Open the terminal in the directory containing this README.
3. Run `catkin_make` to build the required files. This also initialises the directory as a catkin workspace.
4. Source the setup file for the workspace by `source ./devel/setup.bash`.
5. Run the simulation by `roslaunch demo_gazebo demo.launch`.
6. To control the robot using teleop, run `roslaunch demo_gazebo demo_teleop.launch` in another terminal.

This launches the gazebo simulation and rviz visualisation of the robot.
