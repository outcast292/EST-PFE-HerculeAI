#!/bin/bash
echo "downloading python3"
sudo apt-get install python3.7
sudo apt-get install python3-pip
sudo apt-get install python3-venv
sudo apt-get install python3-tk
sudo pip3 install virtualenv
echo "creating virtual environement"
python3 -m venv herculeai_env
source herculeai_env/bin/activate
echo "installing dependencies"
pip3 install -r ./requirements.txt
echo "downloading Model"
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5 -O model/yolo.h5 --show-progress
echo "DONE!!!!"
