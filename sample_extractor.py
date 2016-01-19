import numpy as np
import cv2
import os, random
from sys import exit
import copy

class SampleExtractor:

    def __init__(self):
        self.filename = "main window"
        self.files = os.listdir("data")
        self.loadNextImage()

    def handleClick(self, event, m_x, m_y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, (x,y,w,h) in enumerate(self.candidates):
                if x <= m_x and m_x <= x+w and y <= m_y and m_y <= y+h:
                    self.positves.append(self.candidates[i])
                    self.save(i, True)
                    self.update()

        elif event == cv2.EVENT_RBUTTONDOWN:
            for i, (x,y,w,h) in enumerate(self.candidates):
                if x <= m_x and m_x <= x+w and y <= m_y and m_y <= y+h:
                    self.negatives.append(self.candidates[i])
                    self.save(i, False)
                    self.update()
        elif event == cv2.EVENT_MBUTTONDOWN:
            self.loadNextImage()

    def save(self, boundingBox, positve):
        (x,y,w,h) = self.candidates[boundingBox]
        center = [x+w/2, y+h/2]
        if positve:
            path = "positives/%s_%d_%d.png" % (self.filename[-7:-4], center[0], center[1])
        else:
            path = "negatives/%s_%d_%d.png" % (self.filename[-7:-4], center[0], center[1])
        cv2.imwrite(path, self.image[y:y+h, x:x+w])

    def update(self):
        image = copy.copy(self.image)

        for (x,y,w,h) in  self.candidates:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),1)
            roi_image = image[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]

        for (x,y,w,h) in  self.positves:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
            roi_image = image[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]

        for (x,y,w,h) in  self.negatives:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)
            roi_image = image[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]

        cv2.imshow(self.filename,image)

    def loadNextImage(self):
        cv2.destroyWindow(self.filename)
        if len(self.files) > 0:
            self.filename = random.choice(self.files)
            self.files.remove(self.filename)
            self.cascade = cv2.CascadeClassifier('cascade.xml')
            self.positves = []
            self.negatives = []
            self.image = cv2.imread('data/'+self.filename)
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            self.candidates = self.cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=10,minSize=(20,20), maxSize=(45,45))

            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            for (x,y,w,h) in  self.candidates:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),1)
                roi_image = image[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]

            cv2.namedWindow(self.filename, cv2.WINDOW_FULLSCREEN)
            cv2.setMouseCallback(self.filename, self.handleClick)

            cv2.imshow(self.filename,image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            exit("Unnoticed files array is empty. Add more files to the data/ folder and/or try again.")

sampleExtractor = SampleExtractor()