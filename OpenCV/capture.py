import cv2

first_frame = None

video = cv2.VideoCapture(0)

while True:
    """ Because strong lighting, effect is not really good, will be optimized later """
    check, frame = video.read()  # check -- bool, whether get image; frame -- numpy-array, image BGR info

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray screen
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)  #
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # colorful screen

    if first_frame is None:
        first_frame = gray_img
        continue

    delta_frame = cv2.absdiff(first_frame, gray_img)
    thresh_delta = cv2.threshold(delta_frame, 61, 225, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_delta, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Gray Frame', gray_img)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    # print(gray_img)
    # print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
