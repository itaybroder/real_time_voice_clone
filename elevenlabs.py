import requests

def speech_to_speech(voice_id, audio_file_path, api_key):
    url = f"https://api.elevenlabs.io/v1/speech-to-speech/{voice_id}"

    headers = {
        'Content-Type': 'multipart/form-data',
        'xi-api-key': api_key,
    }

    data = {
        'audio': open(audio_file_path, 'rb')
    }

    response = requests.post(url, headers=headers, files=data)

    if response.status_code == 200:
        with open('output.mp3', 'wb') as out_file:
            out_file.write(response.content)

        print("Speech to speech conversion successful!")
    else:
        print(f"Error: {response.status_code}")

    return response.status_code