# Camera

The camera is a device capturing realtime videos and doing image processing in python to analyze:
- person presence
- person positions
- person activities

Once some changes are detected, a notification is send to the hub.

## Getting started

```bash

python3 -m venv .env.private
source .env.private/bin/activate

python3 -m pip install -r requirements.txt

python3 detection_video.py
```



## Setup 

The camera for using raspberry pi.

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

## Equipment 

- [Raspberry Pi B 4GB](https://www.amazon.ca/gp/product/B07W4JM192)
- [Camera with night vision](https://www.amazon.ca/gp/product/B076KCZRDS)

## Datasets & algorithms 

- [Kinetics](https://deepmind.com/research/open-source/kinetics)

## Tutorial & Litterature 

- [How to stream camera to computer](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
- [OpenCV and python on raspberry pi](https://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/)
- https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
- https://github.com/Sid2697/Object-Detection-MobileNet/blob/master/README.md
- https://arxiv.org/abs/1704.04861
- [Stream video in http](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
- 
## Brainstorm 

- https://www.npmjs.com/package/opencv4nodejs: fail to install
- https://www.npmjs.com/package/opencv: fail to install