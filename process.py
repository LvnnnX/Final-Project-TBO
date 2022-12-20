import grammar

def create_table(n):
    table = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append("")
        table.append(temp)
    return table

def concat(x, y):
    z = []
    for i in x:
        for j in y:
            z.append("{} {}".format(i, j))
    return z

def gabung_rumus(table:list):
    # print(table)
    temptable = []
    ubah = 0
    x=0
    while(x<len(table)-1):
        # print('ini x ke ',x)
        ada=0
        temp = ''
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x] in value):
                temp = str(id) + ' ' + table[x+1]
        for key,(id,value) in enumerate(grammar.production.items()):
            if(temp in value):
                # print(f'ketemu {temp} di {id}')
                temptable.append(temp)
                # print(temptable)
                ada=1
                break
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x+1] in value):
                temp = table[x] + ' ' + str(id)
        for key,(id,value) in enumerate(grammar.production.items()):
            if(temp in value):
                # print(f'ketemu {temp} di {id}')
                temptable.append(temp)
                # print(temptable)
                ada=1
                break
        if(ada):
            x=x+2
            ubah=1
            continue
        else:
            temptable.append(table[x])
            x+=1
        # print(temptable)
    table=temptable
    for x in range(len(table)):
        for key,(id,value) in enumerate(grammar.production.items()):
            if(table[x] in value):
                temptable2 = []
                for a,b in enumerate(table):
                    if(a!=x):
                        temptable2.append(b)
                    else:
                        temptable2.append(id)
                table = temptable2
    return table
def table_filling_process(array):
    susunan = grammar.susunan_kata.copy()
    table = ['' for x in range(len(array))]
    # print(array)
    for i in range(len(array)):
        table[i] = grammar.check_production([array[i]])[0]
    table = gabung_rumus(table)
    # print('ini table',table)
    for a,b in enumerate(table):
        for index,(key,value) in enumerate(grammar.main_production.items()):
            if(b in value):
                ada = 0
                for cari in susunan:
                    if(key == cari):
                        ada =1
                        table[a] = key
                        susunan.remove(key)
                        if(len(susunan)==0):
                            susunan=grammar.susunan_kata
                        break
                if(ada):
                    break
    # print('ini hasil',table)
    hasil = ' '.join(table)
    if(hasil in grammar.production['K']):
        return 1
    else:
        return 0
    # for i in range(1, len(array)):
    #     for j in range(i, len(array)):
    #         temp = []
    #         for k in range(j-i, j):
    #             temp = temp + concat(table[j-i][k], table[k+1][j])
    #         table[j-i][j] = grammar.check_production(temp)
    # return grammar.check_symbol(table[0][len(array)-1])
