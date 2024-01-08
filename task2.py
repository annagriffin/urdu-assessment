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
    def on_press(self, key):
        if key.char == 'r':
            self.key_pressed = True
        return True
    def on_release(self, key):
        if key.char == 'r':
            self.key_pressed = False
        return True
    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return (in_data, pyaudio.paContinue)
    def recorder(self):
        # global started, p, stream, frames
        print("started: ", self.started, " key pressed: ", self.key_pressed)
        if self.key_pressed and not self.started:


            # Start the recording
            try:
                self.stream = self.p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK,
                                stream_callback = self.callback)
                print("Stream active:", self.stream.is_active())
                self.started = True
                print("start Stream")
            except Exception as e:
                print(e)
        elif not self.key_pressed and self.started:
            print("Stop recording")
            self.stream.stop_stream()
            self.stream.close()
            # self.p.terminate()
            print("frames: ")
            print(len(self.frames))
            print()
            self.wf.writeframes(b''.join(self.frames))
            self.wf.close()
            self.frames = []
            self.started = False
            print("You should have a wav file in the current directory")
            return
        # Reschedule the recorder function in 100 ms.
        task.enter(0.1, 1, self.recorder, ())



# Opening JSON file
with open('question_bank.json') as json_file:
    data = json.load(json_file)


# playsound('./assets/greeting.mp3')
# answer = input("ہیلو! آپ کا نام کیا ہے\n") # Hi! What is your name?


# playsound('./assets/greeting.mp3') # Let's test your skills

# WAVE_OUTPUT_FILENAME = f"./assets/recordings/{each['category']}-{each['difficulty_level']}-{each['index']}.mp3"
# WAVE_OUTPUT_FILENAME = "test.mp3"

for idx, each in enumerate(data[:4]):
    # listener.started = False
    playsound('./assets/greeting.mp3')
    # uncomment when we have translation files
    # playsound(f"./assets/{each["audio_file"]}")
    print(each["question_text_urdu"])

    print("recording")
    

    WAVE_OUTPUT_FILENAME = f"./assets/recordings/{each['category']}-{each['difficulty_level']}-{each['index']}.mp3"
    listener = MyListener()
    listener.start()
    

    print("Press and hold the 'r' key to begin recording")
    print("Release the 'r' key to end recording")
    task = sched.scheduler(time.time, time.sleep)
    task.enter(0.1, 1, listener.recorder, ())
    task.run()
    # listener.stop()

    print("stopped")



# playsound("1 + 4 کیا ہے؟") # What is 1 + 4?
# addition1 = input("1 + 4 کیا ہے؟\n")
# if addition1 == 5:
#     playsound("بہت اچھا کام")
# else:
#    playsound("آئیے ایک اور کوشش کریں۔")


# addition2 = int(input("What is 5 + 3?\n"))

# if addition2 == 8:
#     print("Great Job")
# else:
#     print("Let's try another")

