from ui.ui_cheltuiala import    citire_functionalitate
from service.svr_cheltuiala import *
from tests.tests import all_tests
import ui


def main():
    
    """Program principal"""
    #Asta este subrutina principala a programului
    #input:
    #output:
    lista = []
    lista_cheltuieli = []
    #adauga_cheltuiala(23, 23, "imbracaminte", lista_cheltuieli)
    #adauga_cheltuiala(9, 43, "mancare", lista_cheltuieli)
    #adauga_cheltuiala(7, 53, "altele", lista_cheltuieli)
    #adauga_cheltuiala(7, 27, "imbracaminte", lista_cheltuieli)
    #adauga_cheltuiala(3, 223, "imbracaminte", lista_cheltuieli)
    #selector_parametrii(input())
    
    #citire_functionalitate(lista,lista_cheltuieli)
    ui(lista_cheltuieli,lista)
    
    print(lista_cheltuieli)
    
all_tests()    
main()