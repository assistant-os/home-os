# Raspberry pi 

## How to setup

1. [install Raspberry pi OS](https://www.raspberrypi.org/software/)
2. [How to find raspberry pi](https://superuser.com/questions/124453/how-can-i-scan-the-local-network-for-connected-devices-mac-os): `ifconfig | grep broadcast` then `arp -a`
3. [Authorize ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
4. [Ssh access](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)
5. Default access: username: `pi`, password `raspberry` 
6. [Generate ssh key](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
7. Connect `ssh pi@raspberrypi.home`
8. [setup wifi](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md)
9. Install git `sudo apt-get install git`
10. Setup camera: `sudo raspi-config` (https://www.raspberrypi.org/forums/viewtopic.php?t=198118)
11. Take a photo: `raspistill -o image.jpg`
12. Download the image on the computer `scp pi@raspberrypi.home:~/image.jpg .`
13. `sudo apt-get install libatlas-base-dev`
14. `sudo apt-get install libsm6 libxext6 libxrender1`
15. `sudo apt-get install build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev`
16. `sudo apt-get install libwebp-dev`
17. `sudo apt-get install libtiff4`
