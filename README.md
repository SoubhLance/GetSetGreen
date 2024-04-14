# GetSetGreen

The core idea and objective of the project:                                                                                                                                                                                   
Vehicle emissions are a major contributor to environmental pollution and climate change, with far-reaching consequences for the planet and human society. We intend to have a seamless paradigm shift from combustion engine based vehicle to electric vehicle provided only the vehicles with higher emission rates are eliminated from roads and the ones meeting the emission check criteria are permitted

Summary of what has been accomplished since the start of the hackathon:
The program so developed until now from the hackathon beginning is capable of extracting car license number from number plate of the car and search for the car details in database which as of now is static csv file and display the same info to user while prompting for greenest navigation route between any two cities as selected by user.

The current functionality and features implemented:                                                                                                                                                                       
We have utilised OpenCV(Open Computer Vision) library for object detection in captured image,
Imutils for extracting layout of the image and sorting contours after edge detection,
Matplotlib module to display captured image,
EasyOCR for text recognition and extraction,
CSV module imported for comma seperated values list of car model and information and also list of starting point to destination.

Future plans and goals for the remainder of the hackathon:                                                                                                                                                                      
Adding a front-end to our project to make it user friendly

The Installation Guide for the libraries and files used in the Project are:
1#OpenCV : pip install opencv-python
2#Matplotlib : pip install matplotlib
3#Imutils : pip install imutils
4#EasyOCR : pip install easyocr
5# Check your GPU CUDA Core version by entering the command "nvidia-smi" in the CMD
a) CUDA 11.8 : pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
b) CUDA 12.1 : pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
all the above modules are tested in python3 and using a windows environment.

For mac:
To install these Python libraries on a Mac, you can use the Terminal application. Follow these steps:

Open Terminal: You can find Terminal in the Applications > Utilities folder, or you can use Spotlight Search (Cmd + Space) and type "Terminal" to open it.

1#OpenCV :sudo pip install opencv-python
2#Matplotlib :sudo pip install matplotlib
3#Imutils :sudo pip install imutils
4#EasyOCR :sudo pip install easyocr

