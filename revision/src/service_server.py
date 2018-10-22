#!/usr/bin/env python
import rospy
from revision.srv import CountWord,CountWordResponse

def count_words(request):

	return CountWordResponse(len(request.words.split()))

rospy.init_node('service_server')

service = rospy.Service('word_count', CountWord, count_words)

rospy.spin()
