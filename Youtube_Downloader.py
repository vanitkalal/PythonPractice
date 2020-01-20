# This program will download a video using YouTube URL and convert it to an MP3 file

from pytube import YouTube
import time
import subprocess

print('Enter the YouTube URL which will be then converted to MP3: ')

x = input()

yt = YouTube(x)

print(yt.title)

print('Filename: ')

_filename = input()

print(yt.streams.all())
print('Downloading... ')
stream = yt.streams.download(filename=_filename)
#stream.download(/Users/vanitk/Downloads)
time.sleep(1)

mp4 = (_filename + '.mp4')
mp3 = (_filename + '.mp3')

ffmeg = ('ffmeg -i %s ' % mp4 + mp3)
subprocess.call(ffmeg, shell=True)

print('\nDone\n')


