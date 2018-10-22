#!/usr/bin/env python
import rospy
from revision.msg import Complex_dil
from random import random
rospy.init_node('Complex_publisher')
pub = rospy.Publisher('Complex_Sender', Complex_dil,queue_size=10)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	msg = Complex_dil()
	msg.real = random()
	msg.imaginary = random()
	pub.publish(msg)
	rate.sleep()
