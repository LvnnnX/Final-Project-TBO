file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\verb.txt", "r")
kata_kerja = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\noun.txt", "r")
kata_benda = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\adj.txt", "r")
kata_sifat = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\adv.txt", "r")
kata_keterangan = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\num.txt", "r")
numeralia = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\prep.txt", "r")
preposisi = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\prop_noun.txt", "r")
proper_noun = file.read().split("\n")
file.close()
file = open("E:\\Folder_apps\\NGODING\\Python\\Final-Project-TBO-main\\file_kata\\pronoun.txt", "r")
kata_ganti = file.read().split("\n")

file.close()

alphabet = kata_kerja + kata_benda + kata_sifat + kata_keterangan + numeralia + preposisi + proper_noun + kata_ganti
cek = 'dia menggunakan gaun biru di acara tersebut'
def check_alphabet(array):
    for i in array:
        if i not in alphabet:
            print(i)
            return False
    return True