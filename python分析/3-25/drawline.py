#! usr/bin/env python3
import matplotlib.pyplot as plt

#创建图标列表及其文件名列表
marker_list=[',','.','o','v','*']
sample_list=['speed=30 R/m','speed=40 R/m','speed=50 R/m','speed=60 R/m','speed=80 R/m']
file_index=range(1,6,1)
file_name=[]
for i in file_index:
    file_name.append('{0:d}.csv'.format(i))
#画基础图
plt.style.use('ggplot')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

#画出各个数据相应图案
for file in file_name:
    filereader=open('{0:s}'.format(file),'r',newline='')
    count_num=file_name.index(file)
    data_var=[]
    for row in filereader:
        row_list=row.split(',')
        data_select=float(row_list[1])
        data_var.append(data_select)
    ax1.plot(data_var,marker=r'{0:s}'.format(marker_list[count_num]),color=u'green',linestyle='--',label='{0:s}'.format(sample_list[count_num]))

#画出图表其他元素
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Pic of Torque-Time')
plt.xlabel('Time/s')
plt.ylabel('Torque/N*m')
plt.legend(loc='best')
plt.savefig('wpcs.png',dpi=800,bbox_inches='tight')
plt.show()