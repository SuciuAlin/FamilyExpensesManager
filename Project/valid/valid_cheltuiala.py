from model.cheltuiala import get_zi_cheltuiala, get_tip_cheltuiala,\
    get_suma_cheltuiala

def validare_numar(inp):
    #verifica ca variabila sa fie int
    #citeste din nou de la tastatura daca nu e
    #input: string 
    #output: int
    while True:
            try:
                return int(inp)
            except:
                inp = input("introdu un numar:")
                




def valideaza_cheltuiala(c):
    #input: cheltuiala c
    #output: raise Exception
    erori = ""
    if validare_numar(get_zi_cheltuiala(c)) < 0 or validare_numar(get_zi_cheltuiala(c)) > 31:
        erori += "zi invalida!\n"
    if get_suma_cheltuiala(c) < 0:
        erori += "suma invalida!\n"
    if get_tip_cheltuiala(c) != "mancare" and get_tip_cheltuiala(c) != "intretinere" and get_tip_cheltuiala(c) != "imbracaminte" and get_tip_cheltuiala(c) != "telefon" and get_tip_cheltuiala(c) != "altele":
        erori += "tip invalid!\n"
    if len(erori) > 0:
        raise Exception(erori)
