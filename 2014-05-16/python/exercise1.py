import os,sys
sys.path.insert(0, 'C:/Users/Davide/lar-cc/lib/py/')

from scipy import *
from splines import *
from sysml import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *


DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAWS = COMP([VIEW,SKEL_1,STRUCT,MKPOLS]) 
DRSM = COMP([STRUCT,MKPOLS])

def numbers_faces(model):
    hpc = SKEL_1(STRUCT(MKPOLS(model)))
    return cellNumbering (model,hpc)(range(len(model[1])),RED,1)


def insert_into_cell(obg,model,lista):
    for k in lista:
        model = diagram2cell(obg,model,k)
    return model


"""NOTA IMPORTANTISSIMA: IO ED ALCUNI DEI MIEI COLLEGHI, AGGIORNANDO IL LAR, ABBIAMO RISCONTRATO ALCUNI PROBLEMI NELL'ESEGUIRE IL 
                         TEST04.PY, ED IN PARTICOLARE NELL'ISTRUZIONE MKPOL AL MOMENTO CUI SI APPLICA IL toMERGE, PERCIO NON POTRO
                         AVERE IL VANTAGGIO DI CAPIRE COME PUO ESSERE SFRUTTATO IL MERGE....."""
                         
                         

"""PRATO INIZIALMENTE A DEFINIRE UNO SCHEMA TOP LEVEL COMPOSTO DA UNA SERIE DI BLOCCHI COME SUGGERIVA IL TESTO (ALMENO IO COSI HO CAPITO)"""
shape = [1,3,2]
sizePatterns = [[20],[5,2,8],[0.1,4]]
master_apartment = assemblyDiagramInit(shape)(sizePatterns)
V,CV = master_apartment


hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)





#INSERISCO LA PRIMA PARTE DELL'APPARTAMENTO
part_apartment_1 = assemblyDiagramInit([11,3,1])([[0.1,1.99,1,2,1,1,1,5,2,4.9,0.1],[0.1,5,0.1],[4]])
hpc_ap_1 = numbers_faces(part_apartment_1)
#@VIEW(hpc_ap_1)

"""inserisco part_apartment_1 in master_apartment"""
master_apartment = diagram2cell(part_apartment_1,master_apartment,1)
#DRAWS(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)



#INSERISCO LA SECONDA PARTE DELL APPARTAMENTO
part_apartment_2 = assemblyDiagramInit([7,3,1])([[0.1,8.9,1,5,2,2.9,0.1],[0.1,7.9,0.1],[4]])
hpc_ap_2 = numbers_faces(part_apartment_2)
#VIEW(hpc_ap_2)


"""inserisco part_apartment_2 in master_apartment"""
master_apartment = diagram2cell(part_apartment_2,master_apartment,4)
#DRAWS(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)




#INSERISCO LA TERZA PARTE DELL APPARTAMENTO
part_apartment_3 = assemblyDiagramInit([3,1,1])([[0.1,19.8,0.1],[2],[4]])
hpc_ap_3 = numbers_faces(part_apartment_3)
#VIEW(hpc_ap_3)



"""inserisco part_apartment_2 in master_apartment"""
master_apartment = diagram2cell(part_apartment_3,master_apartment,2)
#DRAWS(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)


"""ora elimino alcune componenti"""
V,CV = master_apartment
toRemove = [7,13,19,25,31,8,39,40,46,52,58]
master_apartment = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master_apartment)

hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)


"""definisco una componente per definire le porte"""
door = assemblyDiagramInit([3,1,2])([[1,1,1],[0.01],[3,1]])
hpc_d = numbers_faces(door)
#VIEW(hpc_d)
V,CV = door
door = V,[cell for k,cell in enumerate(CV) if not (k in [2])]
#DRAW(door)

"""inserisco door in diversi punti"""
master_apartment =  insert_into_cell(door,master_apartment,[42,37,26,21,16,11])
#DRAW(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)


"""definisco una componente per definire le finestre"""
window = assemblyDiagramInit([3,1,3])([[1,1,1],[0.01],[1,1,1]])
hpc_w = numbers_faces(window)
#VIEW(hpc_w)
V,CV = window
window = V,[cell for k,cell in enumerate(CV) if not (k in [4])]
#DRAW(window)


"""inserisco window in diversi punti"""
master_apartment =  insert_into_cell(window,master_apartment,[37,33,22,18,14,10])
#DRAW(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)

"""altro elemento di finestre"""
windows_double = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
hpc_wd = numbers_faces(windows_double)
#VIEW(hpc_wd)
V,CV = windows_double
windows_double = V,[cell for k,cell in enumerate(CV) if not (k in [4,10])]


"""inserisco le 2 finestre in master"""
master_apartment =  insert_into_cell(windows_double,master_apartment,[25])
#DRAW(master_apartment)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)

master_apartment_c = COLOR([0.9686,0.9098,0.6235])(DRSM(master_apartment))
#VIEW(master_apartment_c)




