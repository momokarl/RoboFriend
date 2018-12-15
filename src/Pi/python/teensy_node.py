import rospy
import TeensyDataHandler
import threading

#import ros service
from ros_robofriend.srv import BatInfData

def node_start():
    print("[INFO] ROS Teensy Communicator Node started")

    try:
        teensy_serial = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
        print("[INFO] Serial for Teensy opened!")
    except:
        print("[INFO] Serial for Teensy could not opened!")
        serial = None

    teensy_handler = TeensyDataHandler.TeensyDataHandler(serial)

    # declare service
    serv = rospy.Service('S_BAT_INF_DATA', BatInfData, teensy_handler.service_handler)

    #TODO: Publisher for motornode is needed