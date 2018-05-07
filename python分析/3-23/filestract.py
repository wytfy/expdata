import sys

root_input=sys.argv[1]
root_output=sys.argv[2]

file_open=open(root_input,'r',newline='')
file_save=open(root_output,'w',newline='')
for row in file_open:
    list=row.split(',')
    list_select=str(list[4])+','+str(list[0]+'\r\n')
    file_save.write(list_select)
file_save.close()