#DOA_array
import numpy as np
import matplotlib.pyplot as plt

r = np.load("/Users/jiayi/Desktop/21cma_data/e19e20_10e6_150Mhz_10Mhz_70_726.npy")
#r = np.load("/Users/jiayi/array_data/signal0629_1420_ch0_1.npy")
r = r.reshape(2,-1)
print(r.shape)

d = 10 # array element distance
Nr = 2 # array number

#DOA开始找到达方向
theta_scan = np.linspace(-1*np.pi, np.pi, 1000) # 1000 different thetas between -180 and +180 degrees
results = []
for theta_i in theta_scan:
    #print(theta_i)
    w = np.asmatrix(np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta_i))) # look familiar?
    r_weighted = np.conj(w) @ r # apply our weights corresponding to the direction theta_i
    r_weighted = np.asarray(r_weighted).squeeze() # get it back to a normal 1d numpy array
    results.append(np.mean(np.abs(r_weighted)**2)*10) # energy detector

# print angle that gave us the max value
print(theta_scan[np.argmax(results)] * 180 / np.pi) # 19.99999999999998

plt.plot(theta_scan*180/np.pi, results) # lets plot angle in degrees
plt.xlabel("Theta [Degrees]")
plt.ylabel("DOA Metric")
plt.grid()
plt.show()

#用极坐标来找位置
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta_scan, results) # MAKE SURE TO USE RADIAN FOR POLAR
ax.set_theta_zero_location('N') # make 0 degrees point up
ax.set_theta_direction(-1) # increase clockwise
ax.set_rgrids([0,2,4,6,8])
ax.set_rlabel_position(22.5)  # Move grid labels away from other labels
plt.show()
