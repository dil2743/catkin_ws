#!/usr/bin/env python
import rospy
from std_msgs.msg import String,Int32

rospy.init_node('talker', anonymous=True)


pub =rospy.Publisher('counter',Int32,queue_size=1)

count=0;
rate=rospy.Rate(2)
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():	
		pub.publish(count)
		count+=1
		rospy.sleep(2)
    except rospy.ROSInterruptException:
        pass
