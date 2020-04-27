#!/bin/bash
echo """                                                       dPdPdP  .d888888   
88     88                                      88             d8    88   88 
88aaaaa88a .d8888b. 88d888b. .d8888b. dP    dP 88 .d8888b.    88aaaaa88a 88 
88     88  88ooood8 88       88 88    88    88 88 88ooood8    88     88  88 
88     88  88.  ... 88       88.  ... 88.  .88 88 88.  ...    88     88  88 
dP     dP  88888P   dP88888P 88888P dP 88888P     8888dP      88     88  88
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"""

echo "script by othmane mdarhri and Hatim atertour"
printf "\n\n"
echo "setting up RS323 device "
sudo chmod 666 /dev/ttyUSB0
echo "activating virtual environement"
source herculeai_env/bin/activate
echo "launching script"
python3 main.py
