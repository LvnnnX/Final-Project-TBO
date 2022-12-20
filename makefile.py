import re
with open('E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\input_test.txt','r') as f:
    listinput = f.readlines()
    for x,value in enumerate(listinput):
        if(value[0]==' '):
            value= value[1:len(value)]
        clean = re.sub('\n','',value)
        listinput[x] = clean
with open('E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\input_test.txt','w') as f:
    for x in listinput:
        x = x+'\n'
        f.write(x)