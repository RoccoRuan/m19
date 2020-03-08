#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

import sys, termios, tty, os, time, fcntl
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    except:
        ch = "0"
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def talker():
    x_dir = "stop"
    y_dir = "stop"
    z_dir = "stop"
    x_speed = 0
    y_speed = 0
    z_speed = 0
    pub = rospy.Publisher('motor_commands', String, queue_size=10)
    rospy.init_node('manual_motor_controller', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        

        keypress = getch()
        if (keypress == "a"):
            x_dir = "left"
        elif (keypress == "d"):
            x_dir = "right"
        elif (keypress == "w"):
            y_dir = "forward"
        elif (keypress == "s"):
            y_dir = "back"
        elif (keypress == "e"):
            z_dir = "up"
        elif (keypress == "q"):
            z_dir = "down"
        elif (keypress == "r"):
            x_speed += 1
            y_speed += 1
            z_speed += 1
        elif (keypress == "f"):
            x_speed -= 1
            y_speed -= 1
            z_speed -= 1
        else:
            x_dir = "stop"
            y_dir = "stop"
            z_dir = "stop"
        if (x_speed > 10000):
            x_speed = 10000
        elif (x_speed < 0):
            x_speed = 0
        if (y_speed > 10000):
            y_speed = 10000
        elif (y_speed < 0):
            y_speed = 0
        if (z_speed > 10000):
            z_speed = 10000
        elif (z_speed < 0):
            z_speed = 0
        commands = x_dir+" "+str(x_speed)+" "+y_dir+" "+str(y_speed)+" "+z_dir+" "+str(z_speed)
        print(commands)
        rospy.loginfo(commands)
        pub.publish(commands)
        rate.sleep()

if __name__ == '__main__':
    fd = sys.stdin.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    try:
        talker()
    except rospy.ROSInterruptException:
        pass


