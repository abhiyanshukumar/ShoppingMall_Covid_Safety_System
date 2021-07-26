from tkinter import *

from PIL import ImageTk, Image
from cv2 import cv2
import time
from keras.models import load_model
import cv2
import numpy as np
import PIL.Image, PIL.ImageTk


class App:
    def __init__(self, window, w, h, video_source=0):
        self.window = window
        self.w = w
        self.h = h
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = Button(window, text="Capture Face", width=75, command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.labels_dict = {0: 'No MASK', 1: 'MASK'}
        self.model = load_model('model-008.model')
        self.color_dict = {0: (0, 0, 255), 1: (0, 255, 0)}
        self.vid = cv2.VideoCapture(video_source)
        self.face_clsfr = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            self.ret, self.img = self.vid.read()
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            faces = self.face_clsfr.detectMultiScale(gray, 1.3, 5)

            for x, y, w, h in faces:
                face_img = gray[y:y + w, x:x + w]
                resized = cv2.resize(face_img, (100, 100))
                normalized = resized / 255.0
                reshaped = np.reshape(normalized, (1, 100, 100, 1))
                result = self.model.predict(reshaped)

                label = np.argmax(result, axis=1)[0]

                cv2.rectangle(self.img, (x, y), (x + w, y + h), self.color_dict[label], 2)
                cv2.rectangle(self.img, (x, y - 40), (x + w, y), self.color_dict[label], -1)
                cv2.putText(self.img, self.labels_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        if self.ret:
            # Return a boolean success flag and the current frame converted to BGR
            return (self.ret, cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        else:
            return (self.ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
