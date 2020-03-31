from model.cheltuiala import creeaza_cheltuiala, get_zi_cheltuiala,\
    get_suma_cheltuiala, get_tip_cheltuiala

from service.svr_cheltuiala import *
    
    
from repo.repo_cheltuiala import actualizeaza_cheltuiala

def test_creeaza_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1,3,"telefon")
    assert(get_zi_cheltuiala(cheltuiala)==1)
    assert (get_suma_cheltuiala(cheltuiala)== 3)
    assert (get_tip_cheltuiala(cheltuiala) == "telefon")
    cheltuiala = creeaza_cheltuiala(2,3,"mancare")
    assert(get_zi_cheltuiala(cheltuiala)==2)
    assert (get_suma_cheltuiala(cheltuiala) == 3)
    assert (get_tip_cheltuiala(cheltuiala) == "mancare")



def test_adauga_cheltuiala():
    lista_cheltuieli = []
    adauga_cheltuiala(1,3,"intretinere",lista_cheltuieli)
    assert(get_zi_cheltuiala(lista_cheltuieli[0])==1)
    assert(get_tip_cheltuiala(lista_cheltuieli[0])=="intretinere")
    adauga_cheltuiala(2,40,"imbracaminte",lista_cheltuieli)
    assert (get_zi_cheltuiala(lista_cheltuieli[0]) == 1)
    assert (get_tip_cheltuiala(lista_cheltuieli[0])== "intretinere")
    assert (get_suma_cheltuiala(lista_cheltuieli[1]) == 40)
    assert (get_tip_cheltuiala(lista_cheltuieli[1])== "imbracaminte")

    
def test_actualizeaza_cheltuiala():
    zi_v = 1
    suma_v = 2
    tip_v = "mancare"
    zi_n = 4
    suma_n = 14
    tip_n = "imbracaminte"
    lista_cheltuieli = []
    adauga_cheltuiala(zi_v,suma_v,tip_v,lista_cheltuieli)
    actualizeaza_cheltuiala(zi_v,suma_v,tip_v,zi_n,suma_n,tip_n,lista_cheltuieli)
    assert (get_zi_cheltuiala(lista_cheltuieli[0])==zi_n)
    assert (get_zi_cheltuiala(lista_cheltuieli[0])==zi_n)
    assert (get_zi_cheltuiala(lista_cheltuieli[0])==zi_n)
    actualizeaza_cheltuiala(zi_n,suma_n,tip_n,zi_v,suma_n,tip_v,lista_cheltuieli)
    assert (get_zi_cheltuiala(lista_cheltuieli[0])==zi_v)
    assert (get_suma_cheltuiala(lista_cheltuieli[0])==suma_n)
    assert (get_tip_cheltuiala(lista_cheltuieli[0])==tip_v)
    

#cautari
def test_mai_mare_decat_suma():
    lista_cheltuieli = []
    zi_1 = 3
    suma_1 = 33
    tip_1 = "mancare"
    zi_2 =2
    suma_2 = 32
    tip_2 = "imbracaminte"
    zi_3 = 31
    suma_3 = 456
    tip_3 = "telefon"

    adauga_cheltuiala(zi_1, suma_1, tip_1,lista_cheltuieli)
    adauga_cheltuiala(zi_2, suma_2, tip_2,lista_cheltuieli)
    adauga_cheltuiala(zi_3, suma_3, tip_3,lista_cheltuieli)

    suma_mai_mare_decat = 32

    lista_buna = []
    adauga_cheltuiala(zi_1,suma_1,tip_1,lista_buna)
    adauga_cheltuiala(zi_3,suma_3,tip_3,lista_buna)
    # de intrebat daca asta e metoda optima de a face testul
    assert (mai_mare_decat_suma(lista_cheltuieli,suma_mai_mare_decat) == lista_buna)


#stergere
def test_sterge_cheltuieli_pentru_zi():
    lista_cheltuieli = []
    lista_buna = []
    zi = 7
    adauga_cheltuiala(23,23,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(9,43,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(7,53,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(7,27,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(3,223,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(23,23,"imbracaminte",lista_buna)
    adauga_cheltuiala(9,43,"imbracaminte",lista_buna)
    adauga_cheltuiala(3,223,"imbracaminte",lista_buna)
    sterge_cheltuieli_pentru_zi(lista_cheltuieli,zi)
    assert (lista_cheltuieli == lista_buna)
    adauga_cheltuiala(11,11,"mancare",lista_cheltuieli)
    zi = 11
    sterge_cheltuieli_pentru_zi(lista_cheltuieli,zi)
    assert (lista_cheltuieli == lista_buna)


def test_sterge_cheltuieli_de_tip_x():
    lista_cheltuieli = []
    lista_buna = []
    tip_x = "imbracaminte"
    adauga_cheltuiala(2, 5, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_buna)
    adauga_cheltuiala(5, 6, "telefon", lista_buna)
    assert (lista_cheltuieli != lista_buna)
    sterge_cheltuieli_de_tip_x(lista_cheltuieli,tip_x)
    assert (lista_cheltuieli == lista_buna)
    adauga_cheltuiala(3, 33, "intretinere", lista_cheltuieli)
    adauga_cheltuiala(8, 5, "intretinere", lista_cheltuieli)
    tip_x = "intretinere"
    sterge_cheltuieli_de_tip_x(lista_cheltuieli,tip_x)
    adauga_cheltuiala(8, 5, "altele", lista_cheltuieli)
    adauga_cheltuiala(8, 5, "altele", lista_buna)
    adauga_cheltuiala(23, 33, "intretinere", lista_cheltuieli)
    sterge_cheltuieli_de_tip_x(lista_cheltuieli,tip_x)
    assert (lista_cheltuieli == lista_buna)


def test_sterge_cheltuieli_zi_inceput_sfarsit():
    lista_cheltuieli = []
    lista_buna = []
    zi_inceput = 4
    zi_sfarsit = 10
    adauga_cheltuiala(2, 5, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    adauga_cheltuiala(2, 5, "imbracaminte", lista_buna)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_buna)
    assert (lista_cheltuieli != lista_buna)
    sterge_cheltuieli_zi_inceput_sfarsit(lista_cheltuieli, zi_inceput, zi_sfarsit)
    assert (lista_cheltuieli == lista_buna)
    adauga_cheltuiala(3, 33, "intretinere", lista_cheltuieli)
    adauga_cheltuiala(8, 5, "intretinere", lista_cheltuieli)
    adauga_cheltuiala(3, 33, "intretinere", lista_buna)
    sterge_cheltuieli_zi_inceput_sfarsit(lista_cheltuieli, zi_inceput, zi_sfarsit)
    adauga_cheltuiala(8, 5, "altele", lista_cheltuieli)
    adauga_cheltuiala(23, 33, "intretinere", lista_cheltuieli)
    adauga_cheltuiala(23, 33, "intretinere", lista_buna)
    sterge_cheltuieli_zi_inceput_sfarsit(lista_cheltuieli, zi_inceput, zi_sfarsit)
    assert (lista_cheltuieli == lista_buna)


def test_inainte_zi_si_mai_mic_decat_suma():
    lista_cheltuieli = []
    zi = 6
    suma = 5
    adauga_cheltuiala(2, 3, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    adauga_cheltuiala(3, 33, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(8, 2, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(6, 7, "telefon", lista_cheltuieli)
    lista_buna = []
    adauga_cheltuiala(2, 3, "imbracaminte", lista_buna)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_buna)
    assert (inainte_zi_si_mai_mic_decat_suma(lista_cheltuieli,zi,suma) == lista_buna)


def test_e_tip_cheltuiala():
    lista_cheltuieli = []
    tip = "imbracaminte"
    adauga_cheltuiala(2,3,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(3,4,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(4,5,"mancare",lista_cheltuieli)
    adauga_cheltuiala(5,6,"telefon",lista_cheltuieli)
    adauga_cheltuiala(3,33,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(8,2,"imbracaminte",lista_cheltuieli)
    adauga_cheltuiala(6,7,"telefon",lista_cheltuieli)
    lista_buna = []
    adauga_cheltuiala(2,3,"imbracaminte",lista_buna)
    adauga_cheltuiala(3,4,"imbracaminte",lista_buna)
    adauga_cheltuiala(3,33,"imbracaminte",lista_buna)
    adauga_cheltuiala(8,2,"imbracaminte",lista_buna)
    assert (e_tip_cheltuiala(lista_cheltuieli,tip) == lista_buna)


#rapoarte
def test_suma_totala_pentru_tip():
    lista_cheltuieli = []
    assert (suma_totala_pentru_tip(lista_cheltuieli,"imbracaminte") == 0)
    adauga_cheltuiala(2, 3, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    adauga_cheltuiala(3, 33, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(8, 2, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(6, 7, "telefon", lista_cheltuieli)
    suma = 3+4+33+2
    assert (suma_totala_pentru_tip(lista_cheltuieli,"imbracaminte") == suma)


def test_zi_cu_suma_maxima():
    lista_cheltuieli = []
    assert (zi_cu_suma_maxima(lista_cheltuieli) == None)
    adauga_cheltuiala(2, 3, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    assert (zi_cu_suma_maxima(lista_cheltuieli)==5)
    adauga_cheltuiala(3, 33, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(8, 2, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(6, 7, "telefon", lista_cheltuieli)
    assert (zi_cu_suma_maxima(lista_cheltuieli)==3)


def test_cheltuieli_cu_suma_x():
    lista_cheltuieli = []
    suma_x = 5
    lista_buna = []
    assert(cheltuieli_cu_suma_x(lista_cheltuieli,suma_x) == lista_buna)
    adauga_cheltuiala(2, 5, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(5, 6, "telefon", lista_cheltuieli)
    adauga_cheltuiala(2, 5, "imbracaminte", lista_buna)
    adauga_cheltuiala(4, 5, "mancare", lista_buna)
    assert (cheltuieli_cu_suma_x(lista_cheltuieli,suma_x) == lista_buna)
    adauga_cheltuiala(3, 33, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(8, 5, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(8, 5, "imbracaminte", lista_buna)
    adauga_cheltuiala(6, 7, "telefon", lista_cheltuieli)
    assert (cheltuieli_cu_suma_x(lista_cheltuieli,suma_x) == lista_buna)


def test_tipareste_cheltuieli_sortat_dupa_tip():
    lista_cheltuieli = []
    lista_buna = []
    assert(cheltuieli_sortat_dupa_tip(lista_cheltuieli) == lista_buna)
    adauga_cheltuiala(2, 5, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(2, 5, "imbracaminte", lista_buna)
    adauga_cheltuiala(3, 4, "imbracaminte", lista_buna)
    adauga_cheltuiala(4, 5, "mancare", lista_cheltuieli)
    adauga_cheltuiala(4, 5, "mancare", lista_buna)
    lista_buna2 = cheltuieli_sortat_dupa_tip(lista_cheltuieli)
    assert (lista_buna2 == lista_buna)


#filtrare
def test_filtrare_cheltuieli_de_tip_x():
    lista_cheltuieli = []
    lista_buna = []
    tip = "imbracaminte"
    adauga_cheltuiala(23, 23, "mancare", lista_cheltuieli)
    adauga_cheltuiala(9, 43, "mancare", lista_cheltuieli)
    adauga_cheltuiala(7, 53, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(7, 27, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 223, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(23, 23, "mancare", lista_buna)
    adauga_cheltuiala(9, 43, "mancare", lista_buna)
    filtrare_cheltuieli_de_tip_x(lista_cheltuieli,tip)
    assert (lista_cheltuieli == lista_buna)
    adauga_cheltuiala(11, 11, "altele", lista_cheltuieli)
    tip = "altele"
    filtrare_cheltuieli_de_tip_x(lista_cheltuieli,tip)
    assert (lista_cheltuieli == lista_buna)


def test_filtrare_cheltuieli_mai_mare_decat_suma():
    lista_cheltuieli = []
    lista_buna = []
    suma = 52
    adauga_cheltuiala(23, 23, "mancare", lista_cheltuieli)
    adauga_cheltuiala(9, 43, "mancare", lista_cheltuieli)
    adauga_cheltuiala(7, 53, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(7, 27, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(3, 223, "imbracaminte", lista_cheltuieli)
    adauga_cheltuiala(7, 53, "imbracaminte", lista_buna)
    adauga_cheltuiala(3, 223, "imbracaminte", lista_buna)
    filtrare_cheltuieli_mai_mare_decat_suma(lista_cheltuieli,suma)
    assert (lista_cheltuieli == lista_buna)
    adauga_cheltuiala(11, 11, "altele", lista_cheltuieli)
    suma = 20
    filtrare_cheltuieli_mai_mare_decat_suma(lista_cheltuieli,suma)
    assert (lista_cheltuieli == lista_buna)



def all_tests():
    test_creeaza_cheltuiala()
    test_adauga_cheltuiala()
    test_actualizeaza_cheltuiala()
    test_mai_mare_decat_suma()
    test_inainte_zi_si_mai_mic_decat_suma()
    test_e_tip_cheltuiala()
    test_suma_totala_pentru_tip()
    test_zi_cu_suma_maxima()
    test_cheltuieli_cu_suma_x()
    test_sterge_cheltuieli_de_tip_x()
    test_sterge_cheltuieli_pentru_zi()
    test_sterge_cheltuieli_zi_inceput_sfarsit()
    test_filtrare_cheltuieli_de_tip_x()
    test_filtrare_cheltuieli_mai_mare_decat_suma()
    test_tipareste_cheltuieli_sortat_dupa_tip()



