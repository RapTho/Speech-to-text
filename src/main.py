import os
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def recognize_sync():
    dotenv_path = join(dirname(__file__), 'config.env')
    load_dotenv(dotenv_path)

    authenticator = IAMAuthenticator(os.getenv('APIKEY'))
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(os.getenv('URL'))

    with open((join(dirname(__file__), os.getenv('PATH_TO_FILE'))), 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type=os.getenv('AUDIO_FORMAT'),
            model=os.getenv('LANGUAGE'),
            word_alternatives_threshold=0.9,
            background_audio_suppression=os.getenv('BACKGROUND_SUPPRESSION'),
            word_confidence=False,
        ).get_result()
    
    transcript = speech_recognition_results['results']

    with open((join(dirname(__file__), 'output/transcriptRaw.json')), 'wt') as file:
        file.write(json.dumps(transcript, indent=2))

    with open((join(dirname(__file__), 'output/transcript.txt')), 'wt') as file:
        trancriptJoined = ""
        for index in range(0, (len(transcript) -1) ):
            trancriptJoined += transcript[index]['alternatives'][0]['transcript'] + ' '

        file.write(trancriptJoined)
        print(trancriptJoined)

if __name__ == "__main__":
    recognize_sync()