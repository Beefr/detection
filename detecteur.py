
import threading
#from cv2 import cvtColor, equalizeHist, COLOR_BGR2GRAY, VideoCapture,CascadeClassifier, imshow, ellipse, waitKey, destroyAllWindows
import cv2 as cv

from sound import Sound

class Detecteur(object):

    def __init__(self, path, frame_skip):
        self._model=None
        self._camera=None
        self._frame_skip=frame_skip
        self._sound=Sound()
        
        self._camera = cv.VideoCapture(0)

        while not self._camera.isOpened():
            pass # attente de l'ouverture de la caméra

        self._thread = threading.Thread(target=self.start_detecting, args=(self._frame_skip,))

        

        self.load_cascade_classifier(path)

        
        self._count=0
        self._thread.start()


    def __del__(self):
        self._camera.release()
        cv.destroyAllWindows()

    def start_detecting(self, frame_skip):
        
        #while True:
        self._count+=1
        if self._count==frame_skip:
            _, frame = self._camera.read()
            self.detect_object(frame)
            self._count=0
        
        self._thread.start()

    def detect_object(self, frame):
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        #-- Detect object
        obj = self._model.detectMultiScale(frame_gray)
        if len(obj)>=1:
            print("found a cat")
            self._sound.play()
        #self.show(frame, obj)


    def show(self, frame, obj):
        for (x,y,w,h) in obj:
            center = (x + w//2, y + h//2)
            frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        cv.imshow('Detection', frame)
        cv.waitKey(1)
        

    #-- 1. Load the cascade classifier
    def load_cascade_classifier(self, path):
        self._model = cv.CascadeClassifier(path)

    