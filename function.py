from rembg import remove
from PIL import Image
import numpy as np
import cv2

img = cv2.imread("cartoon_i2_edited.jpg", cv2.IMREAD_COLOR)
img1 = cv2.imread("cartoon_i1_edited.jpg")

def Filter_gray(img):
    img = cv2.imread("cartoon_i2_edited.jpg", cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)

def Edges(img):
    img = cv2.imread("cartoon_i2_edited.jpg",cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    edges_color = cv2.applyColorMap(edges, cv2.COLORMAP_WINTER)
    cv2.imshow("Edges", edges_color)

def merge(img1):
    img1 = Image.open("cartoon_i1_edited.jpg")
    output = remove(img1)
    output.save("removed_BG.png")
    mi1 = Image.open("removed_BG.png")
    mi2 = Image.open("bg.png")
    mi2.paste(mi1, (0, 0), mi1)
    mi2.save("merged_image.png")

def cartoon(img):
    img = cv2.imread("cartoon_i2_edited.jpg", cv2.IMREAD_COLOR)
    img = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # edges_color = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    color = cv2.bilateralFilter(img,1, 250, 250) 
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imshow("Cartoon", cartoon)

Filter_gray(img)
Edges(img)
merge(img1)
cartoon(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
