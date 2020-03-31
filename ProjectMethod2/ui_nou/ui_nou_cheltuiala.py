from valid.valid_cheltuiala import validare_numar
from service.svr_cheltuiala import adauga_cheltuiala,\
    sterge_cheltuieli_zi_inceput_sfarsit, filtrare_cheltuieli_de_tip_x, undo,\
    adauga_stare_lista, e_tip_cheltuiala

def tipareste_e_tip_cheltuiala(cheltuieli,tip):
    print(e_tip_cheltuiala(cheltuieli,tip))


def ui(cheltuieli,lista):
    #x = input("text")
    txt = "adauga_cheltuiala 7 2 mancare ,  adauga_cheltuiala 8 2 altele,adauga_cheltuiala 1 2 altele,filtrare_cheltuieli_de_tip_x altele,adauga_cheltuiala 1 9 mancare, undo, undo, undo"

    x = txt.split(",")
    for comanda in x:
        cmd = comanda.split()
        if cmd:
            print(cmd)
            if cmd[0] == "adauga_cheltuiala":
                adauga_cheltuiala(int(cmd[1]), int(cmd[2]), cmd[3], cheltuieli)
                adauga_stare_lista(lista,cheltuieli)
            elif cmd[0] == "sterge_cheltuieli_zi_inceput_sfarsit":  
                sterge_cheltuieli_zi_inceput_sfarsit(cheltuieli, int(cmd[1]), int(cmd[2])) 
                adauga_stare_lista(lista,cheltuieli)
            elif cmd[0] == "filtrare_cheltuieli_de_tip_x":       
                filtrare_cheltuieli_de_tip_x(cheltuieli, cmd[1])
                adauga_stare_lista(lista,cheltuieli)
             
            elif cmd[0] == "tipareste_e_tip_cheltuiala":
                tipareste_e_tip_cheltuiala(cheltuieli, cmd[1])
            elif cmd[0] == "undo":
                cheltuieli = undo(lista)
                print(cheltuieli)
    return cheltuieli    
                
cheltuieli = []  
lista = []  
cheltuieli = ui(cheltuieli,lista)
print(cheltuieli)




