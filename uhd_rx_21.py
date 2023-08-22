import uhd
import os
import numpy as np

usrp = uhd.usrp.MultiUSRP()
samples = usrp.recv_num_samps(int(1e6), 150e6, 10e6, [0,1], 50) # units: Number_sample, frequency_Hz, sample_rating_Hz, list of channel IDs, dB
print(samples[0:10])
print(samples.shape)
# samples.tofile('FM103_CH0_1.iq')

#data = np.zeros([])
data = np.zeros([2,int(1e6)])
# print(data.shape)
data = np.append(data, samples)
print(data[0:10])
np.save(f"./samp10e6_0630_103_ch1_pm", data, allow_pickle=True)
