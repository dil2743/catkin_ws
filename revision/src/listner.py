#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from revision.msg import Complex_dil
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() +"I heard %s", data.data)
	print "############################i heard",data.data	
rospy.init_node('listener', anonymous=True)

def listener():

    rospy.Subscriber("counter", Int32, callback)

def callComplex(data):
	a=data.real
	b=data.imaginary
	print "real: ",a
	print "imaginary: ",b
	

def complex_listner():

	rospy.Subscriber("Complex_Sender", Complex_dil, callComplex)
rate= rospy.Rate(2)
if __name__ == '__main__':
    try:
        listener()
      
        complex_listner()
        rospy.sleep(2)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
