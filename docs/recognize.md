# Recognize

[# Object detection with deep learning and OpenCV](https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/)

When it comes to deep learning-based object detection there are three primary object detection methods that you’ll likely encounter:

-   [Faster R-CNNs](https://arxiv.org/abs/1506.01497) (Girshick et al., 2015) : complicated and slow, __~7fps__
-   [You Only Look Once (YOLO)](https://arxiv.org/abs/1506.02640) (Redmon and Farhadi, 2015) : very fast and not very accurate, __~40fps__
-   [Single Shot Detectors (SSDs)](https://arxiv.org/abs/1512.02325) (Liu et al., 2015) : compromise, more accurate, __~24fps__


- [List of models](https://github.com/onnx/models#image_classification)


## Detect people 

### Yolo

- [Detect with Yolo](https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/)
- [Yolo v3](https://arxiv.org/pdf/1804.02767.pdf)
- [List of trained classes](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

- [How to use MobileNet](https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/)
- [Coco dataset](https://cocodataset.org/#home) used to train MobileNet
- [How to use MobileNet](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
- https://www.pyimagesearch.com/2020/06/01/opencv-social-distancing-detector/

- https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
- https://github.com/Sid2697/Object-Detection-MobileNet/blob/master/README.md
- https://arxiv.org/abs/1704.04861


## Recognize activity 

- [Human Activity Recognition with OpenCV and Deep Learning](https://www.pyimagesearch.com/2019/11/25/human-activity-recognition-with-opencv-and-deep-learning/)
- https://github.com/kenshohara/3D-ResNets-PyTorch
- https://github.com/opencv/opencv/blob/master/samples/dnn/action_recognition.py
- https://github.com/shuvamdas/human-activity-recognition

- [Kinetics](https://deepmind.com/research/open-source/kinetics)

- https://github.com/kenshohara/3D-ResNets-PyTorch
- https://github.com/kenshohara/video-classification-3d-cnn-pytorch
- https://github.com/imatge-upc/activitynet-2016-cvprw use tensorflow

### 3d ResNets

```
python3 -m util_scripts.generate_video_jpgs ../datasets/test/video/ ../datasets/test/kinetics_videos/jpg kinetics --size 480
python3 -m util_scripts.kinetics_json ../datasets/test/annotations 700 ../datasets/test/kinetics_videos/jpg/default2/video jpg ../datasets/test/kinetics.json
python3 main.py --root_path ../datasets/test/ --video_path kinetics_videos/jpg --annotation_path kinetics.json --result_path results --dataset kinetics --resume_path results/r3d50_K_200ep.pth --model_depth 50 --n_classes 700 --n_threads 4 --no_train --no_val --inference --output_topk 5 --inference_batch_size 1 --no_cuda
```


## Recognize pose

- [Top and Best Computer Vision Human-Pose Estimation Projects](https://medium.datadriveninvestor.com/top-and-best-computer-vision-human-pose-estimation-projects-186d04204dde) 

### OpenPose

- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- https://learnopencv.com/multi-person-pose-estimation-in-opencv-using-openpose/
- https://learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/

### PifPaf

- [OpenPifPaf](https://github.com/vita-epfl/openpifpaf)

## Benchmarks

- https://www.hackster.io/news/benchmarking-machine-learning-on-the-new-raspberry-pi-4-model-b-88db9304ce4
- https://www.hackster.io/news/benchmarking-tensorflow-and-tensorflow-lite-on-the-raspberry-pi-43f51b796796