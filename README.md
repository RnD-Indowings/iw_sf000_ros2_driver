# SF000 ROS 2 Driver

A ROS 2 driver package for the **Lightware SF000 Series** LiDAR sensor, developed and maintained by [Indowings R&D].

This driver enables integration of the SF000 LiDAR sensor with ROS 2-based robotics systems for reliable and real-time distance measurement.

---

## 📦 Package Overview

- **Sensor**: Lightware SF000 Series
- **ROS 2 Compatibility**: Humble (or specify your distro)
- **Communication**: Serial / UART
- **Message Type**: `sensor_msgs/Range`
- **Node Name**: `sf000_lidar_node`

---

## 🛠️ Installation

### 1. Clone into your ROS 2 workspace

```bash
cd ~/your_ros2_ws/src
git clone git@github.com:RnD-Indowings/sf000_ros2_driver.git

### 2. Build the workspace
cd ~/your_ros2_ws
colcon build --packages-select sf000_ros2_driver
source install/setup.bash


### 3. Run the node
ros2 launch sf000_ros2_driver sf000_lidar_launch.py

🧪 Test

Use rqt_graph or ros2 topic echo to visualize data:

ros2 topic echo /sf000/range


sf000_ros2_driver/
├── launch/
├── src/
├── include/
├── config/
├── CMakeLists.txt
└── package.xml
