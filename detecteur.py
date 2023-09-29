
from cv2 import cvtColor, equalizeHist, COLOR_BGR2GRAY, VideoCapture,CascadeClassifier, imshow, ellipse, waitKey, destroyAllWindows
from sound import Sound

class Detecteur(object):

    def __init__(self, path, frame_skip):
        self._model=None
        self._camera=None
        self._frame_skip=frame_skip
        self._sound=Sound()

        self.load_cascade_classifier(path)
        self.start_detecting(self._frame_skip)


    def start_detecting(self, frame_skip):
        self._camera = VideoCapture(0)
        if not self._camera.isOpened:
            print('--(!)Error opening video capture')
            exit(0)
        count=0
        while True:
            count+=1
            if count==frame_skip:
                _, frame = self._camera.read()
                self.detect_object(frame)
                count=0
        self._camera.release()
        destroyAllWindows()

    def detect_object(self, frame):
        frame_gray = cvtColor(frame, COLOR_BGR2GRAY)
        frame_gray = equalizeHist(frame_gray)
        #-- Detect object
        obj = self._model.detectMultiScale(frame_gray)
        if len(obj)>=1:
            print("found a cat")
            self._sound.play()
        #self.show(frame, obj)


    def show(self, frame, obj):
        for (x,y,w,h) in obj:
            center = (x + w//2, y + h//2)
            frame = ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        imshow('Detection', frame)
        waitKey(1)
        

    #-- 1. Load the cascade classifier
    def load_cascade_classifier(self, path):
        self._model = CascadeClassifier(path)

    