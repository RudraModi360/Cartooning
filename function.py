from rembg import remove
from PIL import Image
import numpy as np
import cv2
import os
from pathlib import Path
home = str(Path.home()) + "/Downloads/"


def Filter_gray(img):
    sf_name = img
    img = cv2.imread(img, cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(home, 'gray_' + os.path.basename(sf_name)),gray)

def Edges(img):
    sf_name=img
    img = cv2.imread(img,cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    edges_color = cv2.applyColorMap(edges, cv2.COLORMAP_WINTER)
    cv2.imwrite(os.path.join(home, 'Edged_'+os.path.basename(sf_name)),edges_color)

def merge(img):
    img = Image.open(img)
    output = remove(img)
    output.save("removed_BG.png")    
    mi1 = Image.open("removed_BG.png")
    mi2 = Image.open("bg.png")
    mi2.paste(mi1, (0, 0), mi1)
    mi2.save("C:\\Users\\Rudra\\Downloads\\merged_image.png")

def removebg(img):
    img = Image.open(img)
    output = remove(img)
    output.save("C:\\Users\\Rudra\\Downloads\\removed_BG_LOGO.png")
    

def cartoon(img):
    sf_name=img
    img = cv2.imread(img, cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # edges_color = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    color = cv2.bilateralFilter(img,1, 250, 250) 
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(os.path.join(home, 'Simple_Cartooned'+os.path.basename(sf_name)),cartoon)
def cartoonize(img, k):
    sf_name=img
    img = cv2.imread(img, cv2.IMREAD_COLOR)
    data = np.float32(img).reshape((-1, 3))
    print("shape of input data: ", img.shape)
    print("shape of resized data", data.shape)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, label, center = cv2.kmeans(
        data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)
    print(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    # cv2.imshow("result", result)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges  = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
    blurred = cv2.medianBlur(result, 3)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    cv2.imwrite(os.path.join(home, 'Final_Cartooned'+os.path.basename(sf_name)),cartoon)

Filter_gray("LOGO.jpeg")
Edges("LOGO.jpeg")
removebg("LOGO.jpeg")
cartoon("LOGO.jpeg")
cartoonize("LOGO.jpeg",8)
merge("LOGO.jpeg")

cv2.waitKey(0)
cv2.destroyAllWindows()
