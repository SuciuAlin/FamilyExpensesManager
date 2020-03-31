from model.cheltuiala import *
from valid.valid_cheltuiala import valideaza_cheltuiala
from repo.repo_cheltuiala import repo_adauga_cheltuiala
from test.support import swap_item



def adauga_cheltuiala(zi,suma,tip,cheltuieli):
    #adauga o cheltuiala formata din zi, suma si tip la lista de cheltuieli dupa ce 
    #verifica ca aceasta e valida 
    c = creeaza_cheltuiala(zi,suma,tip)
    
    valideaza_cheltuiala(c)
    
    #print("Cheltuiala nu e valida")
    
    repo_adauga_cheltuiala(zi,suma,tip,cheltuieli)

#revazut
#de facut la fel pentru toate stergerile si updateurile??
#stergere
def sterge_cheltuieli_pentru_zi(cheltuieli,zi):
    
    #2.a.
    #sterge cheltuielile ce sunt facute in aceeasi zi cu ziua data
    #input: cheltuieli - lista de dictionare, zi - int
    #output: lista de dictionare cu elementele ce respecta regula
    ok = True
    while ok:
        ok = False
        for c in cheltuieli:
            if get_zi_cheltuiala(c) == zi:
                cheltuieli.remove(c)
                ok = True

                

def sterge_cheltuieli_zi_inceput_sfarsit(cheltuieli,inceput,sfarsit):
    #2.b.
    #sterge cheltuielile ce sunt facute in intervalul format din zilele inceput si sfarsit
    #input: cheltuieli - lista de dictionare, inceput - int, sfarsit -int
    #output: lista de dictionare cu elementele ce respecta regula
    ok = True
    while ok:
        ok = False
        for c in cheltuieli:
            if get_zi_cheltuiala(c)>= inceput and get_zi_cheltuiala(c) <= sfarsit:
                cheltuieli.remove(c)
                ok = True


def sterge_cheltuieli_de_tip_x(cheltuieli,tip_x):
    #2.c.
    #sterge cheltuielile ce sunt facute de acelasi tip cu tipul dat
    #input: cheltuieli - lista de dictionare, tip_x - string
    #output: lista de dictionare cu elementele ce respecta regula
    ok = True
    while ok:
        ok = False
        for c in cheltuieli:
            if get_tip_cheltuiala(c) == tip_x:
                cheltuieli.remove(creeaza_cheltuiala(get_zi_cheltuiala(c),get_suma_cheltuiala(c),get_tip_cheltuiala(c)))
                ok = True


def mai_mare_decat_suma(cheltuieli,suma):
    #cauta cheltuielile ce au suma mai mare decat cea data
    #input: lista cheltuielilor, suma - int
    #output: array cu cheltuielile ce respecta conditia
    cheltuieli_bune = []
    for c in cheltuieli:
        if suma < get_suma_cheltuiala(c):
            adauga_cheltuiala(get_zi_cheltuiala(c),get_suma_cheltuiala(c),get_tip_cheltuiala(c),cheltuieli_bune)
    return cheltuieli_bune


def inainte_zi_si_mai_mic_decat_suma(cheltuieli,zi,suma):
    #3.b.
    #afiseaza cheltuielile ce au ziua si suma mai mici decat cele date
    #input: cheltuieli - lista de dictionare, zi - int, suma - int
    #output: lista de dictionare cu elementele ce respecta regula
    lista_buna = []
    for c in cheltuieli:
        if get_zi_cheltuiala(c) < zi and get_suma_cheltuiala(c) < suma:
            adauga_cheltuiala(get_zi_cheltuiala(c),get_suma_cheltuiala(c),get_tip_cheltuiala(c),lista_buna)
    return lista_buna


def e_tip_cheltuiala(cheltuieli,tip):
    #3.c.
    #returneaza cheltuielile ce au acelasi tip cu cel dat
    #input: cheltuieli - lista de dictionare, tip - string
    #output: lista de dictionare cu elementele ce respecta regula
    lista_buna = []
    for c in cheltuieli:
        if tip == get_tip_cheltuiala(c):
            adauga_cheltuiala(get_zi_cheltuiala(c),get_suma_cheltuiala(c),get_tip_cheltuiala(c),lista_buna)
    return lista_buna


def suma_totala_pentru_tip(cheltuieli,tip):
    #returneaza cheltuielile ce au acelasi tip cu cel dat
    #input: cheltuieli - lista de dictionare, tip - string
    #output: suma tuturor cheltuielilor de tipul dat
    suma = 0
    for c in cheltuieli:
        if get_tip_cheltuiala(c) == tip:
            suma += get_suma_cheltuiala(c)
    return suma


def zi_cu_suma_maxima(cheltuieli):
    #4.b.
    #returneaza cheltuielile ce au acelasi tip cu cel dat
    #input: cheltuieli - lista de dictionare
    #output: int(ziua) cu cea mai mare suma cheltuita
    zi_maxima = 0
    suma_maxima = 0
    for c in cheltuieli:
        if get_suma_cheltuiala(c) > suma_maxima:
            zi_maxima = get_zi_cheltuiala(c)
            suma_maxima = get_suma_cheltuiala(c)
    if zi_maxima == 0:
        return None
    else:
        return zi_maxima


def cheltuieli_cu_suma_x(cheltuieli,suma_x):
    #returneaza cheltuielile ce au acelasi tip cu cel dat
    #input: cheltuieli - lista de dictionare, suma_x - int
    #output: lista cheltuielilor cu suma_x  
    lista_buna = []
    for c in cheltuieli:
        if get_suma_cheltuiala(c) == suma_x:
            adauga_cheltuiala(get_zi_cheltuiala(c),get_suma_cheltuiala(c),get_tip_cheltuiala(c),lista_buna)
    return lista_buna


def cheltuieli_sortat_dupa_tip(cheltuieli):
    #altele, întreținere, îmbrăcăminte,mâncare, telefon
    #input: cheltuieli - lista de dictionare,
    #output: lista de dictionare sortate dupa tip
    ok = 1
    while ok:
        ok = 0
        for i in range(0,len(cheltuieli)-1):
            if get_tip_cheltuiala(cheltuieli[i]) > get_tip_cheltuiala(cheltuieli[i+1])  :      
                aux = cheltuieli[i]
                cheltuieli[i] = cheltuieli[i+1]
                cheltuieli[i+1] = aux
                ok = 1
         
            
            
    return cheltuieli


#filtrare
def filtrare_cheltuieli_de_tip_x(cheltuieli,tip_x):
    #5.a
    #sterge cheltuielile ce sunt de tipul x
    #input: cheltuieli - lista de dictionare, tip_x - string
    #output: lista de dictionare cu elementele ramase
    ok = True
    while ok:
        ok = False
        for c in cheltuieli:
            if get_tip_cheltuiala(c) == tip_x:
                ok = True
                cheltuieli.remove(c)


def filtrare_cheltuieli_mai_mare_decat_suma(cheltuieli,suma):
    #5.b
    #sterge cheltuielile ce sunt mai mici decat suma data
    #input: cheltuieli - lista de dictionare, suma - int
    #output: lista de dictionare cu elementele ce respecta regula
    ok = True
    while ok:
        ok = False
        for c in cheltuieli:
            if get_suma_cheltuiala(c) <= suma:
                ok = True
                cheltuieli.remove(c)


def adauga_stare_lista(lista,cheltuieli):
    #adauga lista de cheltieli curenta la lista istoricului de lista daca e diferita de ultima lista
    #input: lista- lista de cheltuieli,cheltuieli - lista de dictionare
    #output: lista de liste modificata daca e cazul
    if len(lista)>0 and lista[-1] == cheltuieli:
        return
    else:    
        lista.append(cheltuieli.copy())
        
    
def sterge_ultima_stare(lista):
    #sterge ultima lista memorata in lista de liste
    #input: lista de liste
    #output: lista de liste modificata
    lista.pop(len(lista)-1)
    
def undo(lista): 
    #sterge ultima lista memorata in lista de liste
    #input: lista de liste
    #output: ultima lista ramasa
    sterge_ultima_stare(lista)
    if not lista:
        return []
    else:
        return lista[-1]
    
    
