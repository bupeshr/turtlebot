## Turtlebot3 Motion in Gazebo

I worked out with Turtlebot3 waffle

**OS:** Ubuntu 20.04 LTS

**Distro:** Noetic

Python3

## Install turtlebot3 for Noetic

Install dependent ROS packages

```
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

Install Turtlebot3 via Debian packages 

```
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
```
Build the pkg by

```
$ cd ~/catkin_ws/
$ catkin build
$ cd ~/catkin_ws/src/
$ source devel/setup.bash
```
Clone repo by 

```
$ git clone https://github.com/bupeshr/turtlebot.git
```

Build and source the pkg by

```
$ cd ~/catkin_ws/
$ catkin build
$ cd ~/catkin_ws/src/
$ source devel/setup.bash
```

Start the Turtlebot simulation in Gazebo with
```
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
The above will launch the turtlebot in empty world where I mostly test my shape nodes

### Move in Square

```
$ rosrun aturtlebot square.py
```
### Move in Circle
```
$ rosrun aturtlebot circle.py
```

### Move in 8 shape

```
$ rosrun aturtlebot eight.py
```

