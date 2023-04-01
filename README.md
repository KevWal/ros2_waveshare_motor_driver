Please note this is work in progress and not yet complete

# ROS 2 Waveshare Motor Driver HAT Package
ROS 2 Driver Package for the PCA9685 based Waveshare Motor Driver HAT on a Rasperbery Pi for a two-wheeled differential drive and castor robot.

Converts /cmd_vel topic to i2c register settings for the PCA9685 to control a differential drive robot.
- https://www.waveshare.com/motor-driver-hat.htm
- https://www.waveshare.com/wiki/Motor_Driver_HAT

ToDo:
- Add feedback mechanism using wheel encoders
- Add runaway timeout protection

Created from these tutorials:
- https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html
- https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html

Inspiration taken from:
- https://github.com/stevej52/ros2_pca9685
