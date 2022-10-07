import cv2 as cv

image = cv.imread("questao1/pokemon.jpg")
hsvImg = cv.cvtColor(image, cv.COLOR_BGR2HSV)

maskVermelho = cv.inRange(hsvImg, (0, 50, 50), (17, 255, 255))
cntVermelho = cv.findContours(maskVermelho, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
cntVermelho = sorted(cntVermelho, key=cv.contourArea, reverse=True)[:2]

if cntVermelho:
    for cnt in cntVermelho:
        (cx, cy), r = cv.minEnclosingCircle(cnt)
        cv.putText(image, "Red", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 0), 2)
        cv.circle(image, (int(cx), int(cy)), int(r), (0, 0, 0), 3)

maskVerde = cv.inRange(hsvImg, (30, 50, 50), (80, 255, 255))
cntVerde = cv.findContours(maskVerde, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
cntVerde = sorted(cntVerde, key=cv.contourArea, reverse=True)[:2]

if cntVerde:
    for cnt in cntVerde:
        (cx, cy), r = cv.minEnclosingCircle(cnt)
        cv.putText(image, "Green", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 0), 2)
        cv.circle(image, (int(cx), int(cy)), int(r), (0, 0, 0), 3)

maskAzul = cv.inRange(hsvImg, (67, 50, 50), (100, 255, 255))
cntAzul = cv.findContours(maskAzul, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
cntAzul = sorted(cntAzul, key=cv.contourArea, reverse=True)[:2]

if cntAzul:
    for cnt in cntAzul:
        (cx, cy), r = cv.minEnclosingCircle(cnt)
        cv.putText(image, "Blue", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 0), 2)
        cv.circle(image, (int(cx), int(cy)), int(r), (0, 0, 0), 3)


cv.imshow("image", image)
cv.waitKey(0)
