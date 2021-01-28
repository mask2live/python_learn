import cv2

video = cv2.VideoCapture(0)

a = 0  # count loop times

while True:
    a = a + 1
    check, frame = video.read()  # check -- bool, wether get image; frame -- numpy-array, image BGR infos

    print(check)
    print(frame)

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray screen
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # colorful screen

    cv2.imshow('Capturing', img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
