#!/usr/bin/env python3
import rospy
import teensyCommunicator
import ioWarriorModule
from ros_robofriend.msg import CamData
from std_msgs.msg import String

# TODO: according to the known face let the ears light in different colors
# TODO: test with a dummy talker until second Robofriend is operational

def callback (data):
    print("[INFO] Facedetection Listener received callback!")
    rospy.loginfo("top: " + str(data.top))
    rospy.loginfo("right: " + str(data.right))
    rospy.loginfo("bottom: " + str(data.bottom))
    rospy.loginfo("left: " + str(data.left))
    rospy.loginfo("name: " + str(data.name))

    coordin = {"y" : data.top, "x_w" : data.right, "y_h" : data.bottom, "x" : data.left, "name" : data.name}

    centre_face(coordin)
    resize_face(coordin)
    identify_face(coordin)
    
def rfid_data_cb(data):
    print("[INFO] Received rfid date: {}".format(data.data))

def listener():
    print("[INFO] Starting Facedetection Listener!")
#    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("T_CAM_DATA", CamData, callback)
    rospy.Subscriber("T_RFID_DATA", String, rfid_data_cb)
    print("[INFO] Facedetection Listener started!")


def identify_face(coordinates):
    if (coordinates["name"] != "Unknown"):
        print("[INFO] Known Face!")
        ioWarriorModule.sendToIOWarrior(0, 15, 0) #if it's a known face let the ears light in green
    else:
        print("[INFO] Unknown Face!")
        ioWarriorModule.sendToIOWarrior(15, 0, 0) #for a unknown face let the ears light in red

def centre_face(coordinates):
    if (coordinates["x"] < 90):
        #move left
        print("[INFO] x: {}, therefore move left".format(coordinates["x"]))
        teensyCommunicator.moveLeftStep()
    elif(coordinates["x"] > 150):
        #move right
        print("[INFO] x: {}, therefore move right".format(coordinates["x"]))
        teensyCommunicator.moveRightStep()
    else:
        print("[INFO] Face is in the centre")
        return

def resize_face(coordinates):
    if (coordinates["x_w"] - coordinates["x"] < 70):  # TODO: check if parameters for ForwardStep and BackwardStep are ok
        # move forward
        print("[INFO] Move forward / diff of x: {}".format(coordinates["x_w"] - coordinates["x"]))
        teensyCommunicator.moveForwardStep()
    elif(coordinates["x_w"] - coordinates["x"] > 160):
        # move backward
        print("[INFO] Move backward / diff of x: {}".format(coordinates["x_w"] - coordinates["x"]))
        teensyCommunicator.moveBackStep()
    else:
        print("[INFO] In the right distance!")
        return
