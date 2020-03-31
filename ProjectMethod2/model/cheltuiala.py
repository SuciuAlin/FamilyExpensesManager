def creeaza_cheltuiala(zi, suma, tip):
    #functie ce creeaza o cheltuiala
    #input: zi - integer, suma - integer, tip - string
    #output: cheltuiala - o cheltuiala
    return {"zi":zi,"suma":suma,"tip":tip}
 

#getter cheltuiala
def get_zi_cheltuiala(cheltuiala):
    return cheltuiala["zi"]


def get_suma_cheltuiala(cheltuiala):
    return cheltuiala["suma"]


def get_tip_cheltuiala(cheltuiala):
    return cheltuiala["tip"]

#setter
def set_zi_cheltuiala(cheltuiala,zi):
    cheltuiala["zi"] = zi


def set_suma_cheltuiala(cheltuiala,suma):
    cheltuiala["suma"] = suma


def set_tip_cheltuiala(cheltuiala,tip):
    cheltuiala["tip"] = tip
    
    