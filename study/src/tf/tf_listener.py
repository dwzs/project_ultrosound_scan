#!/usr/bin/env python  


import rospy
import tf


if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/base_link', '/tool0', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        print trans 
        print rot
        rate.sleep()
