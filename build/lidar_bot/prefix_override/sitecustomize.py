import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jmazelin/ros2_ws/src/ROS2_Lidar_Robot/install/lidar_bot'
