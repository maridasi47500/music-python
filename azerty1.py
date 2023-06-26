from __future__ import division
 
import numpy as np
from scipy.io.wavfile import write
 
# Create waveform.
rate = 44100  # Sampling rate [samples/s].
n = 44100     # Length [samples].
f = 1000      # Frequency of the sine [Hz].
t = np.linspace(0, n / rate, n, endpoint=False)
f= 261 #do

note1 = np.sin(2 * np.pi * f * t)
do=np.round(note1 * 32767).astype(np.int16)
f=  293 #re

note2 = np.sin(2 * np.pi * f * t)
re=np.round(note2 * 32767).astype(np.int16)
f= 329 #mi
note3 = np.sin(2 * np.pi * f * t)
mi=np.round(note3 * 32767).astype(np.int16)
f= 349 #fa
note4 = np.sin(2 * np.pi * f * t)
fa=np.round(note4 * 32767).astype(np.int16)
f= 392 #sol
note5 = np.sin(2 * np.pi * f * t)
sol=np.round(note5 * 32767).astype(np.int16)
print(type(do))
# Save audio file (range of s is [-1, 1]).
write('sine.wav', rate, np.concatenate((do,mi,re,fa,mi,sol)))


