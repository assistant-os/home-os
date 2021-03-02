# Benchmarks

## How to create benchmark file

```shell
 top -n 1 -b | head -n 10
```

## Versions 

### Version 1

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
[INFO] approx. FPS: 13.08
```


- https://www.hackster.io/news/benchmarking-machine-learning-on-the-new-raspberry-pi-4-model-b-88db9304ce4
- https://www.hackster.io/news/benchmarking-tensorflow-and-tensorflow-lite-on-the-raspberry-pi-43f51b796796

### Version 2

Prerecorded video

```
[INFO] elapsed time: 268.90
[INFO] approx. FPS: 0.37
[INFO] computations: count: 100, mean: 2.635s, std: 0.012
```