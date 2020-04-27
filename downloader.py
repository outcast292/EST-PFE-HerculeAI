import wget
print("Downloading model, it might take some time ~150MB")
url = "https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5"
wget.download(url, 'model\\yolo1.h5')
