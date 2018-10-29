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



class Information_uses:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        self.manipulator = moveit_commander.MoveGroupCommander('manipulator')
        self.end_effector_link = self.manipulator.get_end_effector_link()
        self.reference_frame = 'base_link'
        self.manipulator.set_pose_reference_frame(self.reference_frame)
        self.manipulator.allow_replanning(True)
        self.manipulator.set_goal_position_tolerance(0.01)
        self.manipulator.set_goal_orientation_tolerance(0.05)



    def movej_target(self, pose_target):
        self.manipulator.set_pose_target(pose_target, self.end_effector_link)
        self.manipulator.go()
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)        


    def movej_targets(self):
        pass        

    def movel_target(self):
        pass        

    def movel_targets(self):
        pass        

    def movep_target(self):
        pass        

    def movep_targets(self, lists_poses_target):
        fraction = 0.0
        maxtries = 100
        attempts = 0

        poses_target = Tools.lists_to_poses(lists_poses_target)
        print poses_target

        # Plan the Cartesian path connecting the waypoints
        while fraction < 1.0 and attempts < maxtries:
            (plan, fraction) = self.manipulator.compute_cartesian_path (
                                    poses_target,   # waypoint poses
                                    0.01,        # eef_step
                                    0.0,         # jump_threshold
                                    True)        # avoid_collisions
            attempts += 1
            if attempts % 10 == 0:
                rospy.loginfo("Still trying after " + str(attempts) + " attempts...")

        if fraction == 1.0:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            self.manipulator.execute(plan)
            rospy.loginfo("Path execution complete.")
        else:
            rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(maxtries) + " attempts.")  
        # moveit_commander.roscpp_shutdown()
        # moveit_commander.os._exit(0)       

if __name__ == "__main__":
    rospy.init_node('demo_information_uses')
    information_uses = Information_uses()

    demo_list_pose_target1 = [0.3, 0.5, 0.6, 0, 0, 0, 1]
    demo_list_pose_target2 = [0.4, 0.5, 0.5, 0, 0, 0, 1]
    demo_list_pose_target3 = [0.5, 0.5, 0.6, 0, 0, 0, 1]
    demo_lists_poses_target = [demo_list_pose_target1, demo_list_pose_target2, demo_list_pose_target3]

    # information_uses.movej_target(demo_list_pose_target1)
    information_uses.movep_targets(demo_lists_poses_target)    
