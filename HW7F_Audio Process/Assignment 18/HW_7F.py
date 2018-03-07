# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:26:27 2018

@author: chxzh
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav
from scipy import fftpack

#read data from raw file, cut one channel
rate, raw_data = wav.read('wooguy.wav')
data = raw_data[:,0]

#compute time step, fft and magnitude
dt = 1./rate
data_fft = fftpack.fft(data)
power = np.abs(data_fft)

#get fftfreq and plot magnitude against the frequency
freqs = fftpack.fftfreq(len(power),d = dt)
plt.plot(freqs, power)

#find 700Hz is the closest to the woo guy (by tone generator)
woo = 700

#set its adjacent area to be 0
area = 200
data_mod = data_fft.copy()
data_mod[np.logical_and(np.abs(freqs) > woo - area, np.abs(freqs) < woo + area)] = 0
power_mod = np.abs(data_mod)

#re-plot
freqs_mod = fftpack.fftfreq(len(power_mod), d = dt)
plt.plot(freqs_mod, power_mod)

#use ifft and write it to new file
new_data = fftpack.ifft(data_mod)
output = wav.write('wooguy_removed.wav',rate,new_data.astype(raw_data.dtype))