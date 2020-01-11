#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
file_baseline_dir= 'deconv.txt'
file_v1_dir= 'conv.txt'
file_v2_dir= 'skip_conv.txt'
file_v3_dir= 'depth_final.txt'

f1 = open(file_baseline_dir, 'r')
f2 = open(file_v1_dir, 'r')
f3 = open(file_v2_dir, 'r')
f4 = open(file_v3_dir, 'r')

list1 = f1.readlines()
length1=len(list1)
xy1=[]
for i in range(length1):
    xdata1 = float(list1[i].split(' ')[0])
    ydata1 = float(list1[i].split(' ')[1])
    xy1.append((xdata1,ydata1))
xy1=np.reshape(np.array(xy1),[-1,2])
plt.plot(xy1[:,0],xy1[:,1], 'ro-',label = 'baseline')

# list2 = f2.readlines()
# length2=len(list2)
# xy2=[]
# for i in range(length2):
#     xdata2 = float(list2[i].split(' ')[0])
#     ydata2 = float(list2[i].split(' ')[1])
#     xy2.append((xdata2,ydata2))
# xy2=np.reshape(np.array(xy2),[-1,2])
# plt.plot(xy2[:,0],xy2[:,1], 'bo-',label = 'nearest neighbor sample+conv')
#
# list3 = f3.readlines()
# length3=len(list3)
# xy3=[]
# for i in range(length3):
#     xdata3 = float(list3[i].split(' ')[0])
#     ydata3 = float(list3[i].split(' ')[1])
#     xy3.append((xdata3,ydata3))
# xy3=np.reshape(np.array(xy3),[-1,2])
# plt.plot(xy3[:,0],xy3[:,1], 'yo-',label = 'skip+conv')

list4 = f4.readlines()
length4=len(list4)
xy4=[]
for i in range(length4):
    xdata4 = float(list4[i].split(' ')[0])
    ydata4 = float(list4[i].split(' ')[1])
    xy4.append((xdata4,ydata4))
xy4=np.reshape(np.array(xy4),[-1,2])
plt.plot(xy4[:,0],xy4[:,1], 'go-',label = 'full')


plt.title('depth abs error :deconv VS nearest neighbor sample+conv VS skip-connection+conv')
plt.xlabel('step')
plt.ylabel('error')
plt.legend(loc = 0)
plt.show()
