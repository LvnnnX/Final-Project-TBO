# CFG
# ======================================================================================

# K → S P | S P Pel | S P O | S P Ket | S P O Pel | S P O Ket

# S -> NP 
# P -> VP | AdjP | NP
# O -> NP
# Pel -> NP | AdjP | NumP | VP | PP | NP VP
# Ket -> PP | NP

# NP → Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# VP → Verb | Adv VP
# AdjP → Adv AdjP | Adj
# PP → Prep NP
# NumP → Num | NumP Num | NumP Noun


# CNF
# ======================================================================================

# K -> S P
# K -> K Pel
# K -> K O
# K -> K Ket

# S -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# P -> Verb | Adv VP
# P -> Adj | Adv AdjP
# P -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# O -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# Pel -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# Pel -> Adj | Adv AdjP
# Pel -> Num | NumP Num | NumP Noun
# Pel -> Verb | Adv VP
# Pel -> Prep NP
# Pel -> NP VP

# Ket -> Prep NP
# Ket -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# NP → Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# VP → Verb | Adv VP
# AdjP → Adv AdjP | Adj
# PP → Prep NP
# NumP → Num | NumP Num | NumP Noun




# variable = ["K", "S", "P", "O", "Pel", "Ket", "NP", "VP", "AdjP", "PP", "NumP", "Verb", "Noun", "Adj", "Adv", "Num", "Prep", "PropNoun", "Pronoun"]
# production = {
#     "K" : ["S P", "K Pel", "K O", "K Ket"],
#     "S" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
#     "P" : general.kata_kerja + ["Adv VP"] + general.kata_sifat + ["Adv AdjP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
#     "O" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
#     "Pel" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"] + general.kata_sifat + ["Adv AdjP"] + general.numeralia + ["NumP Num", "NumP Noun"] + general.kata_kerja + ["Adv VP"] + ["Prep NP"] + ["NP VP"],
#     "Ket" : ["Prep NP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "Num PNP"],
#     "NP" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
#     "VP" : general.kata_kerja + ["Adv VP"],
#     "AdjP" : general.kata_sifat + ["Adv AdjP"],
#     "PP" : ["PrepNP"],
#     "NumP" : general.numeralia + ["NumP Num", "NumP Noun"],
#     "Verb" : general.kata_kerja,
#     "Noun" : general.kata_benda,
#     "Adj" : general.kata_sifat,
#     "Adv" : general.kata_keterangan,
#     "Num" : general.numeralia,
#     "Prep" : general.preposisi,
#     "PropNoun" : general.proper_noun,
#     "Pronoun" : general.kata_ganti
# }

# K → S P
# K → S P O
# K → S P Pel
# K → S P O Pel
# K → S P Ket
# K → S P O Ket

# Rule Gabungan : 
# S → NP  
# P → VP  | AdjP
# O → NP 
# Pel → AdjP | PP  
# Ket → PP
# NP → PropNoun | NP Noun  | Pronoun  | Noun | Num NP | NP ProNoun | NP PropNoun 
# VP → Verb | Adv VP |  AdjP VP
# AdjP → Adj | Adv AdjP | Adj Adv | Adj Pronoun
# PP → Prep NP | Prep AdjP | Prep Num
import general
production = {
    "K" : ['S P','O P','S Ket','O Ket','S P Pel','S P Ket','O P Pel','O P Ket','S P O','S P S','O P S','O P O','S P O Pel','O P O Pel','O P S Pel','S P S Pel','S P O Ket','O P O Ket','O P S Ket','S P S Ket'],
    "S" : ['NP'],
    "P" : ['VP','AdjP'],
    "O" : ['NP'],
    "Pel" : ['AdjP', 'PP'],
    "Ket" : ['PP','AdjP'],
    "NP" : ['PropNoun','NP Noun','Pronoun','Noun','Num NP','NP Pronoun','NP PropNoun'],
    "VP" : ['Verb','Adv VP','AdjP VP'],
    "AdjP" : ['Adj','Adv AdjP','Adj Adv','Adj Pronoun','Adj Noun'],
    "PP" : ["Prep NP",'Prep AdjP','Prep Num','Prep'],
    "Verb" : general.kata_kerja,
    "Noun" : general.kata_benda,
    "Adj" : general.kata_sifat,
    "Adv" : general.kata_keterangan,
    "Num" : general.numeralia,
    "Prep" : general.preposisi,
    "PropNoun" : general.proper_noun,
    "Pronoun" : general.kata_ganti
}
main_production = {
    "S" : ['NP'],
    "P" : ['VP','AdjP'],
    "O" : ['NP'],
    "Pel" : ['AdjP', 'PP'],
    "Ket" : ['PP']
}
variable = list(production.keys())
start_symbol = ["K"]
def check_production(array):
    sum = []
    for i in array:
        for j in variable:
            if i in production[j]:
                sum.append(j)
    return sum

def check_symbol(array):
    for i in array:
        if i in start_symbol:
            return True
    return False
