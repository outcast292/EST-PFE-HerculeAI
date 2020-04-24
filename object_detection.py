from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import cv2
import sys
import handler
from sys import platform


execution_path = "model/"
detected = []

def returnDetected(output_arrays):
    detected = []
    for eachItem in output_arrays:
        if(len(eachItem) != 0):
            dictx = {
                "name": eachItem[0].get("name"),
                "box_points": eachItem[0].get("box_points"),
            }
            if len(detected) == 0:
                detected.append(dictx)
            else:
                for eachDict in detected:
                    if eachDict != dictx is True:
                        detected.append(dictx)

    return detected


def forSecond(frame_number, output_arrays, count_arrays, average_count, returned_frame):
    detected = returnDetected(output_arrays)
    if len(detected) == 0:
        print("Nothing detected")
    else:
        handler.sortObject(detected)


def launch_detector():
    handler.setup_handler()
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    #video_detector.setModelTypeAsRetinaNet()
    print("setting model")
    # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0
    video_detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    #video_detector.setModelPath(os.path.join(execution_path, "resnet.h5"))
    print("loading model")
    video_detector.loadModel("flash")
    print("loaded model")
    camera = None
    if platform=="win32":
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    elif platform=="linux":
        camera = cv2.VideoCapture(0)
    else:
        print("os detécté inconnu ou non-supporté")
        exit(0)

    plt.show()
    costum_obj = video_detector.CustomObjects(
        person=True, orange=True, banana=True, apple=True)
    video_detector.detectCustomObjectsFromVideo(camera_input=camera,
                                                save_detected_video=False,
                                                frames_per_second=5,
                                                frame_detection_interval=1,
                                                per_second_function=forSecond,
                                                per_frame_function=forFrame,
                                                minimum_percentage_probability=60,
                                                return_detected_frame=True,
                                                log_progress=True,
                                                display_percentage_probability=False,
                                                custom_objects=costum_obj
                                                )

    camera.release()
    cv2.destroyAllWindows()


def forFrame(frame_number, output_array, output_count, returned_frame):
    plt.clf()
    plt.title("Frame : " + str(frame_number))
    plt.imshow(returned_frame, interpolation="none")
    plt.pause(0.01)
