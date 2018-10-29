#!/usr/bin/env python  


import rospy
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('tf_ransform')
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)

    pose_tcp = geometry_msgs.msg.PointStamped()
    pose_tcp.header.frame_id = 'tool0'
    pose_tcp.header.stamp =rospy.Time(0)
    pose_tcp.point.z = -0.1
    print pose_tcp


    while not rospy.is_shutdown():
        try:
            listener.waitForTransform("/base_link", "/tool0", rospy.Time(0),rospy.Duration(4.0))
            pose_base = listener.transformPoint('base_link', pose_tcp)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        print pose_base

        rate.sleep()


