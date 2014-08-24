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
sudo apt-get install -y htop
sudo apt-get install -y apt-file
sudo apt-get remove unity-lens-shopping


# Python
sudo apt-get install -y python-dev
sudo apt-get install -y python-setuptools
sudo apt-get install -y ipython-notebook
sudo apt-get install -y python-pygame
sudo easy_install pip
sudo pip install PyOpenGL
sudo pip install PyOpenGL-accelerate
sudo pip install pyglet
sudo pip install glfw
sudo pip install pyglfw

# Powerline
pip install --user git+git://github.com/Lokaltog/powerline
# https://powerline.readthedocs.org/en/latest/installation/linux.html#font-installation


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

# webcam 
sudo apt-get install -y python-opencv
sudo apt-get install -y fswebcam
sudo apt-get install -y cheese

# glfw3 - this is in utopic unicorn universe
# https://launchpad.net/~pyglfw/+archive/ubuntu/pyglfw
sudo apt-add-repository ppa:pyglfw/pyglfw -y
sudo apt-get update
sudo apt-get install -y libglfw3-dev

# openbox - why not?
git clone https://github.com/BurntSushi/xpybutil
cd xpybutil
sudo python setup.py install
cd ..
git clone https://github.com/BurntSushi/pytyle3
cd pytyle3
sudo python setup.py install
cd ..



###
# See also: https://randomfoo.hackpad.com/Linux-Desktop-Tools-QFiFiyW2Wmv
###

# sudo apt-get install i3
# sudo apt-get install mrxvt
# sudo apt-get install stress

