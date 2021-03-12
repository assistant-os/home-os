# home-os

## Getting started

```shell

# on camera
source .env.private/bin/activate
python3 src/stream-camera.py


# on hub 
source .env.private/bin/activate
python3 src/detect_object.py --stream <url>
python3 src/detect_object.py --video <path to video>
python3 src/detect_object.py --video <path to video> --algo ssd
```

