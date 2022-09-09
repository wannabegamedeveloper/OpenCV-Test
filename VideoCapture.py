import cv2 as cv

def GrabVideo():
    return cv.VideoCapture('C:/Users/tusha/Videos/3d character.mp4')

capture = GrabVideo()

while True:
    isTrue, frame = capture.read()
    if (isTrue):
        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('d'):
            break
    else:
        capture = GrabVideo()

capture.release()
cv.destroyAllWindows()