#_*_ coding:utf-8 _*_ 
#! usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np   ##科学计算库 
import scipy as sp   ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法

#创建列表
list_csv = []
list_num = int(input("please input the number of list."))
for i in range(list_num):
    i += 1
    file_name = str(i)+"."+"csv"+"."+"csv"
    list_csv.append(file_name)
#读取列表中的文件，得出其均值，存储到列表中
torque_average = []
torque_cd = []
for j in list_csv:
    with open(j,'r',newline='') as file_read:
        torque_1 = []
        for row in file_read:
            row = row.split(',')
            if 350 <= int(row[1]) <= 550:
                torque_1.append(float(row[0]))
            else:
                pass
        aver_tor = sum(torque_1)/len(torque_1)
        torque_average.append(aver_tor)
        cd = np.std(torque_1)/np.mean(torque_1)
        torque_cd.append(cd)
speed = [30,40,50,60,80]
print(torque_cd)
'''
#最小二乘法
##样本数据(Xi,Yi)，需要转换成数组(列表)形式
##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array(speed)
Yi=np.array(torque_average)

#    设定拟合函数和偏差函数
#    函数的形状确定过程：
#    1.先画样本图像
#    2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)


##需要拟合的函数func :指定函数的形状
def func(p,x):
    k,b=p
    return k*x+b

##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y


#    主要部分：附带部分说明
#    1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
#    2.官网的原话（第二个值）：Value of the cost function at the solution
#    3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
#    4.返回值元组中第一个值的数量跟需要求解的参数的数量一致


#k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0=[1,20]

#把error函数中除了p0以外的参数打包到args中(使用要求)
Para=leastsq(error,p0,args=(Xi,Yi))

#读取结果
k,b=Para[0]
print("k=",k,"b=",b)
print("cost："+str(Para[1]))
print("求解的拟合直线为:")
print("y="+str(round(k,2))+"x+"+str(round(b,2)))


#   绘图，看拟合效果.
#   matplotlib默认不支持中文，label设置中文的话需要另行设置
#   如果报错，改成英文就可以


#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2) 

#画出图表其他元素
plt.xlabel('speed/R/min')
plt.ylabel('torque/N*m')
plt.title('平衡转矩-转速拟合结果')
#画拟合直线
x=np.linspace(0,100,100) ##在0-100直接画100个连续点
y=k*x+b ##函数式
plt.plot(x,y,color="red",label="拟合直线",linewidth=2) 
plt.legend(loc='lower right') #绘制图例
plt.show()
'''




#绘制变异系数-转速图
plt.style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(speed,torque_cd,marker=r'o',color=u'blue',linestyle='-')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('转速/R/min')
plt.ylabel('变异系数/%')
ax1.set_title('变异系数-转速图')
plt.show()
