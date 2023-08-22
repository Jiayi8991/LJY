import numpy as np
import matplotlib.pyplot as plt

data = np.load('/Users/jiayi/Desktop/21cma_data/e20_56e6_150Mhz_56Mhz_70_726.npy')

print(data.shape)

num_samps = int(56e6)+1
center_freq = 150e6
Fs = 56e6



mag = np.abs(np.fft.fft(data))
mag = np.fft.fftshift(mag)

f = np.arange(Fs/-2.0, Fs/2.0, Fs/num_samps) # start, stop, step
f += center_freq
f = f/int(1e6)

v = np.abs(data)**2
t = np.arange(0, num_samps/Fs, 1/Fs) * int(1e6)
# data = np.abs(data)
# x = np.arange(10)
# print(x)
# data = x + 1

#时域信号图
plt.plot(t[0:10000], v[0:10000], '.-')
#plt.plot(t[:1000009], v[:1000009], '.-')
plt.xlabel("Time(us)")
plt.ylabel("mag")
plt.grid(True)
plt.show()

#频域
plt.xlabel("Frequency [MHz]")
plt.ylabel("Magnitude")
plt.plot(f,mag)
plt.show()

