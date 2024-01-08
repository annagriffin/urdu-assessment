

from playsound import playsound
from google.cloud import speech
import os
import json
import base64
import io

file_name = "./assets/recordings/recording-counting-1.mp3"


def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response



def print_response(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)


def print_result(result: speech.SpeechRecognitionResult):
    best_alternative = result.alternatives[0]
    print("-" * 80)
    print(f"language_code: {result.language_code}")
    print(f"transcript:    {best_alternative.transcript}")
    print(f"confidence:    {best_alternative.confidence:.0%}")


config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    audio_channel_count=1,
    sample_rate_hertz=24000,
    language_code="ur-PK",
)

with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    myObj = base64.b64encode(content).decode('ascii')
    audio = speech.RecognitionAudio(content=myObj)

response = speech_to_text(config, audio)
print_response(response)




# # Sends the request to google to transcribe the audio
# response = client.recognize(request={"config": config, "audio": audio})
# # Reads the response
# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))




# playsound('./assets/greeting.mp3')
# answer = input("ہیلو! آپ کا نام کیا ہے\n") # Hi! What is your name?




# playsound("آئیے آپ کی صلاحیتوں کا اندازہ لگائیں۔") # Let's test your skills
# playsound("ہم اضافہ کے ساتھ شروع کریں گے") # We will start with addition



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


