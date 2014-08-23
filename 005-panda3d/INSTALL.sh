#!/bin/bash

# http://ubuntuusertips.wordpress.com/2014/04/14/panda3d-compile-from-source-install-and-start-programming-games-in-python-with-ubuntu-14-04/

# dependencies
sudo apt-get install -y build-essential bison flex python-dev
sudo apt-get install -y freeglut3-dev libglu1-mesa-dev libfreetype6-dev libosmesa6-dev
sudo apt-get install -y libgtk2.0-dev libpng12-dev libjpeg-dev libtiff5-dev libxft-dev libssl-dev
sudo apt-get install -y libeigen3-dev libswscale-dev fftw-dev libgles1-mesa-dev libgles2-mesa-dev libgegl-dev libode-dev libopenal-dev libbullet-dev libxxf86dga-dev
sudo apt-get install -y libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavifile-0.7-dev libavutil-dev
sudo apt-get install -y libopencv-dev

# get source
curl 'http://panda3d.cvs.sourceforge.net/viewvc/panda3d/?view=tar&pathrev=HEAD' | tar xvz

# build
cd panda3d
python makepanda/makepanda.py --everything --no-artoolkit --no-fcollada --no-fmodex --no-squish --no-tiff --no-vrpn --no-rocket --no-fftw --threads 4 --no-egl --no-gles --no-gles2 --installer

# install
sudo dpkg -i panda3d1.9_1.9.0_amd64.deb
