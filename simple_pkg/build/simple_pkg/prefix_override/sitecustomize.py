import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nipun/ros2RB_ws/simple_pkg/install/simple_pkg'
