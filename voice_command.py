#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import cv2
import numpy as np
import multiprocessing

# function for response to command

def respond(command):
    if "start" in command:
        print("Start Recording")
        cap = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


# function to translate audio to command

def hear(audio):
    command = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + command)
    return command


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)



# recognize speech using Google Speech Recognition
try:

    command = hear(audio)
    respond(command)


except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
