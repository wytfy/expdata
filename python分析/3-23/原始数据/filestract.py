import sys

root_input=sys.argv[1]
root_output=sys.argv[2]

file_open=open(root_input,'r',newline='')
file_save=open(root_output,'w',newline='')

i=1
for row in file_open:
    if i==1:
        i +=1
    elif i%5==0:
        list=row.split(',')
        list_select=str(list[4])+','+str(list[0]+'\r\n')
        file_save.write(list_select)
        i +=1
    else:
        i +=1
file_save.close()