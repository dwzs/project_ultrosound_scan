#!/usr/bin/env python
import rospy, sys
from geometry_msgs.msg import Pose
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

if __name__ == "__main__":
#    tools = Tools()

    demo_list1 = [0.3, 0.4, 0.6, 0, 0, 0, 1]
    demo_list2 = [0.4, 0.4, 0.5, 0, 0, 0, 1]
    demo_list3 = [0.5, 0.4, 0.6, 0, 0, 0, 1]
    demo_lists = [demo_list1, demo_list2, demo_list3]

    waypoints = Tools.lists_to_waypoints(demo_lists)
    
    print (waypoints)
