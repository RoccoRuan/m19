#!/usr/bin/env python
lastx = [0.1,1]
lasty = [0.1,1]
lastz = [0.1,1]

def controlx(coordinate):
    maxspeed = 1000
    disttoslow = 100
    resizedw = 500
    tolerance = 5
    pub_xctl = rospy.Publisher('xstuff', ******?*****, queue_size=10)
    rospy.init_node('x_speedanddir', anonymous=True)
    if coordinate == 0:
        speed = 0.9 * lastx[0]
        direction = lastx[1]
    else if coordinate > resizedw/2 + disttoslow:
        speed = maxspeed
        direction = -1
    else if coordinate < resizedw/2 - disttoslow:
        speed = maxspeed
        direction = 1
    else if coordinate <= resizedw/2 + disttoslow and coordinate >= resizedw/2 + tolerance:
        speed = abs(coordinate - resizedw/2)/disttoslow * maxspeed
        direction = -1
    else if coordinate <= resizedw/2 + disttoslow and coordinate >= resizedw/2 + tolerance:
        speed = abs(coordinate - resizedw/2)/disttoslow * maxspeed
        direction = 1
    else:
        speed = 0
        direction = 0
    lastx[0] = speed
    lastx[1] = direction
    pub_xctl.publish([speed,direction])

def listenerx():
    rospy.init_node('listenerx', anonymous=True)
    rospy.Subscriber("xstuff", float32, controlx)
    rospy.spin()

def controlz(coordinate):
    maxspeed = 1000
    disttoslow = 100
    resizedh = 500
    tolerance = 5
    pub_zctl = rospy.Publisher('zstuff', ******?*****, queue_size=10)
    rospy.init_node('z_speedanddir', anonymous=True)
    if coordinate == 0:
        speed = 0.9 * lastz[0]
        direction = lastz[1]
    else if coordinate > resizedh/2 + disttoslow:
        speed = maxspeed
        direction = -1
    else if coordinate < resizedh/2 - disttoslow:
        speed = maxspeed
        direction = 1
    else if coordinate <= resizedh/2 + disttoslow and coordinate >= resizedh/2 + tolerance:
        speed = abs(coordinate - resizedh/2)/disttoslow * maxspeed
        direction = -1
    else if coordinate <= resizedh/2 + disttoslow and coordinate >= resizedh/2 + tolerance:
        speed = abs(coordinate - resizedh/2)/disttoslow * maxspeed
        direction = 1
    else:
        speed = 0
        direction = 0
    lastz[0] = speed
    lastz[1] = direction
    pub_zctl.publish([speed,direction])

def listenerz():
    rospy.init_node('listenerz', anonymous=True)
    rospy.Subscriber("zstuff", float32, controlz)
    rospy.spin()

def controly(radius):
    maxspeed = 1000
    rtoslow = 50
    maxr = 100
    tolerance = 5
    pub_yctl = rospy.Publisher('ystuff', ******?*****, queue_size=10)
    rospy.init_node('y_speedanddir', anonymous=True)
    if radius = 0:
        speed = 0.9 * lastx[0]
        direction = lastx[1]
    else if radius > maxr - rtoslow:
        speed = maxspeed
        direction = -1
    else if radius < maxr + rtoslow:
        speed = maxspeed
        direction = 1
    else if radius <= maxr + rtoslow and radius >= maxr + tolerance:
        speed = abs(coordinate - resizedw/2)/disttoslow * maxspeed
        direction = -1
    else if radius >= maxr - rtoslow and radius <= maxr - tolerance:
        speed = abs(coordinate - resizedw/2)/disttoslow * maxspeed
        direction = 1
    else:
        speed = 0
        direction = 0
    lasty[0] = speed
    lasty[1] = direction
    pub_yctl.publish([speed,direction])

def listenery():
    rospy.init_node('listenery', anonymous=True)
    rospy.Subscriber("ystuff", float32, controly)
    rospy.spin()