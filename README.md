# GetSetGreen

## Core Idea and Objective

Vehicle emissions are a major contributor to environmental pollution and climate change, with far-reaching consequences for the planet and human society. Our goal is to facilitate a seamless transition from combustion engine vehicles to electric vehicles by eliminating high-emission vehicles from the roads and allowing only those that meet emission check criteria to operate.

---

## Summary of Progress

Since the start of the hackathon, we have developed a program capable of:

- Extracting car license numbers from the number plates of vehicles.
- Searching for car details in a static CSV file database.
- Displaying car information to the user.
- Prompting users for the greenest navigation route between two cities of their choice.

---

## Current Functionality and Features

We have implemented the following functionalities:

- **OpenCV**: Utilized for object detection in captured images.
- **Imutils**: Used for extracting the layout of the image and sorting contours after edge detection.
- **Matplotlib**: Employed to display captured images.
- **EasyOCR**: Used for text recognition and extraction from images.
- **CSV Module**: Imported for working with the static CSV database, which contains car models, information, and navigation routes between cities.

---

## Future Plans

For the remainder of the hackathon, we plan to:

- Add a front-end interface to make the project more user-friendly and interactive.

---

## Installation Guide

To install the required libraries and files for this project, follow these instructions:

### For Windows:

```bash
# OpenCV
pip install opencv-python

# Matplotlib
pip install matplotlib

# Imutils
pip install imutils

# EasyOCR
pip install easyocr
```

### Check your GPU CUDA Core version by entering the command `nvidia-smi` in the CMD:
- CUDA 12.1
  ```bash
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

These modules have been tested with Python3 in a Windows environment.

### For macOS:

To install these libraries on macOS using Terminal, follow these steps:
- Open Terminal (Cmd + Space and type "Terminal" to search for it).
- Run the following commands:
 ``` bash
# OpenCV
sudo pip install opencv-python

# Matplotlib
sudo pip install matplotlib

# Imutils
sudo pip install imutils

# EasyOCR
sudo pip install easyocr
```
### Overview Video

Watch the project demonstration here:  
[GetSetGreen - Overview Video](https://youtu.be/CJgtsMvKSa0)


```bash

You can use this Markdown format for your project on GitHub or other platforms. It includes all the necessary details in a clean, organized format.
```
