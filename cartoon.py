import cv2
import numpy as np

img = cv2.imread("removed_BG_LOGO.png")


def cartoonize(img, k):
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
    cv2.imshow("result", result)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges  = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
    # cv2.imshow("edges", edges)
    blurred = cv2.medianBlur(result, 3)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    cv2.imshow("cartoon",cartoon)
    

cartoonize(img, 8)
cv2.imshow("input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
