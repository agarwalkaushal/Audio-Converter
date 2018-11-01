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

#If you wish to convert to single channel, download ffmpeg from https://ffmpeg.zeranoe.com/builds/ and add to path
#cmd> ffmpeg -i output.flac -ac 1 mono.flac
