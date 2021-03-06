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

sys.path.insert(0, '/home/athome/catkin_ws/src/mimi_common_pkg/scripts/')
from common_action_client import *
from common_function import *

def main():
    rospy.loginfo('Start Test')
    approachPersonAC()
    #enterTheRoomAC(0.5)
    #localizeObjectAC('person')
    rospy.loginfo('Finish Test')

if __name__ == '__main__':
    try:
        rospy.init_node('action_test', anonymous = True)
        main()
    except rospy.ROSInterruptException:
        pass
