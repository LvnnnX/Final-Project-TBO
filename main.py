import process, general

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
    if general.check_alphabet(kalimat.get().lower().split()) == False:
        showinfo(title="Notifikasi", message="Kalimat Tidak Valid Karena Terdapat Kata Yang Belum Ada Di Data File")
    elif process.table_filling_process(kalimat.get().lower().split()) == True:
        showinfo(title="Notifikasi", message="Kalimat Diterima Karena Sesuai Dengan Pola Dan Persyaratan")
    else:
        showinfo(title="Notifikasi", message="Kalimat Ditolak Karena Tidak Sesuai Dengan Pola Dan Persyaratan")

button = ttk.Button(frame, text="Cek", command=event)
button.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()