#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist


class square():
	def __init__(self):
		rospy.init_node('square_node', anonymous=False)	
		rospy.loginfo("Let's make a square Bupesh")	

		self.vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	
		rate = rospy.Rate(10)

		#for straight motion
		front = Twist()
		front.linear.x = 0.2
		front.linear.y = 0.0
		front.linear.z=0.00
		front.angular.z= 0.0

		rate.sleep()

		#for rotation/turning
		rot = Twist()
		rot.linear.x = 0
		rot.angular.z = 0.5
		rate.sleep()


		#while not rospy.is_shutdown():
		for i in range(4):
			print("Going Straight")
			for x in range(0,48):
				self.vel.publish(front)
				rate.sleep()
			print("Turning Left!")
			for x in range(0,31):
				self.vel.publish(rot)
				rate.sleep()

			rate.sleep()
			


 
if __name__ == '__main__':
	square()

