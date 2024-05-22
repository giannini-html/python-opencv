import cv2

IMAGE_PATH="1344213.png"

DISPLAY_WINDOW = "result"

img = cv2.imread(IMAGE_PATH)

cv2.imshow(DISPLAY_WINDOW, img)

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break