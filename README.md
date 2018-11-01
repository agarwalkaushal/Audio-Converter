# Audio-Converter
Convert your Audio files to any FFmpeg codec using python's <b>pydub</b>.
<br /><br />
In .py, replace format="mp3" with any other FFmpeg supported format. Also, get chunks of .raw files for audio processing.
<br /><br />
Don't wish to use python, work directly from command line. Download <a href="https://ffmpeg.zeranoe.com/">FFmpeg</a> and set path to environmental variables.
<br />
<br />
````
cmd> ffmpeg -i input.mp3 output.flac
````
Convert stereo to mono,
<br />
````
cmd> ffmpeg -i output.flac -ac 1 mono.flac
