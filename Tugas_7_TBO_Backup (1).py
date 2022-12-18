import konversi
#Inserting Rules
def insert_rules(rules):
    nrules={}
    for x in rules:
        values = x.split(',')
        if(values[0] in nrules.keys()):
            if values[1] not in nrules[values[0]]:            
                nrules[values[0]].append(values[1])
        else:
            nrules[values[0]]=[values[1]]
    return nrules

#Checking Rules        
def check_rules(check : str,rules : dict):
    ans = []
    for index,(key,value) in enumerate(rules.items()):
        list_rules = value
        if(check in list_rules): #Apakah ada pada rules atau tidak
            if(key not in ans):
                ans+=[key]
    return ans
        
#Iterasi
def iteration(string):
    list_sgt = []
    mapping = []
    for x in range(len(string),0,-1): #Membuat list baru untuk mapping lokasi segitiga bawah
        beda = abs(len(string)-x)
        list_tambah = []
        for y in range(x):
            list_tambah.append([y,y+beda])
        mapping.append(list_tambah)

    for x in range(len(string),0,-1):
        counter=abs(x-len(string)) #Beda pada lokasi segitiga bawah, misal 1,1 beda 0, 1,2 beda 1
        list_sgt.append([]) 
        if(counter==0):
            for y in string:
                list_sgt[counter].append(check_rules(y,rules)) #untuk yang beda 0, langsung cek rules
        else:
            #Untuk beda 1 - panjang string-1 
            sgt_sub = []
            for i in range(x):
                sgt_sub.append(find_hasil(i,i+counter,mapping,list_sgt)) #Concat
            # print(list_sgt[0])
            for each in sgt_sub:
                list_ans = []
                for y in each:
                    list_ans += (check_rules(y,rules)) #Union
                if(list_ans==[]):
                    list_sgt[counter].append(['∅'])
                else:
                    list_ans = sorted([*set(list_ans)])[::-1] #Menghapus duplikat sekaligus sorting
                    list_sgt[counter].append(list_ans)
            # print(*list_sgt,sep='\n')

    print(*list_sgt,sep='\n')
    col,row = find_index(mapping,[0,len(string)-1])
    if(list_sgt[col][row]!=['∅']):
        print(list_sgt[col][row])
        print("Diterima")
    else:
        print("Ditolak")

def find_hasil(i,j,mapping,list_sgt):
    ans = []
    for a in range(i,j):
        b,c = find_index(mapping,[i,a]) #Mencari lokasi dari i,a di list_sgt
        list1 = list_sgt[b][c]
        d,e = find_index(mapping,[a+1,j]) #Mencari lokasi dari a+1,j di list_sgt
        list2 = list_sgt[d][e]
        for value1 in list1:
            if(value1==[]):
                continue
            for value2 in list2:
                if(value2==[]):
                    continue
                else:
                    if(value1+value2 not in ans):
                        ans += [value1+value2] #Union
    return ans

def find_index(mapping : list, find : list): #Mencari lokasi sgt dengan mencocokan pada mapping
    for x,value1 in enumerate(mapping):
        for y,value2 in enumerate(value1):
            if(value2 == find):
                return x,y    

def print_rules(rules:dict):
    for index,(key,value) in enumerate(rules.items()):
        print(f'{key} → ',end='')
        print(*value,sep='|')

rules = insert_rules(rules)
print_rules(rules)
# print(rules)
string = str(input('Masukkan string yang ingin dicek : '))
iteration(string)