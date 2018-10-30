#!/usr/bin/env python
import rospy, sys, math, tf
from geometry_msgs.msg import Pose, PoseStamped
from copy import deepcopy

class Tools:
    def __init__(self):
        pass


    @staticmethod
    def lists_to_poses(lists):
        pose = Pose()
        waypoints = []

        for lst in lists:
            pose.position.x = lst[0]
            pose.position.y = lst[1]            
            pose.position.z = lst[2]            
            pose.orientation.x = lst[3]
            pose.orientation.y = lst[4]
            pose.orientation.z = lst[5]       
            waypoints.append(deepcopy(pose))
        return waypoints
    @staticmethod
    def information_adjust_to_quat(information_adjust):
        pose = Pose()
        pose.position.x = information_adjust[0]
        pose.position.y = information_adjust[1]   
        pose.position.z = information_adjust[2]
        pose.orientation.x = information_adjust[3] * math.sin(information_adjust[6]/2) 
        pose.orientation.y = information_adjust[4] * math.sin(information_adjust[6]/2)  
        pose.orientation.z = information_adjust[5] * math.sin(information_adjust[6]/2)  
        pose.orientation.w = math.cos(information_adjust[6]/2)
        return pose  

    @staticmethod
    def transform_pose_tcp_to_base(pose_target_tcp):
        listener = tf.TransformListener()
        poseStamped_tcp = PoseStamped()

        poseStamped_tcp.header.frame_id = 'ee_link'
        poseStamped_tcp.pose = pose_target_tcp
        listener.waitForTransform("/base_link", "/ee_link", rospy.Time(0),rospy.Duration(4.0))
        pose_base = listener.transformPose('base_link', poseStamped_tcp)

        return pose_base        



if __name__ == "__main__":
    rospy.init_node('tools') 
    demo_pose_target_tcp = Pose()       
#    tools = Tools()

    demo_list1 = [0.3, 0.4, 0.6, 0, 0, 0, 1]
    demo_list2 = [0.4, 0.4, 0.5, 0, 0, 0, 1]
    demo_list3 = [0.5, 0.4, 0.6, 0, 0, 0, 1]
    demo_lists = [demo_list1, demo_list2, demo_list3]
    demo_information_adjust = [0, 0, 0, 0, 0, 0, math.pi/4]
    demo_pose_target_tcp.position.z = -0.1

    waypoints = Tools.lists_to_poses(demo_lists)
    pose_quat = Tools.information_adjust_to_quat(demo_information_adjust)
    pose_base = Tools.transform_pose_tcp_to_base(demo_pose_target_tcp)



    # print (waypoints)
    # print pose_quat
    print pose_base
