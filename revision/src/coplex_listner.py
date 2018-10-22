#!/usr/bin/env python
import rospy
from revision.msg import Complex_dil

rospy.init_node('Complex_listener', anonymous=True)

def callComplex(data):
	a=data.real
	b=data.imaginary
	print "real: ",a
	print "imaginary: ",b
	

def complex_listner():

	rospy.Subscriber("Complex_Sender", Complex_dil, callComplex)

if __name__ == '__main__':
    try:
        complex_listner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
