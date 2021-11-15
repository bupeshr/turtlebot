#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist


class eight():
	def __init__(self):
		rospy.init_node('eight_node', anonymous=False)	
		rospy.loginfo("Let's make a eight Bupesh")	

		self.vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	
		rate = rospy.Rate(10)

		for i in range(0, 130):
		#for top zero
			top = Twist()
			rospy.loginfo("Top zero initiated")
			top.linear.x = 0.2
			top.linear.y = 0.0
			top.linear.z = 0.00
			top.angular.z= 0.5
			self.vel.publish(top)

			rate.sleep()
		for i in range(0, 123):

			#for bottom zero
			bottom = Twist()
			rospy.loginfo("Bottom zero initiated")
			bottom.linear.x = 0.2
			bottom.angular.z = -0.5
			self.vel.publish(bottom)
			rate.sleep()

		for i in range(1):
			rospy.loginfo("8 shape completed Bro!")
			top.linear.x = 0.0
			top.angular.z= 0.0
			bottom.linear.x = 0.0
			bottom.angular.z = 0.0
			self.vel.publish(top)
			self.vel.publish(bottom)
			rate.sleep()


 
if __name__ == '__main__':
	eight()

