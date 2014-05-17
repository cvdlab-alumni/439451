'''
Created on 17/mag/2014

@author: Davide
'''


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


"""metodo enumerazione"""
#cellNumbering (larModel,hpcModel)

"""metodo fusione"""
#diagram2cell(diagram,master,cell)

"""metodo eliminazione"""
#V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]


"""creo una funzione che applica il ciclo fusione-enumerazione-fusione"""


#funzione di appoggio che mi consente di restituire il risultato dell'operazione
def toNumber_faces(model):
    hpc = SKEL_1(STRUCT(MKPOLS(model)))
    hpc = cellNumbering (model,hpc)(range(len(model[1])),CYAN,1)
    VIEW(hpc)

#metodo che mi permette di inserire il diagramma in diverse celle del master
def toReplicate_into_masters2cell(obg,model,lista):
    lista.sort();
    lista.reverse();
    for k in lista:
        model = diagram2cell(obg,model,k)
    toNumber_faces(model)
    return model

def toRemoveCells(model,lista):
    V,CV = model
    model =  V,[cell for k,cell in enumerate(CV) if not (k in lista)]
    toNumber_faces(model)
    return model
    
#funzione di appoggio che fonde 2 celle seguendo il principio del ciclo eureliano
def merge_mkpol(l1,l2):
    fus = []
    j = 0
    stop = False
    while(j<len(l1) and not(stop)):
        fus = fus + [l1[j]]
        if (l1[j] in l2):
            stop = True
            ind = l2.index(l1[j])
            j = j+1
            i = ind+1
            while (i<len(l2)):
                fus = fus+[l2[i]]
                i = i+1
            i=0
            while (i<ind):
                fus = fus+[l2[i]]
                i = i+1
            while (j<len(l1)):
                if (not(l1[j] in fus)):
                    fus = fus+[l1[j]]
                j = j+1
        j=j+1
    return fus



#questa funzione mi unisce le celle di un diagramma, utile se voglio inserire un diagramma x dentro a una serie di celle di un diagramma y
def union_cell(model,lista_cells):
    V,CV = model
    CVn = []
    lista_cells.sort()
    app =   CV[lista_cells[0]]
    stop = False
    for k,cell in enumerate(CV):
        if (k in lista_cells):
            app = merge_mkpol(app,cell)
            lista_cells.remove(k)
        elif(len(lista_cells)==0 and not(stop)):
            CVn = CVn + [app]
            CVn = CVn + [cell]
            stop = True
        else:
            CVn = CVn + [cell]
    return V,CVn
    
    


""" * * * TEST * * * """

#inseriamo il master
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
toNumber_faces(master)

#rimuoviamo le celle
master = toRemoveCells(master,[13,33,17,37])


#inseriamo il diagramma per la porta
diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])

#adesso inseriamo il diagram su diverse celle del master
master = toReplicate_into_masters2cell(diagram,master,[29,32,14])

#ora buchiamo le porte
master = toRemoveCells(master,[51,45,57])

#uniamo le celle
master = union_cell(master,[16,26,32])
toNumber_faces(master)


#inseriamo il 3-array del diagram dentro alle celle unite
master = toRemoveCells(toReplicate_into_masters2cell(diagram,master,[30]),[57])

#VIEW(STRUCT(MKPOLS(master)))
    
