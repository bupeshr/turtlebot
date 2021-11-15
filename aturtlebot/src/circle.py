#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist


class circle():
	def __init__(self):
		rospy.init_node('circle_node', anonymous=False)	
		rospy.loginfo("Let's make a circle Bupesh")	

		self.vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	
		rate = rospy.Rate(10)

		for i in range(0, 130):
		#for top zero
			top = Twist()
			rospy.loginfo("Circle initiated BOSS")
			top.linear.x = 0.2
			top.linear.y = 0.0
			top.linear.z = 0.00
			top.angular.z= 0.5
			self.vel.publish(top)

			rate.sleep()

		for i in range(1):
			rospy.loginfo("circle shape completed Bro!")
			top.linear.x = 0.0
			top.angular.z= 0.0
			self.vel.publish(top)
			
			rate.sleep()



 
if __name__ == '__main__':
	circle()

