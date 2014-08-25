We have a modern Ubuntu 14.04.1 LTS system setup w/ ubuntu-desktop (Unity) running.

We've added the latest nvidia drives via https://launchpad.net/~xorg-edgers/+archive/ubuntu/ppa

(currently nvidia-343)


Oculus Setup
---
* DL latest Linux drivers from http://developer.oculsvr.com/
  * Currently this is 0.3.2

Run the ConfigurePermissionsAndPackages.sh to setup Ubuntu fairly well

You might need to symlink libudev (see the script notes)


jherico's https://github.com/jherico/OculusSDK in general seems to be better maintained/up-to-date

Until an official Linux 0.4 comes out, it may be best to use 0.3.3.pre1

That's what the current checkin is as:
http://stackoverflow.com/questions/1777854/git-submodules-specify-a-branch-tag

How to swap the submodule branch:
```
git fetch
git checkout 0.3.3.pre1
```

If you screw up, it's easiest to rm the submodule and just do a
```
git submodule update --init
```

More cheat sheet: http://blog.jacius.info/git-submodule-cheat-sheet/


At some point, I should probably roll in information into the dev wiki
maybe there should be a Linux page?

https://developer.oculusvr.com/forums/viewtopic.php?f=20&t=12972
https://developer.oculusvr.com/wiki/Tutorials
https://developer.oculusvr.com/wiki/Ubuntu_13.04


We may need/want to switch to Arch Linux:
* More up-to-date kernel for latest ATI/noveau drivers
* Wayland support
