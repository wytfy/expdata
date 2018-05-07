#! usr/bin/env python3

#创建文件名列表
file_index=range(1,6,1)
file_name_read=[]
for i in file_index:
    file_name_read.append('{0:d}.txt'.format(i))
#文件处理
for file in file_name_read:
    file_num=file_name_read.index(file)+1
    file_read=open(file,'r',newline='')
    file_save=open('{0:d}.csv'.format(file_num),'w',newline='')
    n=1
    for row in file_read:
        if n==1:
            n +=1
        elif n%5==0:
            list=row.split(',')
            list_select=str(list[4])+','+str(list[0]+'\r\n')
            file_save.write(list_select)
            n +=1
        else:
            n +=1
    file_save.close()
