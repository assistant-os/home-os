# Camera

The camera is a device capturing realtime videos and doing image processing in python to analyze:
- person presence
- person positions
- person activities

Once some changes are detected, a notification is send to the hub.


# Setup & Installation

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
13. `sudo apt-get install libatlas-base-dev`
14. `sudo apt-get install libsm6 libxext6 libxrender1`
15. `sudo apt-get install build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev`
16. `sudo apt-get install libwebp-dev`
17. `sudo apt-get install libtiff4`



```shell 
sh ./scripts/setup.sh
sh ./scripts/install.sh # may fail
```

- models


## Getting started

```shell
python3 src/recognize_stream.py --host 0.0.0.0 --port 8080

```

## Equipment 

cf [Hardware documentation](../docs/hardware.md)

## Datasets & algorithms 

- [Kinetics](https://deepmind.com/research/open-source/kinetics)

## Tutorial & Litterature 

Camera with raspberry pi:
- [OpenCV on raspberry pi](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)
- [Stream video in http](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/): useful to make video stream in http
- [How to stream camera to computer](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/) to use picamera
- [OpenCV and python on raspberry pi](https://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/)

Detect people:

- [How to use MobileNet](https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/)
- [Coco dataset](https://cocodataset.org/#home) used to train MobileNet
- [How to use MobileNet](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
- https://www.pyimagesearch.com/2020/06/01/opencv-social-distancing-detector/

- https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
- https://github.com/Sid2697/Object-Detection-MobileNet/blob/master/README.md
- https://arxiv.org/abs/1704.04861


- [Stream python](https://github.com/jacksonliam/mjpg-streamer)

## Benchmarks

- https://www.hackster.io/news/benchmarking-machine-learning-on-the-new-raspberry-pi-4-model-b-88db9304ce4
- https://www.hackster.io/news/benchmarking-tensorflow-and-tensorflow-lite-on-the-raspberry-pi-43f51b796796


