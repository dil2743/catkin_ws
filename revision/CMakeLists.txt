cmake_minimum_required(VERSION 2.8.3)
project(revision)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  genmsg
  message_generation
  actionlib
  actionlib_msgs
)


add_message_files(
  FILES
  Complex_dil.msg
)


add_service_files(

FILES
CountWord.srv
)

add_action_files(
DIRECTORY action
FILES
timer.action
)


generate_messages(
DEPENDENCIES
std_msgs
actionlib_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES chapter2_tutorials
#  CATKIN_DEPENDS roscpp std_msgs
#  DEPENDS system_lib
	CATKIN_DEPENDS message_runtime
	actionlib_msgs
)
