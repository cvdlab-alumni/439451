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





"""creo una funzione che applica il ciclo fusione-enumerazione-fusione"""

"""QUESTO ESERCIZIO E DIVISO IN 4 PARTI: UNA PARTE  COMPRENDe FUNZIONI CHE SEMPLIFICANO TANTE OPERAZIONI ELEMENTARI (RIMUOVI, FONDI, ENUMERA CELLE ECC..) 
   IN POCHE ISTRUZIONI; UN ALTRA PARTE COMPRENDE FUNZIONI CHE  AUTOMATIZZA OPERAZIONI ELEMENTARI COME MERGE ED ELIMINATE SENZA DOVER RIGUARDARE LE
   CELLE NUMERATE; UN ALTRA PARTE COMPRENDE FUNZIONI CHE CONSENTONO DI UNIRE CELLE DI UN DIAGRAMMA; L ULTIMA PARTE INVECE E DEDICATA AI TEST:
   CE NE SONO DUE: IL PRIMO USA FUNZIONI ELEMENTARI SEMPLIFICATI CON LA NECESSITA PERO DI GUARDARE LE CELLE NUMERATE; IL SECONDO USA UNA FUNZIONE
   (POSSIAMO DIRE, QUELLA PIU  RICHIESTA IN QUESTO ESERCIZIO) CHE ELIMINA E FONDE DIRETTAMENTE SENZA DOVER RIGUARDARE LE CELLE NUMERATE  """


#funzione di appoggio che mi consente di restituire il diagramma-modello con le celle numerate
def toNumber_faces(model):
    hpc = SKEL_1(STRUCT(MKPOLS(model)))
    hpc = cellNumbering (model,hpc)(range(len(model[1])),CYAN,1)
    VIEW(hpc)
    
    
    

"""metodo PRONCIPALE che mi permette di INSERIRE IL SUB-DIAGRAMMA IN DIVERSE CELLE DEL MASTER, obg=SUB-DIAGRAM  model=MASTER  
    lista=LISTA CELLE DEL MASTER SULLE QUALI VOGLIO INSERIRE IL SUBDIAGRAM, includendo anche la visione dell'output numerato"""
def toReplicate_into_masters2cell(obg,model,lista):
    lista.sort();
    lista.reverse();
    for k in lista:
        model = diagram2cell(obg,model,k)
    toNumber_faces(model)
    return model


#funzione che mi rimuove determinate celle di una diagramma, includendo anche la visione dell'output numerato
def toRemoveCells(model,lista):
    V,CV = model
    model =  V,[cell for k,cell in enumerate(CV) if not (k in lista)]
    toNumber_faces(model)
    return model




"""ALTRA FUNZIONE PRINCIPALE: CREO UNA FUNZIONE PIU COMPLESSA CHE CONTEMPORANEAMENTE FA IL REMOVE E IL MERGE CALCOLANDOSI IL CAMBIAMENTO DELL ENUMERAZIONI 
   DELLE CELLE SENZA A STARE A RIGUARDARLI OGNI VOLTA """
   

#funzione di appoggio che mi decrementa el di una quantita pari al numero degli elementi della lista per i quali el is maggiore 
def decr_qt(el,lista):
    cont = 0
    for k in lista:
        if k<el:
            cont+=1
    return el-cont

#funzione di appoggio che usa la funzione di sopra (decr_qt) per applicarla a tutti gli elementi della lista del primo parametro in base all altra
#lista passata come secondo parametro
def decr_qt_all(lista,ll):
    return [decr_qt(k,ll) for k in lista]


#FUNZIONE PRINCIPALE CHE AUTOMATIZZA TUTTO
def cycle_merge_eliminate(diagram,master,toRemove,toMerge):
    toMerge = decr_qt_all(toMerge,toRemove)
    V,CV = master
    master =  V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
    toMerge.sort()
    toMerge.reverse()
    for k in toMerge:
        master = diagram2cell(diagram,master,k)
    toNumber_faces(master)
    return master
    


    
"""funzione di appoggio che fonde 2 celle seguendo il principio del ciclo eureliano"""
#so che non is esteticamente bello questo frammento di codice, ma non ho saputo semplificarlo usando i trucchi di python (ad esempio mi is stato difficile usare il list.filter) 
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



"""questa funzione mi unisce le celle di un diagramma y, utile se voglio inserire un diagramma x dentro a una serie di celle di un diagramma y"""
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
toNumber_faces(diagram)

#adesso inseriamo il diagram su diverse celle del master
master = toReplicate_into_masters2cell(diagram,master,[29,32,14])

#ora buchiamo le porte
master = toRemoveCells(master,[51,45,57])

#uniamo le celle
master = union_cell(master,[16,26,32])
toNumber_faces(master)


#inseriamo il 3-array del diagram dentro alle celle unite
master = toRemoveCells(toReplicate_into_masters2cell(diagram,master,[30]),[57])

VIEW(STRUCT(MKPOLS(master)))


""" * * * TEST2 * * * """
"""Rifacciamo le stesse operazioni usando pero l altra funzione principale complessa che automatizza il ciclo (cycle_merge_eliminate)"""

#ridefinisco il solito master
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
toNumber_faces(master)

#diagramma porta
diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram = toRemoveCells(diagram,[2])

#ora applichiamo la funzione PRINCIPALE cycle_merge_eliminate in modo che con una funzione elimino e inserisco direttamente le porte
#senza a stare a riguardare nuovamente i  numeri
toRemove=[13,17,33,37]
toMerge=[31,35,15]
master = cycle_merge_eliminate(diagram,master,toRemove,toMerge)

VIEW(STRUCT(MKPOLS(master)))

    
