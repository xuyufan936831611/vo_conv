#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
file_rnn_dir='no_decouple.txt'
file_svo_dir='decouple.txt'
f1 = open(file_rnn_dir, 'r')
f2 = open(file_svo_dir, 'r')
################09
# list1 = f1.readlines()
# length=len(list1)
# xy1=[]
# for i in range(length):
#     xdata = float(list1[i].split(' ')[0])
#     ydata = float(list1[i].split(' ')[1])
#     xy1.append((xdata,ydata))
# xy1=np.reshape(np.array(xy1),[-1,2])
# plt.figure('09')
# plt.plot(xy1[:,0],xy1[:,1], 'ro-',label = 'no_decouple')
#
# list2 = f2.readlines()
# length=len(list2)
# xy2=[]
# for i in range(length):
#     xdata = float(list2[i].split(' ')[0])
#     ydata = float(list2[i].split(' ')[1])
#     xy2.append((xdata,ydata))
# xy2=np.reshape(np.array(xy2),[-1,2])
#
# plt.plot(xy2[:,0],xy2[:,1], 'bo-',label = 'decouple')
#
# plt.title('seq 09 abs error :no_decouple VS decouple')
# plt.xlabel('step')
# plt.ylabel('error')
# plt.legend(loc = 0)
################10
list1 = f1.readlines()
length=len(list1)
xy1=[]
for i in range(length):
    xdata = float(list1[i].split(' ')[0])
    ydata = float(list1[i].split(' ')[2])
    xy1.append((xdata,ydata))
xy1=np.reshape(np.array(xy1),[-1,2])
plt.figure('10')
plt.plot(xy1[:,0],xy1[:,1], 'ro-',label = 'no_decouple')

list2 = f2.readlines()
length=len(list2)
xy2=[]
for i in range(length):
    xdata = float(list2[i].split(' ')[0])
    ydata = float(list2[i].split(' ')[2])
    xy2.append((xdata,ydata))
xy2=np.reshape(np.array(xy2),[-1,2])
plt.plot(xy2[:,0],xy2[:,1], 'bo-',label = 'decouple')
plt.title('seq 10 abs error :no_decouple VS decouple')
plt.xlabel('step')
plt.ylabel('error')
plt.legend(loc = 0)
plt.show()
