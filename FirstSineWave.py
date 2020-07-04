# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import numpy as np
from scipy.io.wavfile import write

# Samples per second
sps = 44100

# Frequency / pitch of C sharp (138.59 - Low Sa to 277.18 - High Sa)
freq_hz = 277.18

# Duration
duration_s = 5.0

# np.arange (n) = [0,1, ..., n-1]
each_sample_number = np.arange(duration_s * sps)
print("each_sample_number: " + str(each_sample_number))

# waveform = sin (2 * pi * each_sample_number * number of samples taken per period)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
print("waveform: " + str(waveform))

# diminish amplitude 
waveform_quiet = waveform * 0.3
print("waveform_quiet: " + str(waveform_quiet))

# int16 is datatype: int from -32768 to 32767 (=0b111111111111111)
# converts decimals from -1 to 1 (outputs of sine) to ints from -32768 to 32767 (=0b111111111111111) that wav reads
waveform_integers = np.int16(waveform_quiet * 32767)
print("waveform_integers: " + str(waveform_integers))
print (len(waveform_integers))
print (duration_s * sps)

# Write the .wav file
# write('c_sharp_HIGHSA.wav', sps, waveform_integers)


