import cv2 as cv

video = cv.VideoCapture("pixar.mp4")

tracker = cv.legacy.TrackerCSRT_create()
success, image = video.read()
box = cv.selectROI("Tracking", image, False)
tracker.init(image, box)


def retangulo(image, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv.rectangle(image, (x, y), ((x + w), (y + h)), (255, 0, 0), 3, 1)


while True:
    timer = cv.getTickCount()
    success, image = video.read()

    success, box = tracker.update(image)

    if success:
        retangulo(image, box)
    else:
        cv.putText(image, "Lost", (75, 80), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv.putText(image, "Sair (s)", (250, 350), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv.imshow("Tracking Object", image)

    if cv.waitKey(1) & 0xff == ord('s'):
        break