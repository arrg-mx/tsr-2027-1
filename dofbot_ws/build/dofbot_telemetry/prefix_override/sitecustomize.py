import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/arrgusr/ROS2Dev/tsr-2027-1/dofbot_ws/install/dofbot_telemetry'
