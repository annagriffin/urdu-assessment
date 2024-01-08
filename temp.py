import json
from playsound import playsound
from google.cloud import speech
import os
import base64
import io
import pyaudio
import wave
 
data = None

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.mp3"

p = pyaudio.PyAudio()  # Create an interface to PortAudio


def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)


# Opening JSON file
with open('question_bank.json') as json_file:
    data = json.load(json_file)


# playsound('./assets/greeting.mp3')
# answer = input("ہیلو! آپ کا نام کیا ہے\n") # Hi! What is your name?


# playsound('./assets/greeting.mp3') # Let's test your skills


for each in data[:1]:
    playsound('./assets/greeting.mp3')
    # uncomment when we have translation files
    # playsound(f"./assets/{each["audio_file"]}")
    print(each["question_text_urdu"])

    print("recording")

    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()




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

