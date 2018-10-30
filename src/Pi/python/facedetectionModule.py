#!/usr/bin/env python3
import rospy
import teensyCommunicator
from facedetection_coordinates.msg import Coordinates

# TODO: according to the known face let the ears light in diefferent colors
# TODO: test with a dumy talker until second Robofriend is operational 

def callback (data):
    rospy.loginfo("y_top: " + str(data.y_top))
    rospy.loginfo("right: " + str(data.right))
    rospy.loginfo("bottom: " + str(data.bottom))
    rospy.loginfo("x_left: " + str(data.x_left))
    coordin = {"y" : data.y_top, "x_w" : data.right, "y_h" : data.bottom, "x" : data.x_left}
    centre_face(coordin)
    resize_face(coordin)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("face_cordinates_topic", Coordinates, callback)

    rospy.spin()

def centre_face(coordinates):
    if (coordinates["x"] < 160):
        #move left
        teensyCommunicator.moveLeftStep()
    elif(coordinates["x"] > 160):
        #move right
        teensyCommunicator.moveRightStep()
    else:
        return

def resize_face(coordinates):
    if (coordinates["x_w"] - coordinates["x"] < 100):   # TODO: check if parameters for ForwardStep and BackwardStep are ok
        # move forward
        teensyCommunicator.moveForwardStep()
    elif(coordinates["x_w"] - coordinates["x"] > 160):
        # move backward
        teensyCommunicator.moveBackStep()
    else:
        return
