#!/usr/bin/env python

import rospy, sys
import moveit_commander
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import Pose
from copy import deepcopy

class MoveItDemo:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('moveit_demo', anonymous=True)
        right_arm = MoveGroupCommander('manipulator')
        right_arm.allow_replanning(True)
        right_arm.set_pose_reference_frame('base_link')
        right_arm.set_goal_position_tolerance(0.01)
        right_arm.set_goal_orientation_tolerance(0.1)
        end_effector_link = right_arm.get_end_effector_link()

        start_pose = right_arm.get_current_pose(end_effector_link).pose
        waypoints = []
        waypoints.append(start_pose)
        wpose = deepcopy(start_pose)
        wpose.position.x -= 0.2
        wpose.position.y -= 0.2
        waypoints.append(deepcopy(wpose))
        wpose.position.x += 0.05
        wpose.position.y += 0.15
        wpose.position.z -= 0.15
        waypoints.append(deepcopy(wpose))
        waypoints.append(deepcopy(start_pose))

        fraction = 0.0
        maxtries = 100
        attempts = 0
        while fraction < 1.0 and attempts < maxtries:
            (plan, fraction) = right_arm.compute_cartesian_path (
                                    waypoints,   # waypoint poses
                                    0.01,        # eef_step
                                    0.0,         # jump_threshold
                                    True)        # avoid_collisions
            attempts += 1
            if attempts % 10 == 0:
                rospy.loginfo("Still trying after " + str(attempts) + " attempts...")
                        
        if fraction == 1.0:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            right_arm.execute(plan)
            rospy.loginfo("Path execution complete.")
        else:
            rospy.loginfo("Path planning failed with only " + str(fraction) + " success after " + str(maxtries) + " attempts.")  
        print waypoints

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItDemo()
    except rospy.ROSInterruptException:
        pass