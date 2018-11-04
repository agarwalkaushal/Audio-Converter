# Audio-Converter
Convert your Audio files to any FFmpeg codec using python's <a href="https://github.com/jiaaro/pydub"><b>pydub</b></a>. For handling conversions, <a href="https://ffmpeg.zeranoe.com/">FFmpeg</a> needs to be installed.
<br /><br />
Set path to environmental variables or set path of FFmpeg's binary explicitly.<br />
````
pydub.AudioSegment.converter = r"C:\\path\\to\\ffmpeg.exe"
````
<br />
In <b><i>file-flac.py</b></i>, replace format="mp3" with any other FFmpeg supported format. Also, get chunks of .raw files for audio processing using <b><i>file-raw.py</b></i>.
<br /><br />
Don't wish to use python, work directly from command line.
<br />


````
cmd> ffmpeg -i input.mp3 output.flac
```` 

<br />
For transcribing large audio files, Google's speech-to-text requires audio with FLAC extention & mono channel,
<br />


````
cmd> ffmpeg -i output.flac -ac 1 mono.flac
````
