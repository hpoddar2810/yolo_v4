import os
dir1 = "E:/yolo_v4/tensorflow-yolov4-tflite"
def process():
    code = "python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --image E:/yolo_v4/web_app/upload/upload.jpg"
    os.chdir(dir1)
    return os.system(code)