# Camera

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

## Equipment 

- [Raspberry Pi B 4GB](https://www.amazon.ca/gp/product/B07W4JM192)
- [Camera with night vision](https://www.amazon.ca/gp/product/B076KCZRDS)

## Datasets & algorithms 

- [Kinetics](https://deepmind.com/research/open-source/kinetics)

## Tutorial & Litterature 

- https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
- https://github.com/Sid2697/Object-Detection-MobileNet/blob/master/README.md
- https://arxiv.org/abs/1704.04861

## Brainstorm 

- https://www.npmjs.com/package/opencv4nodejs: fail to install
- https://www.npmjs.com/package/opencv: fail to install
