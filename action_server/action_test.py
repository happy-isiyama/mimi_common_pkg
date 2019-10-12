#!/usr/bin/env python
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
#Title: ActionServerNodeのデバッグ用ROSノード
#Author: Issei Iida
#Date: 2019/10/11
#Memo:
#---------------------------------------------------------------------

#Python関係ライブラリ
import sys
#ROS関係ライブラリ
import rospy
import roslib

#sys.path.append(roslib.packages.get_pkg_dir('mimi_common_pkg') + 'action_server')
sys.path.insert(0, '/home/issei/catkin_ws/src/mimi_common_pkg/scripts/')
from common_action_client import *
def main():
    rospy.loginfo('Test ActionServer')
    #approachPersonAC()
    findPerson()
    rospy.loginfo('Finish test')

if __name__ == '__main__':
    try:
        rospy.init_node('action_test', anonymous = True)
        main()
    except rospy.ROSInterruptException:
        pass