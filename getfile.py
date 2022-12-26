import re
with open('E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\verb.txt','r') as f:
    input = f.readlines()
    for key,value in enumerate(input):
        if(value[0]==' '):
            value= value[1:len(value)]
        clean = re.sub('\n','',value)
        input[key] = clean
    print(*input,sep=' | ')