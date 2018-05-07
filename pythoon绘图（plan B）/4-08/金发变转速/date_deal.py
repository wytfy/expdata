#_*_ coding:utf-8 _*_ 
#! usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

#参数设定
line_styles=[':','-','--','-.','steps']

#处理文件名
file_num=int(input('请输入文件数量：'))
a=range(file_num)
file_list=[]
for i in a:
    file_list.append("{0:s}.csv".format(str(i+1)))

#读取文件,清洗数据，就截取后400个数据
for file in file_list:
    with open(file,'r',newline='') as csv_in_file:
        file_reader=csv.reader(csv_in_file,delimiter=',')
        next(file_reader)
        with open('{0:s}.csv'.format(file),'w',newline='') as file_writer:
            count = 1
            for row in file_reader:
                if count <= 200:
                    count +=1
                else:
                    file_writer.write(str(row[0])+','+str(row[4]) + '\r\n')
                    count +=1
        file_writer.close()

#新文件列表
new_file=[]
for b in file_list:
    new_file.append('{0:s}'.format('{0:s}.csv'.format(b)))

#画基础图形
plt.style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#循环画图
for file_use in new_file:
    with open('{0:s}'.format(file_use),'r',newline='') as new_file_input:
        new_file_reader=csv.reader(new_file_input,delimiter=',')
        x=[]
        y=[]
        l_n = new_file.index(file_use)
        for row_s in new_file_reader:
            x.append(int(row_s[1]))
            y.append(float(row_s[0]))
        #f = interpolate.interp1d(x, y,kind=3)
        #nx = np.linspace(x[0],x[-1],400)
        #ny = f(nx)
        #plt.plot(nx,ny,linestyle=line_styles[l_n])
        plt.plot(x,y,linestyle=line_styles[l_n])
#画出图表其他元素
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
title=input('请输入图像标题：')
ax1.set_title(title)
plt.xlabel('time/s')
plt.ylabel('torque/N*m')

labels_list=[]
for w in a:
    the_label=input('请输入第{0:d}条线的标签：'.format(w+1))
    labels_list.append(the_label)
plt.legend(labels_list,loc='best')
plt.savefig('wpcs.png',dpi=1000,bbox_inches='tight')
plt.show()

#完成提示
print('全部完成!')