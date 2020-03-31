from service.svr_cheltuiala import *
from valid.valid_cheltuiala import validare_numar
from repo.repo_cheltuiala import actualizeaza_cheltuiala



def citire_ziua_suma_tip():
    ziua = validare_numar(input("ziua"))
    suma = validare_numar(input("suma"))
    dictionar = {"ziua":ziua,"suma":suma,"tip":input("tip")}
    return dictionar["ziua"], dictionar["suma"], dictionar["tip"]



def citire_ziua():
    ziua =  validare_numar(input("ziua"))
    return ziua


def citire_tip():
    tip = input("tip")
    return tip


def citire_suma():
    suma =  validare_numar(input("suma"))
    return suma

#cautari
def tipareste_mai_mare_decat_suma(cheltuieli,suma):
    #3.a.
    #afiseaza cheltuielile ce au suma mai mare decat suma data
    #input: cheltuieli - lista de dictionare, suma - int
    #output: lista de dictionare cu elementele ce respecta regula
    print(mai_mare_decat_suma(cheltuieli,suma))


def tipareste_inainte_zi_si_mai_mic_decat_suma(cheltuieli,zi,suma):
    print(inainte_zi_si_mai_mic_decat_suma(cheltuieli,zi,suma))


def tipareste_e_tip_cheltuiala(cheltuieli,tip):
    print(e_tip_cheltuiala(cheltuieli,tip))


def tipareste_suma_totala_pentru_tip(cheltuieli,tip):
    #4.a.
    print(suma_totala_pentru_tip(cheltuieli,tip))


def tipareste_zi_cu_suma_maxima(cheltuieli):
    print(zi_cu_suma_maxima(cheltuieli))


def tipareste_cheltuieli_cu_suma_x(cheltuieli,suma_x):
    print(cheltuieli_cu_suma_x(cheltuieli,suma_x))


def tipareste_cheltuieli_sortat_dupa_tip(cheltuieli):
    print(cheltuieli_sortat_dupa_tip(cheltuieli))


def selector_operatie(inp):
    #inp = numar _ litera
    #functii[numar][litera-ord('a')]
    numar1 = ord(inp[0])-ord('1')
    numar2 = ord(inp[2])-ord('a')
    functii = [[adauga_cheltuiala,actualizeaza_cheltuiala],[sterge_cheltuieli_pentru_zi,sterge_cheltuieli_zi_inceput_sfarsit,sterge_cheltuieli_de_tip_x],[tipareste_mai_mare_decat_suma,tipareste_inainte_zi_si_mai_mic_decat_suma,tipareste_e_tip_cheltuiala],[tipareste_suma_totala_pentru_tip,tipareste_zi_cu_suma_maxima,tipareste_cheltuieli_cu_suma_x,tipareste_cheltuieli_sortat_dupa_tip],[filtrare_cheltuieli_de_tip_x,filtrare_cheltuieli_mai_mare_decat_suma]]
    return functii[numar1][numar2]

def selector_parametrii(inp,cheltuieli):
    numar1 = ord(inp[0])-ord('1')
    numar2 = ord(inp[2])-ord('a')
    parametrii = [[[citire_ziua(),citire_suma(),citire_tip(),cheltuieli],[citire_ziua(),citire_suma(),citire_tip(),citire_ziua(),citire_suma(),citire_tip(),cheltuieli]]]
    #print(parametrii[numar1][numar2])
    #revazut
    #imi apeleaza toate functiile din lista parametrii
    return parametrii[numar1][numar2]


def parametrii(inp,cheltuieli):
    if len(inp) < 3:
        return
    a = inp[0]
    b = inp[2]
    if a == '1':
        if b == 'a':
            selector_operatie(inp)(*citire_ziua_suma_tip(), cheltuieli)
        elif b == 'b':
            selector_operatie(inp)(*citire_ziua_suma_tip(),*citire_ziua_suma_tip(), cheltuieli)
    elif a == '2':
        if b == 'a':
            selector_operatie(inp)(cheltuieli,citire_ziua())
        elif b == 'b':
            selector_operatie(inp)(cheltuieli,citire_ziua(),citire_ziua())
        elif b == 'c':
            selector_operatie(inp)(cheltuieli, citire_tip())
    elif a == '3':
        if b == 'a':
            selector_operatie(inp)(cheltuieli, citire_suma())
        elif b == 'b':
            selector_operatie(inp)(cheltuieli, citire_ziua(), citire_suma())
        elif b == 'c':
            selector_operatie(inp)(cheltuieli, citire_tip())
    elif a == '4':
        if b == 'a':
            selector_operatie(inp)(cheltuieli, citire_tip())
        elif b == 'b':
            selector_operatie(inp)(cheltuieli)
        elif b == 'c':
            selector_operatie(inp)(cheltuieli, citire_suma())
        elif b == 'd':
            selector_operatie(inp)(cheltuieli)
    elif a == '5':
        if b == 'a':
            selector_operatie(inp)(cheltuieli, citire_tip())
        elif b == 'b':
            selector_operatie(inp)(cheltuieli, citire_suma(), citire_tip())
    elif a == '6':
        if b == 'a':
            pass


def citire_functionalitate(lista,cheltuieli):
    x = "       \n\
                    Apasa 1.a pentru a adauga comanda\n\
                    Apasa 1.b pentru a actualiza o cheltuiala\n\
                    Apasa 2.a pentru a sterge cheltuielile dintr-o zi introdusa\n\
                    Apasa 2.b pentru a sterge cheltuielile dintr-un interval de zile introdus\n\
                    Apasa 2.c pentru a sterge cheltuielile de tipul introdus\n\
                    Apasa 3.a pentru a afisa cheltuielile mai_mari_decat_suma introdusa\n\
                    Apasa 3.b pentru a afisa cheltuielile inainte de ziua introdusa si mai mici decat suma introdusa\n\
                    Apasa 3.c pentru a afisa cheltuielile de acelasi tip ca si cel introdus\n\
                    Apasa 4.a pentru a tipari suma totala pentru un tip dat\n\
                    Apasa 4.b pentru a tipari ziua cu suma maxima\n\
                    Apasa 4.c pentru a tipari_cheltuielile cu o anumite suma\n\
                    Apasa 4.d pentru a tipari cheltuielile sortate după tip\n\
                    Apasa 5.a pentru a elimina toate cheltuielile de un anumit tip\n\
                    Apasa 5.b pentru a elimina toate cheltuielile mai mici decât o sumă dată\n\
                    Apasa 6.a pentru a reface ultima operație\n\
                    Apasa 7.a pentru a afisa din nou meniul\n\
                    Apasa 7.b pentru a iesi \n\
                    "
                

    while True:
        inp = input(x)

        if inp == "7.a":
            x = "       \n\
                    Apasa 1.a pentru a adauga comanda\n\
                    Apasa 1.b pentru a actualiza o cheltuiala\n\
                    Apasa 2.a pentru a sterge cheltuielile dintr-o zi introdusa\n\
                    Apasa 2.b pentru a sterge cheltuielile dintr-un interval de zile introdus\n\
                    Apasa 2.c pentru a sterge cheltuielile de tipul introdus\n\
                    Apasa 3.a pentru a afisa cheltuielile mai_mari_decat_suma introdusa\n\
                    Apasa 3.b pentru a afisa cheltuielile inainte de ziua introdusa si mai mici decat suma introdusa\n\
                    Apasa 3.c pentru a afisa cheltuielile de acelasi tip ca si cel introdus\n\
                    Apasa 4.a pentru a tipari suma totala pentru un tip dat\n\
                    Apasa 4.b pentru a tipari ziua cu suma maxima\n\
                    Apasa 4.c pentru a tipari_cheltuielile cu o anumite suma\n\
                    Apasa 4.d pentru a tipari cheltuielile sortate după tip\n\
                    Apasa 5.a pentru a elimina toate cheltuielile de un anumit tip\n\
                    Apasa 5.b pentru a elimina toate cheltuielile mai mici decât o sumă dată\n\
                    Apasa 6.a pentru a reface ultima operație\n\
                    Apasa 7.a pentru a afisa din nou meniul\n\
                    Apasa 7.b pentru a iesi \n\
                    "
        elif inp == "7.b":
            return
        elif inp == "6.a":
            cheltuieli = undo(lista)
        
        else:
            x = ""
            
            try:
                parametrii(inp, cheltuieli)
                adauga_stare_lista(lista, cheltuieli)
            except Exception as ex:
                print(ex)
                
                
                
