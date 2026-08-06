# Edge Detection Using OpenCV

## Overview

This project demonstrates various edge detection techniques using Python and OpenCV. Edge detection is a fundamental image processing operation used to identify object boundaries by detecting sudden changes in pixel intensity.

The program reads an input image, converts it into grayscale, applies different edge detection algorithms, and displays the results for comparison.

---

## Objectives

- Read an image using OpenCV.
- Convert the image to grayscale.
- Apply different edge detection techniques.
- Compare the output of each edge detector visually.

---

## Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy
- Matplotlib

---

## Required Libraries

Install the required libraries using:

```bash
pip install opencv-python numpy matplotlib
```

---

## Project Structure

```
project/
│── sheero.jpg
│── edge_detection.py
│── README.md
```

---

## Edge Detection Techniques Used

### 1. Sobel Edge Detection
- Computes image gradients in the horizontal and vertical directions.
- Detects edges with good accuracy.

### 2. Prewitt Edge Detection
- Similar to Sobel but uses simpler convolution kernels.
- Useful for detecting horizontal and vertical edges.

### 3. Roberts Edge Detection
- Uses 2×2 kernels.
- Detects diagonal edges.
- Fast but sensitive to noise.

### 4. Laplacian Edge Detection
- Uses the second derivative of the image.
- Detects edges in all directions.

### 5. Canny Edge Detection
- Multi-stage edge detector.
- Produces thin and accurate edges.
- One of the most widely used edge detection algorithms.

---

## Input

Image file:

```
sheero.jpg
```

---

## Output

The program displays:

- Original Image
- Sobel Edge Detection
- Prewitt Edge Detection
- Roberts Edge Detection
- Laplacian Edge Detection
- Canny Edge Detection

---

## How to Run

Run the Python file:

```bash
python edge_detection.py
```

or execute the code in a Jupyter Notebook.

---

## Source Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("sheero.jpg")

# Check if image is loaded
if image is None:
    raise FileNotFoundError("Image not found. Check the image path.")

# Convert to RGB and Grayscale
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------
# Sobel Edge Detection
# --------------------------
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# --------------------------
# Prewitt Edge Detection
# --------------------------
kernelx = np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])

kernely = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])

prewittx = cv2.filter2D(gray, -1, kernelx)
prewitty = cv2.filter2D(gray, -1, kernely)
prewitt = cv2.add(prewittx, prewitty)

# --------------------------
# Roberts Edge Detection
# --------------------------
robertsx = np.array([[1,0],
                     [0,-1]])

robertsy = np.array([[0,1],
                     [-1,0]])

robertx = cv2.filter2D(gray, -1, robertsx)
roberty = cv2.filter2D(gray, -1, robertsy)
roberts = cv2.add(robertx, roberty)

# --------------------------
# Laplacian Edge Detection
# --------------------------
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# --------------------------
# Canny Edge Detection
# --------------------------
canny = cv2.Canny(gray, 100, 200)

# --------------------------
# Display Results
# --------------------------
plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(sobel, cmap="gray")
plt.title("Sobel")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(prewitt, cmap="gray")
plt.title("Prewitt")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(roberts, cmap="gray")
plt.title("Roberts")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(canny, cmap="gray")
plt.title("Canny")
plt.axis("off")

plt.tight_layout()
plt.show()
```

---

## Expected Result

The program displays the original image and the outputs of Sobel, Prewitt, Roberts, Laplacian, and Canny edge detection techniques in a single window, allowing easy visual comparison.

---

## Applications

- Image segmentation
- Object detection
- Face recognition
- Medical image analysis
- Autonomous vehicles
- Computer vision
- Robotics
- Industrial inspection

---

## Output
<img width="1233" height="610" alt="image" src="https://github.com/user-attachments/assets/7cbf585f-32a5-468b-ae58-373dbd89ee70" />


## Author
```
NAME : LOGITHA L
REFERENCE NO : 212225040207
```
