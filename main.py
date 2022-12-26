import process, general
import re
import convert_cyk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
 
window.configure(bg="white")
window.geometry("400x400")
window.resizable(False, False)
window.title("Tugas Final Project")

frame = ttk.Frame(window)
frame.pack(padx=20, pady=20, fill="x", expand=True)

label_entry = ttk.Label(frame, text="Masukkan Kalimat Yang Ingin Diuji")
label_entry.pack(padx=10, fill="x", expand=True)

kalimat = tk.StringVar()
entry = ttk.Entry(frame, textvariable=kalimat)
entry.pack(padx=10, fill="x", expand=True)

def event():
    # if(convert_cyk.is_accepted(kalimat.get().lower().lower())):
    #     showinfo(title="Diterima!", message="Kalimat Diterima")
    # else:
    #     showinfo(title="Ditolak.", message="Kalimat Ditolak")
    if general.check_alphabet(kalimat.get().lower().split()) == False:
        showinfo(title="Hah kalimat apa ini?", message="Kalimat Tidak Valid")
    elif process.table_filling_process(kalimat.get().lower().split()) == True:
        showinfo(title="Diterima!", message="Kalimat Diterima")
    else:
        showinfo(title="Ditolak.", message="Kalimat Ditolak")

button = ttk.Button(frame, text="Cek", command=event)
button.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()

#CEK ALL
# with open('E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\input_test.txt','r') as f:
#     listinput = f.readlines()
#     ditrima=0
#     for x,value in enumerate(listinput):
#         if(value[0]==' '):
#             value= value[1:len(value)]
#         clean = re.sub('\n','',value.lower())
#         if(clean[len(clean)-1]=='.'):
#             clean=clean[0:len(clean)-1]
#         if(general.check_alphabet(clean.lower().split()) == False):
#             print(f'{x+1:>2}. Tidak Ada di List Alphabet')
#         else:
#             if(convert_cyk.is_accepted(clean.lower())):
#                 ditrima+=1
#                 print('Valid')
#             else:
#                 print('Tidak Valid')
#             # if(process.table_filling_process(clean.lower().split()) == True):
#             #     print(f'{x+1:>2}. Diterima',clean)
#             #     hasil = process.print_table(clean.lower().split())
#             #     print(f'{hasil}')
#             #     ditrima+=1
#             # else:
#             #     print(f'{x+1:>2}. Ditolak \n',clean)
#             #     hasil = process.print_table(clean.lower().split())
#             #     print(f'{hasil}')
# print(f'{ditrima}/{len(listinput)}')
