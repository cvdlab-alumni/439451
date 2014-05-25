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
from boolean1 import *
from architectural import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAWS = COMP([VIEW,SKEL_1,STRUCT,MKPOLS]) 
DRSM = COMP([STRUCT,MKPOLS])


#funzione che mi permette di numerare le celle
def numbers_faces(model):
    hpc = SKEL_1(STRUCT(MKPOLS(model)))
    return cellNumbering (model,hpc)(range(len(model[1])),RED,2)

#funzione che mi permette (passando in maniera opportuna la giusta lista) di inserire un sub_diagram in diverse celle del master
def insert_into_cell(obg,model,lista):
    for k in lista:
        model = diagram2cell(obg,model,k)
    return model

#funzione che trasla i vettori secondo gli assi definiti nella lista
def trasl_space(q,lista,assi):
    out = []
    for k in range(len(lista)):
        if (k) in assi:
            out = out+[lista[k]+q]
        else:
            out = out + [lista[k]]
    return out

#funzione che replica un oggetto lar tante volte quanto indicato nel secondo parametro per creare una serie di oggetti
#dello stesso tipo spaziati secondo il terzo parametro negli assi indicati nell'ultimo parametro. Tutto messo in un unico oggetto lar
#assi-> lista: [0]->x; [1]->y; [2]->z; [1,2]->x,y; [1,3]->x,z; [2,3]->y,z; [1,2,3]->x,y,z;
def larMoltiply(model,num,space,assi):
        V,CV = model
        aggV = [V]
        aggCV = [CV]
        for k in range(num-1):
            Vn =   [trasl_space(space,el,assi) for el in aggV[k]]
            aggV = aggV + [Vn]
            CVn =  [trasl_space(len(Vn),el,range(len(Vn))) for el in aggCV[k]]
            aggCV = aggCV + [CVn]
        V = CAT(aggV)
        CV = CAT(aggCV)
        return (V,CV)


#funzione che mi permette di colorare alcune celle del master con TEXTURE
def color_texture(diagram,text,cells):
    for k in cells:
        diagram[k] = TEXTURE(text)(diagram[k])
    return diagram


#funzione che mi permette di colorare alcune celle del master
def color_cells(diagram,values,cells):
    for k in cells:
        diagram[k] = COLOR([values[0]/255.0,values[1]/255.0,values[2]/255.0])(diagram[k])
    return diagram


"""NOTA IMPORTANTISSIMA: IO ED ALCUNI DEI MIEI COLLEGHI, AGGIORNANDO IL LAR, ABBIAMO RISCONTRATO ALCUNI PROBLEMI NELL'ESEGUIRE IL 
                         TEST04.PY, ED IN PARTICOLARE NELL'ISTRUZIONE MKPOL AL MOMENTO CUI SI APPLICA IL toMERGE, PERCIO NON POTRO
                         AVERE IL VANTAGGIO DI CAPIRE COME PUO ESSERE SFRUTTATO IL MERGE....."""
                         
                         

"""PARTO INIZIALMENTE A DEFINIRE UNO SCHEMA TOP LEVEL COMPOSTO DA UNA SERIE DI BLOCCHI COME SUGGERIVA IL TESTO (ALMENO IO COSI HO CAPITO)"""
shape = [1,5,1]
sizePatterns = [[20],[1.5,7,2,8,2],[5]]
master_apartment = assemblyDiagramInit(shape)(sizePatterns)
V,CV = master_apartment


hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)





#INSERISCO LA PRIMA PARTE DELL'APPARTAMENTO
part_apartment_1 = assemblyDiagramInit([11,3,2])([[0.2,1.98,1,2,1,1,1,5,2,4.8,0.2],[0.2,5,0.2],[0.3,4]])
hpc_ap_1 = numbers_faces(part_apartment_1)
#VIEW(hpc_ap_1)

"""inserisco part_apartment_1 in master_apartment"""
master_apartment = diagram2cell(part_apartment_1,master_apartment,1)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)



#INSERISCO LA SECONDA PARTE DELL APPARTAMENTO
part_apartment_2 = assemblyDiagramInit([7,3,2])([[0.2,8.8,1,5,2,2.8,0.2],[0.2,7.9,0.2],[0.3,4]])
hpc_ap_2 = numbers_faces(part_apartment_2)
#VIEW(hpc_ap_2)


"""inserisco part_apartment_2 in master_apartment"""
master_apartment = diagram2cell(part_apartment_2,master_apartment,2)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)




#INSERISCO LA TERZA PARTE DELL APPARTAMENTO
part_apartment_3 = assemblyDiagramInit([3,1,2])([[0.2,19.8,0.2],[2],[0.3,4]])
hpc_ap_3 = numbers_faces(part_apartment_3)
#VIEW(hpc_ap_3)



"""inserisco part_apartment_2 in master_apartment"""
master_apartment = diagram2cell(part_apartment_3,master_apartment,1)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)




"""ora ELIMINO alcune componenti"""
V,CV = master_apartment
toRemove = [113, 101, 89, 77,75, 59, 47, 35, 23, 11,13]
master_apartment = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)



"""ORA DEFINIAMO UN BALCONE PRINCIPALE"""
#definiamo 2 diagramm: uno di partenza per la base e l'altro per la ringhiera da inglobare tutto nel master_apartment
base_balcony = assemblyDiagramInit([5,3,4])([[0.1]*2+([19.6])+[0.1]*2,[1.8,0.1,0.1],[0.3,1.7,0.2,2]]) 
hpc_bb = numbers_faces(base_balcony)
#VIEW(hpc_bb)

V,CV = base_balcony 
base_balcony = V,[cell for k,cell in enumerate(CV) if not (k in [27,31,35,11,7,19,23,3,15,39,51,47,43,55,59,26,25,33,49,1])]
hpc_bb = numbers_faces(base_balcony)
#VIEW(hpc_bb)

#definisco una fascetta
fascia = (([[0,0,0],[0.2,0,0],[0.2,0.1,0],[0,0.1,0],[0,0,1.8],[0.2,0,1.8],[0.2,0.1,1.8],[0,0.1,1.8]],[range(8)]))
railing_balcony = larMoltiply(fascia,50,0.4,[0])

fascia = (([[0,0,0],[0.1,0,0],[0.1,0.2,0],[0,0.2,0],[0,0,1.8],[0.1,0,1.8],[0.1,0.2,1.8],[0,0.2,1.8]],[range(8)]))
railing_balcony_2 = larMoltiply(fascia,5,0.4,[1])  



"""inserisco railing_balcony  e railing_balcony_2 in base_balcony"""

base_balcony = diagram2cell(railing_balcony_2,base_balcony,24)
base_balcony = diagram2cell(railing_balcony,base_balcony,19)
base_balcony = diagram2cell(railing_balcony_2,base_balcony,9)
hpc_bb = numbers_faces(base_balcony)
#VIEW(hpc_bb)
V,CV = base_balcony
base_balcony =  V,[cell for k,cell in enumerate(CV) if not (k in [24,19,6,3,14,26,34,27,35,5,13,32])]



"""inserisco base_balcony in master_apartment"""
master_apartment = diagram2cell(base_balcony,master_apartment,1)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)






"""ORA DEFINIAMO UN BALCONE SECONDARIO"""
base_balcony_2 = assemblyDiagramInit([3,1,1])([[8.2,5,7.2],[1.5],[2]])
V,CV = base_balcony_2
base_balcony_2 = V,[cell for k,cell in enumerate(CV) if not (k in [0,2])]
hpc_bb2 = numbers_faces(base_balcony_2) 
#VIEW(hpc_bb2)

V,CV = base_balcony
Vn = scalePoints(V,[1,-1,1])
base_balcony = Vn,CV


"""inserisco base_balcony dentro a base_balcony_2"""
base_balcony_2 = diagram2cell(base_balcony,base_balcony_2,0)
hpc_bb2 = numbers_faces(base_balcony_2) 
#VIEW(hpc_bb2)


"""inserisco base_balcony_2 dentro a master_apartment"""
master_apartment = diagram2cell(base_balcony_2,master_apartment,0)
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)





"""definisco una componente per definire le porte"""
door = assemblyDiagramInit([3,1,2])([[0.8,1.4,0.8],[0.01],[3,1]])
hpc_d = numbers_faces(door)
#VIEW(hpc_d)
V,CV = door
door = V,[cell for k,cell in enumerate(CV) if not (k in [2])]
door_2 = assemblyDiagramInit([1,3,2])([[0.2],[0.4,2.2,0.4],[3,1]])
door_2 = door_2[0],[cell for k,cell in enumerate(door_2[1]) if not (k in [2])]


"""inserisco door e door_2 in diversi punti"""
master_apartment =  insert_into_cell(door_2,master_apartment,[99])
master_apartment =  insert_into_cell(door,master_apartment,[88,77, 68, 53, 42, 31, 20])
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)


"""definisco una componente per definire le finestre"""
window = assemblyDiagramInit([3,1,3])([[1,1,1],[0.01],[1,1,1]])
hpc_w = numbers_faces(window)
#VIEW(hpc_w)
V,CV = window
window = V,[cell for k,cell in enumerate(CV) if not (k in [4])]


"""inserisco window in diversi punti"""
master_apartment =  insert_into_cell(window,master_apartment,[84,47,27,17,7])
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)

"""altro elemento di finestre"""
windows_double = assemblyDiagramInit([7,1,3])([[1.5,0.9,0.2,0.9,0.4,0.8,0.3],[.3],[1,1.4,.3]])
hpc_wd = numbers_faces(windows_double)
#VIEW(hpc_wd)
V,CV = windows_double
windows_double = V,[cell for k,cell in enumerate(CV) if not (k in [4,10,15,16])]


"""inserisco le 2 finestre in master"""
master_apartment =  insert_into_cell(windows_double,master_apartment,[70,60,34])
hpc_ma = numbers_faces(master_apartment)
#VIEW(hpc_ma)

"""incomincio a colorare alcune parti"""
master_apartment_P = MKPOLS(master_apartment)


master_apartment_P = color_texture(master_apartment_P,'../images/muro.png',[3,48,54,80,86]+range(257,262)+range(297,354)+range(354,388))
master_apartment_P = color_texture(master_apartment_P,'../images/muro.png',[1,5,10,19,28,37,46,50,52,64,73,78])
master_apartment_P = color_texture(master_apartment_P,'../images/muro_bianco.png',[12,14,21,30,32,39,57,8,23,41,60,69,62,71]+range(262,272)+range(277,297))
master_apartment_P = color_cells(master_apartment_P,[210,105,30],range(110,172)+[56,82,90,91,95,96,97,88,93,100,101,103,105,106,108])
master_apartment_P = color_cells(master_apartment_P,[210,105,30],range(197,257)+[188,193,173,178,185,186,190,191,196,195,180,181,182,175,176])


apartment = STRUCT(master_apartment_P)
VIEW(apartment)




