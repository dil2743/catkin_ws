#!/usr/bin/env python
import rospy
from revision.srv import CountWord,CountWordRequest
import sys
rospy.init_node('service_client')
rospy.wait_for_service('word_count')
word_counter = rospy.ServiceProxy('word_count', CountWord)
#the #valued is another way to do the same
#words = ' '.join(sys.argv[1:])
#words= 'dilshad khan is here where are you'
#word_count = word_counter(words)
#print words, '->', word_count.count
request = CountWordRequest('one two three')
count = word_counter(request)
print count
