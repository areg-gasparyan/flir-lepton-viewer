# lepton-thermal-camera

The lepton_viewer.py is the fast and easy python script in the Linux environment for configure and capture FLIR Lepton 3.5 thermal camera images.

To run the script you need to have a python3 and install the OpenCV package. For installation use the following command sudo pip install opencv-python

Running script:


python lepton_viewer.py --device=/dev/video4 --width=1920 --height=1440 --color-map=COLORMAP_BONE



Help:

python lepton_viewer.py --help
