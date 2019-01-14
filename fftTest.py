# !/usr/bin/python

import pyaudio
import wave
import struct
import numpy as np
import scipy.fftpack

CHUNK = 1024 * 4             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

data = stream.read(CHUNK)
print(data)
# convert data to integers, make np array, then offset it by 127

#w = scipy.fftpack.fft(data_int) #Does the FFT shit on the data
#freqs = scipy.fftpack.fftfreq(len(w), CHUNK)
#print freqs

#data_array = np.array(data_int)
#w = np.fft.fft(data_array)
#freqs = np.fft.fftfreq(len(w))
#print(freqs.min(), freqs.max())
## (-0.5, 0.499975)

# Find the peak in the coefficients
#idx = np.argmax(np.abs(w))
#freq = freqs[idx]
#freq_in_hertz = abs(freq * RATE)
#print(freq_in_hertz)







#y = np.fft.fft(data_int)
#print np.abs(y)
