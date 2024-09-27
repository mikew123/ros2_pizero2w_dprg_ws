# DPRG ROS demo project for the club
This project is to make an in-expensive wheeled robot with sensors using ROS2 to demonstrate a simple ROS2 hardware robot.</br>
Initially the robot will be driven manually using a joystick or the keyboard and the sensor will cause an LED to flash faster when an object is closer.</br>
- NOTE: Any of the Pi boards can be used if you have one instead of the Pi Zero 2W</br>

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
We will need to add swap memory to make the Pi Zero run smoothly. Use the tutorial <https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04> select 500M of swap OR <https://linuxize.com/post/how-to-add-swap-space-on-ubuntu-20-04/></br>
If you are having issues connecting to wifi you can use a serial cable on pins 6 (Gnd), 8 & 10 and they will see the output of boot, (115200 baud) and will have a serial console to log into in case the device doesn't come up on the net for some reason, or to find out what the IP address is.</br>
## Update and reboot
Remember to apt update/upgrade and reboot after initial Ubuntu installation</br>
## ROS2 Iron installation
Use this tutorial to install ROS2 Iron</br>
<https://docs.ros.org/en/iron/Installation/Ubuntu-Install-Debs.html>
## Clone this repo for the ROS2 nodes
In the user home directory (cd ~) clone this demo repository to make things simple:</br>
- git clone https://github.com/mikew123/ros2_pizero2w_dprg_ws.git</br>

Then rename the new ros2_pizero2w_dprg_ws directory simple ros2_ws:</br>
- mv ros2_pizero2w_dprg_ws ros2_ws</br>

## Use VSCode on your PC to manage the ros2_ws and edit files
Use the VSCode "Remote Explorer" and create a new remote Linux SHH robo2w@robo2w.local</br>
It is easier to use when its access directory is the new ros2_ws
## Examples Talker and Listener nodes
These nodes are in the ros2_ws_examples ros2 package</br>
In VSCode go down the directory tree "ros2_ws/src/ros2_ws_examples/ros2_ws_examples"</br>
The talker.py and listener.py files are the python code files for the two nodes</br>
The "ros2_ws/src/ros2_ws_examples/setup.py" file has the info for ros2 to build these node files</br>
## LED and HCSR04 sensor nodes
These nodes are in the robo2w_stuff ros2 package</br>
In VSCode go down the directory tree "ros2_ws/src/robo2w_stuff/robo2w_stuff"</br>
The led_node.py and hcsr04_node.py files are the python code files for the two nodes</br>
The "ros2_ws/src/robo2w_stuff/setup.py" file has the info for ros2 to build these node files</br>
## gpiozero python package
The led and hcsr04 nodes need the gpiozero python package wich needs to be installed</br>
- pip3 install gpiozero</br>

### Allow non-root gpiozero access
Followed this web page: <https://superuser.com/questions/826124/use-sys-class-gpio-in-python-without-root-permissions> </br>
- sudo nano /etc/udev/rules.d/99-com.rules </br>
Add line to file: SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'chown -R root:gpio /sys/class/gpio && chmod -R 770 /sys/class/gpio; chown -R root:gpio /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio'"
- sudo usermod -a -G gpio robo2w </br>

# Running ROS2 nodes etc
You need to be in the workspace diectory "~/ros2_ws" to build the ros2 packages and nodes</br>
- cd ~/ros2_ws</br>

The nodes are built using this command</br>
- colcon build</br>

A neat trick is to build the python nodes with the --symlink option and they dont need to be built again when the code changes</br>
- colcon build --symlink</br>

After each build run the environment setup file so that ros2 knows were the nodes are</br>
- source install/setup.bash</br>

Now the nodes can be run.</br>
## HCSR04_NODE
In the SSH terminal enter:</br>
- ros2 run robo2w_stuff hcsr04_node</br>

Notice that the sensor distance reading in meters is displayed in the terminal. Put your hand in front of the sensor to see how far it is.</br>
## LED_NODE
In another SSH terminal enter:</br>
- ros2 run robo2w_stuff led_node</br>

The sensor distance is shown in the terminal and the LED flash duration is longer the closer your hand is to the sensor</br>
## HCSR04_MSG
The hcsr04 distance sensor communicates its distance to the led_node with a meassage the hcsr04_node generates</br>
In another SSH terminal enter:</br>
- ros2 topic echo /hcsr04_msg</br>

The sensor distances are shown in the terminal.</br>

<image src="images/Schematic_DPRG_ros_demo_2024-08-23.pdf"></br>

