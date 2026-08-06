#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:




