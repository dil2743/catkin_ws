#! /user/bin python
import rospy
import random
from std_msgs.msg import Float64 as float32

def callback(data):
    print data.data
    print "exit"

rospy.init_node('arduino',anonymous='false')

def publish():
    pub=rospy.Publisher('your_topic',float32,queue_size=1)
    value=float32()
    value.data=random.random()
    pub.publish(value)
    
def subscrib():
    rospy.Subscriber('my_topic',float32,callback)
        
while not rospy.is_shutdown():
    publish()
    subscrib()
    rospy.sleep(1)
