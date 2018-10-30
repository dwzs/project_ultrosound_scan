#!/usr/bin/env python

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import String

sys.path.append('/home/wsy/catkin_ws/src/project_ur5/lib')
from tools import Tools



class Information_extraction:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        self.K_pressure = 0.01
        self.manipulator = moveit_commander.MoveGroupCommander('manipulator')
        self.end_effector_link = self.manipulator.get_end_effector_link()
        self.reference_frame = 'base_link'
        self.manipulator.set_pose_reference_frame(self.reference_frame)
        self.manipulator.allow_replanning(True)
        self.manipulator.set_goal_position_tolerance(0.01)
        self.manipulator.set_goal_orientation_tolerance(0.05)



    def adjust_pressure(self, pressure):
        information_adjust = [0, 0, 0, 0, 0, 0, 0]
        information_adjust[2] = pressure * self.K_pressure
        return information_adjust


    def adjust_ultrosound(self):
        pass        

    def path(self):
        pass        




if __name__ == "__main__":
    rospy.init_node('demo_information_extraction')
    information_extraction = Information_extraction()

    demo_sim_pressure = 5
     
    information_adjust_pressure = information_extraction.adjust_pressure(demo_sim_pressure)


    print information_adjust_pressure
