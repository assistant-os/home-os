# Datasets

```txt 
.
├── README.md
├── video.avi
└── video_recognize.avi
```


```
ffmpeg -ss 00:00:00 -i ~/Downloads/video.recorded.mp4 -to 00:01:30 -c copy datasets/tests/video05.mp4
```
