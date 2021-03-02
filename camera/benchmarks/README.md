# Benchmarks

## How to create benchmark file

```shell
 top -n 1 -b | head -n 10
```

## Versions 

### Version 1: MobileNet with video streaming

- top ouput: _top.mobileNet_v1.txt_
- hardware: running on raspberry
- algo architecture: mobileNet with caffee
- details: compute all images


```
[INFO] elapsed time: 133.07
[INFO] approx. FPS: 0.29
[INFO] computations: count: 38, mean: 3.400s, std: 0.043
```

With macbook 16"

```
[INFO] elapsed time: 19.56
[INFO] approx. FPS: 13.55
[INFO] computations: count: 265, mean: 0.045s, std: 0.003
```

Why?
- https://www.hackster.io/news/benchmarking-machine-learning-on-the-new-raspberry-pi-4-model-b-88db9304ce4
- https://www.hackster.io/news/benchmarking-tensorflow-and-tensorflow-lite-on-the-raspberry-pi-43f51b796796

### Version 2: MobileNet with prerecorded video

Raspberry pi:
```
[INFO] elapsed time: 268.90
[INFO] approx. FPS: 0.37
[INFO] computations: count: 100, mean: 2.635s, std: 0.012
```

With macbook 16":
```
[INFO] elapsed time: 4.46
[INFO] approx. FPS: 22.41
[INFO] computations: count: 100, mean: 0.040s, std: 0.002
````