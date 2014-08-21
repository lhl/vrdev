##
# Base setup is from https://help.ubuntu.com/community/Installation/MinimalCD
# Ubuntu 14.04 amd64 USB boot stick
# * Basic Server
# * OpenSSH Server
# * Extra Fonts
# * ubuntu-desktop
##

# Basics
sudo apt-get install -y fish
sudo apt-get install -y avahi-daemon
sudo apt-get install -y unzip
sudo apt-get install -y build-essential
sudo apt-get install -y git
sudo apt-get remove unity-lens-shopping


# Python
sudo apt-get install -y python-setuptools
sudo apt-get install -y ipython-notebook
sudo easy_install pip
sudo pip install PyOpenGL
sudo pip install pyglet


# nvidia drivers
sudo add-apt-repository ppa:xorg-edgers/ppa -y
sudo apt-get update
sudo apt-get install -y nvidia-343


# X stuff
sudo apt-get install -y chromium-browser
sudo apt-get install -y vlc
sudo apt-add-repository ppa:tycho-s/ppa -y
sudo apt-get update
sudo apt-get install -y qtile

# nodm - future use
sudo apt-get install -y nodm

# Image Processing
sudo apt-get install -y python-opencv
sudo apt-get install -y fswebcam
sudo apt-get install -y cheese

###
# See also: https://randomfoo.hackpad.com/Linux-Desktop-Tools-QFiFiyW2Wmv
###

# sudo apt-get install i3
# sudo apt-get install mrxvt
# sudo apt-get install stress

