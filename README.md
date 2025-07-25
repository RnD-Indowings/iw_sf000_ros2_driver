# SF000 ROS 2 Driver

A ROS 2 driver package for the **Lightware SF000 Series** LiDAR sensor, developed and maintained by [Indowings R&D].

This driver enables integration of the SF000 LiDAR sensor with ROS 2-based robotics systems for reliable and real-time distance measurement.

---

## 📦 Package Overview

- **Sensor**: Lightware SF000 Series
- **ROS 2 Compatibility**: Humble
- **Communication**: Serial / UART     -For I2C, specific code is mentioned in a different python file
- **Message Type**: `sensor_msgs/Range`
- **Node Name**: `sf000_lidar_node`

---

## 🛠️ Installation | Building | Running 

### 1. Clone into your ROS 2 workspace

```bash
cd ~/your_ros2_ws/src
git clone git@github.com:RnD-Indowings/iw_sf000_ros2_driver.git

OR you can directly clone down the ws!
```

### 2. Build the workspace
```bash
cd ~/your_ros2_ws
colcon build 
source install/setup.bash
```

### 3. Run the node
```bash
ros2 run sf000_lidar sf000_driver

```

🧪 Test
```bash
Use rqt_graph or ros2 topic echo to visualize data:

ros2 topic echo /sf000/range
```



🔌 Manual Testing with I2C in RPI5
```bash
Run:
"python3 i2c_connection_rpi.py"

Steps:
sudo raspi-config
Path: Interfacing Options -> I2C -> Enable
sudo reboot
sudo apt install i2c-tools
i2cdetect -y 1    #--detection of registers
i2cget -y 1 0x66 0x00 w   #-- raw data
i2cdump -y 1 0x66  #--i2c dump 

**pySerial should be installed -- i2c should be enabled through raspi-config -- **

FOR this Lidar:(When you read multi-byte data (like a 16-bit distance value) from an I2C device, the order in which the bytes are sent matters. This is called Endianness)

If the device returns big-endian data, you must combine bytes accordingly:
dist_cm = (data[0] << 8) + data[1]  # MSB first (big-endian)

If little-endian, it would be:
dist_cm = (data[1] << 8) + data[0]  # LSB first

Mismatch in endianness = incorrect distance values.
```


👨‍💻 Maintainer
```bash
Udit Ray
Email: udit.ray@indowings.com
Org: Indo Wings Private Limited
Website: https://www.indowings.com
```

📄 License
```bash
This project is licensed under the MIT License.
```
