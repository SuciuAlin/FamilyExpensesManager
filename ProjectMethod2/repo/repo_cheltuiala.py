#CRUD
#Create, Read, Update, Delete
from model.cheltuiala import creeaza_cheltuiala, get_suma_cheltuiala,\
    get_tip_cheltuiala, get_zi_cheltuiala, set_zi_cheltuiala,\
    set_suma_cheltuiala, set_tip_cheltuiala


def repo_adauga_cheltuiala(zi,suma,tip,cheltuieli):
    #functie care adauga o cheltuiala formata din zi,suma si tip la lista cheltuieli
    #input: zi - integer, suma - integer, tip - string , cheltuieli - lista de cheltuieli
    cheltuieli.append(creeaza_cheltuiala(zi, suma, tip))
#revazut


def actualizeaza_cheltuiala(zi_v,suma_v,tip_v,zi_n,suma_n,tip_n,cheltuieli):
    #functie care modifica valorile unei cheltuieli date
    #input : zi_v,suma_v,tip_v - valorile vechi ale cheltuielii; zi_n,suma_n,tip_n - valorile noi ale cheltuielii
    #output: -
    for c in cheltuieli:
        if zi_v == get_zi_cheltuiala(c) and suma_v == get_suma_cheltuiala(c) and tip_v == get_tip_cheltuiala(c):
            set_zi_cheltuiala(c, zi_n)
            set_suma_cheltuiala(c, suma_n)
            set_tip_cheltuiala(c, tip_n)


