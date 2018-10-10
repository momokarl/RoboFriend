#!/usr/bin/env python3
import rospy
from facedetection_coordinates.msg import Coordinates

def callback (data):
    rospy.loginfo("y_top: " + str(data.y_top))
    rospy.loginfo("right: " + str(data.right))
    rospy.loginfo("bottom: " + str(data.bottom))
    rospy.loginfo("x_left: " + str(data.x_left))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("face_cordinates_topic", Coordinates, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
