from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import cv2
import sys


execution_path = os.getcwd()
detected = []
global camera
resized = False

def forSecond(frame_number, output_arrays, count_arrays, average_count, returned_frame):
    plt.subplot(1, 1, 1)
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")




def launch_detector():
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(os.path.join(execution_path, "yolo.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
    video_detector.loadModel()

    camera    =  cv2.VideoCapture(0,cv2.CAP_DSHOW)

    costum_obj = video_detector.CustomObjects(cup = True, orange=True)
    video_detector.detectCustomObjectsFromVideo(camera_input=camera, 
                                            save_detected_video=False,  
                                            frames_per_second=20,
                                            frame_detection_interval=20, 
                                            per_second_function=forSecond,  
                                            minimum_percentage_probability=30, 
                                            return_detected_frame=True, 
                                            log_progress=True,
                                            detection_timeout=2,
                                            display_percentage_probability=False,
                                            custom_objects=costum_obj  )
    camera.release()
    cv2.destroyAllWindows()

    print("result")
    print(detected)


launch_detector()