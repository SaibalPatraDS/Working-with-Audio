## importing libraries

import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

## Reading a file(for an example)
file = "blues.0000.wav"  # write the location or name of the file, want to read

## waveform
signal, sr = librosa.load(file, sr = 22050)   # signal is a numpy array, signal_array = sample_rate(sr) * Time(T)
# show the signal
librosa.display.waveshow(signal, sr = sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

## Fourier Transformation (fast fourier transformation)

fft = np.fft.fft(signal)
magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

plt.plot(frequency, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

-- for half part

left_magnitude = magnitude[:int(len(magnitude)/2)]
left_frequency = frequency[:int(len(frequency)/2)]

plt.plot(left_frequency, left_magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()


