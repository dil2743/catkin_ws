#! /user/bin python
import rospy
import random
from rosserial_arduino.msg import Adc

def callback(data):
    print data
    print "exit"

rospy.init_node('arduino_ADC',anonymous='false')

def subscrib():
    rospy.Subscriber('adc',Adc,callback)
        
while not rospy.is_shutdown():
    subscrib()
    rospy.sleep(.1)
    
