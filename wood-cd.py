#_*_ coding:utf-8 _*_ 
#! usr/bin/env python3
import matplotlib.pyplot as plt

#数据
speed30 = [0.78,1.36,7.01]
speed40 = [0.70,0.77,3.44]
speed50 = [0.59,0.70,3.22]
speed60 = [0.75,1.02,3.23]
speed80 = [0.45,0.91,1.71]
wood = [0,30,60]

plt.style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(wood,speed30,marker=r'o',color=u'blue',linestyle='-',label="speed=30R/min")
ax1.plot(wood,speed40,marker=r'+',color=u'red',linestyle='--',label="speed=40R/min")
ax1.plot(wood,speed50,marker=r'*',color=u'green',linestyle='-.',label="speed=50R/min")
ax1.plot(wood,speed60,marker=r's',color=u'orange',linestyle=':',label="speed=60R/min")
ax1.plot(wood,speed80,marker=r'+',color=u'black',linestyle='-.',label="speed=80R/min")

labels_list=["speed=30R/min","speed=40R/min","speed=50R/min","speed=60R/min","speed=80R/min"]
plt.legend(labels_list,loc='best')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('木粉含量/%')
plt.ylabel('变异系数/%')
ax1.set_title('变异系数-木粉含量图')
plt.show()
