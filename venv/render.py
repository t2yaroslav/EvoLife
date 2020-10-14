import cv2

while True:
    cv2.imshow("camera", image)
    key = cv2.waitKey(100)
    if key == 27:  # Esc
        break

cv2.destroyAllWindows()