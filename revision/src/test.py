#!/usr/bin/env python
import rospy
from std_msgs.msg import String,Int32

rospy.init_node('test', anonymous=True)

dil=rospy.Publisher("Node",String,queue_size=10)
a="sdvmdklvnv"
def dils(msg):
	print(msg.data)
rospy.Subscriber("Node",String,dils)
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():	
		dil.publish(a)		
    except rospy.ROSInterruptException:
        pass
