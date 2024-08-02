# DPRG ROS demo project for the club
This project is to make an in-expensive wheeled robot with sensors using ROS2 to demonstrate a simple ROS2 hardware robot.</br>
Initially the robot will be driven manually using a joystick or the keyboard and the sensor will cause an LED to flash faster when an object is closer.</br>
- NOTE: Any older Pi boards can be used if you have one 
# Install Ubuntu and ROS2 on Pi Zero 2W
We will use ROS2 Iron distribution since the most recent one (Jazzy) seems to be missing a few critical pyhton libraries. I am sure the libraries will be ported sometime soon, but we are starting now (Aug 2024)</br>
ROS2 Iron requires Ubuntu 22.04 so we will flash the Ubuntu 22.04 64bit server image onto the Pi Zero 2W. (This Pi can not handle a desktop which needs a lot of resources which it is low on.) It will be run "headless" and managed using wifi and SSH so remeber to enter the wifi credentials and SSH capability while flashing the SSD card.</br>
## Ubuntu 22.04 installation
Install the Raspberry Imager on windows and have a 32G SSD card and a card interface available. </br>
<https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/>
Insert the SSD card and start the pi-imager.</br>
Select DEVICE:Pi Zero 2W, OS: Other>Ubuntu>"22.04 server 64 bit"</br>
Chose our storage device SSD card. Chose edit options and add robo2w as the user name and a password of your choosing, configure wifi and enable SSH. Set Linux host name to robo2w (same as user name!)</br>
Wait many minutes for it to flash, then install on the Pi Zero board and power it up.</br>
It will take many minutes to initally boot and there is no light that flashes to let you know when so wait 10 minutes.</br>
You should be able to SSH into the Pi Zero using a Windows power shell window "ssh robo2w@robo2w.local", enter password.
.... You should get a prompt like "robo2w@robo2w>".</br>
We will need to add 4G of swap memory to make the Pi Zero run smoothly. Use the tutorial <https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04> but select 4G of swap instead of 1G OR <https://linuxize.com/post/how-to-add-swap-space-on-ubuntu-20-04/></br>
## ROS2 Iron installation

# LED and DistanceSensor nodes
Use the gpiozero package wich needs installation</br>
pip3 install gpiozero</br>
## Allow non-root gpiozero access
Followed this web page: <https://superuser.com/questions/826124/use-sys-class-gpio-in-python-without-root-permissions> </br>
sudo nano /etc/udev/rules.d/99-com.rules </br>
- Add line to file: SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'chown -R root:gpio /sys/class/gpio && chmod -R 770 /sys/class/gpio; chown -R root:gpio /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio'"

sudo usermod -a -G gpio robo2w </br>
