import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/udit/Lightware_sf000_lidar/install/sf000_lidar'
