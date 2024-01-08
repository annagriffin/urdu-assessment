import json
from playsound import playsound
from google.cloud import speech
import os
import base64
import io
import pyaudio
import wave
from pynput import keyboard
import time
import pyaudio
import wave
import sched
import sys
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
 
data = None


class MyListener(keyboard.Listener):
    def __init__(self):
        super(MyListener, self).__init__(self.on_press, self.on_release)
        self.key_pressed = None
        self.started = False
        self.stream = None
        self.wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        self.wf.setnchannels(CHANNELS)
        self.p = pyaudio.PyAudio()
        self.wf.setsampwidth(self.p.get_sample_size(FORMAT))
        self.wf.setframerate(RATE)
        self.frames = []
        self.skip_flag = False
        self.continuee = False
    def on_press(self, key):

        if hasattr(key, "char"):
            if key.char == 's':
                self.skip_flag = True
            elif key.char == 'c':
                self.continye = False
                return True
        if hasattr(key, "name") and key.name == 'space':
            self.key_pressed = True
        return True
    def on_release(self, key):
        if hasattr(key, "name") and key.name == 'space':
            self.key_pressed = False
        return True
    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return (in_data, pyaudio.paContinue)
    def recorder(self):
        if self.skip_flag:
            return
        if self.key_pressed and not self.started:

            try:
                self.stream = self.p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK,
                                stream_callback = self.callback)
                self.started = True
            except Exception as e:
                print(e)
        elif not self.key_pressed and self.started:
            self.stream.stop_stream()
            self.stream.close()
            self.wf.writeframes(b''.join(self.frames))
            self.wf.close()
            self.frames = []
            self.started = False
            return
        # Reschedule the recorder function in 100 ms.
        task.enter(0.1, 1, self.recorder, ())



# Opening JSON file
with open('short_question_bank.json') as json_file:
    data = json.load(json_file)


playsound('./assets/greeting.mp3') # Hi do you speak urdu?
playsound('./assets/press-yes.mp3')
speak_urdu = input("ہیلو! کیا آپ اردو بولتے ہیں\n") 

if (speak_urdu == "y"):

    playsound('./assets/lets-get-started.mp3') # Let's get started
    playsound('./assets/testing-math.mp3') # Today we are testing your math skills
    playsound('./assets/ask-you-some-questions.mp3') # I will ask you some questions
    playsound('./assets/hold-down-button.mp3') # After I ask each question, hold down the big button and say your answer out loud
    playsound('./assets/dont-know.mp3') # If you don't know the answer, it's okay to skip!
    playsound('./assets/start-test.mp3') # We will start

    pause = input()
    if pause == 'c':



        for idx, each in enumerate(data):
        
            playsound(f"./assets/questions/{each['audio_file']}")
            print(each["question_text_engl"])

            WAVE_OUTPUT_FILENAME = f"./assets/recordings/recording-{each['category']}-{each['index']}.mp3"
            listener = MyListener()
            listener.start()


            print("Press and hold the ' ' key to begin recording")
            task = sched.scheduler(time.time, time.sleep)
            task.enter(0.1, 1, listener.recorder, ())
            task.run()

            print("\nStopped")

            c = input()

        


playsound('./assets/youre-done.mp3')

