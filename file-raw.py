from pydub import AudioSegment
import os

# The path of the audio file to convert

file_name = os.path.join(
    os.path.dirname("C:\\"),
    'Users\HP\PycharmProjects\\audio-transcribe',
    'song.mp3')

sound = AudioSegment.from_file(file_name, format="mp3")

#chunks of raw files depends on number of seconds, for eg. if 5 then set value = 5*1000

value = 5000
c = 1

if not os.path.exists("Output"):
   os.makedirs("Output")

for i in range(0,round(len(sound) / value) * value,value):
    temp = sound[i:i+value]
    r = temp.raw_data
    f = open('Output\\file'+str(c)+'.raw', 'wb')
    f.write(r)
    c = c + 1

