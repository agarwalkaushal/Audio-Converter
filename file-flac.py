#FLAC: Free Lossless Audio Codec

from pydub import AudioSegment
import os

# The name of the audio file to convert
file_name = os.path.join(
    os.path.dirname("C:\\"),
    'Users\HP\PycharmProjects\\audio-converter',
    'song.mp3')

sound = AudioSegment.from_file(file_name, format="mp3")

sound.export("output.flac",format="flac")
