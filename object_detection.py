from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import cv2
import sys


execution_path = "model/"
detected = []

resized = False

def forSecond(frame_number, output_arrays, count_arrays, average_count, returned_frame):
    global detected
    if len(output_arrays) != 0:
        for eachItem in output_arrays:
            dictx = {
                "name" : eachItem[0].get("name"),
                "box_points" : eachItem[0].get("box_points"),
            }
            if len(detected) == 0:
                detected.append(dictx)
            else:
                for eachDict in detected:
                    if eachDict != dictx is True:
                        detected.append(dictx)
                    else:
                        print("Already detected")

    else:
        print("Nothing detected in this frame")



def launch_detector():
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(os.path.join(execution_path, "yolo.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
    video_detector.loadModel()

    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    plt.show()
    costum_obj = video_detector.CustomObjects(person = True,orange=True,banana=True,apple=True)
    video_detector.detectCustomObjectsFromVideo(camera_input=camera, 
                                            save_detected_video=False,  
                                            frames_per_second=30,
                                            frame_detection_interval=3, 
                                            per_second_function=forSecond, 
                                            per_frame_function=forFrame, 
                                            minimum_percentage_probability=60, 
                                            return_detected_frame=True, 
                                            log_progress=True,
                                            detection_timeout=10,
                                            display_percentage_probability=False,
                                            custom_objects=costum_obj
                                            )

    camera.release()
    cv2.destroyAllWindows()

    return detected


def forFrame(frame_number, output_array, output_count, returned_frame):

    plt.clf()

    plt.title("Frame : " + str(frame_number))
    plt.imshow(returned_frame, interpolation="none")

    plt.pause(0.01)

