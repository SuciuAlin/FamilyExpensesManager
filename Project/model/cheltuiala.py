def creeaza_cheltuiala(zi, suma, tip):
    #functie ce creeaza o cheltuiala
    #input: zi - integer, suma - integer, tip - string
    #output: cheltuiala - o cheltuiala
    return [zi,suma,tip]
 

#getter cheltuiala
def get_zi_cheltuiala(cheltuiala):
    return cheltuiala[0]


def get_suma_cheltuiala(cheltuiala):
    return cheltuiala[1]


def get_tip_cheltuiala(cheltuiala):
    return cheltuiala[2]


#setter
def set_zi_cheltuiala(cheltuiala,zi):
    cheltuiala[0] = zi


def set_suma_cheltuiala(cheltuiala,suma):
    cheltuiala[1] = suma


def set_tip_cheltuiala(cheltuiala,tip):
    cheltuiala[2] = tip
    
    