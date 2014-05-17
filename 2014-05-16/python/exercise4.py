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



def toNumber_faces(diagram):
    V,CV = diagram
    hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
    hpc = cellNumbering (diagram,hpc)(range(len(CV)),CYAN,2)
    return VIEW(hpc)



"""cerchiamo di ridefinire le operazioni"""

#metodo che date 2 liste, fa l'unione evitando gli elementi in comune
def union_list(a1,a2):
    comp = []
    for k in a1:
        comp = comp + [k]
    for h in a2:
        if (not(h in comp)):
            comp = comp+[h]
    return comp

# funzione di appoggio che date 2 liste l2 ed l1, da l2 elimino gli elementi in comune con l1
def remove_common(l2,l1):
    return [k for k in l2 if not(k in l1)]

# funzioen che rimuove le repliche in una lista
def remove_double(lst):
    app = []
    for k in lst:
        if (not(k in app)):
            app = app +[k]
    return app

#funzione che mi restituisce la lista degli elementi che occorro + di una volta nella lista
def get_double_elements(lst):
    app=[]
    de = []
    for k in lst:
        if (not(k in app)):
            app = app +[k]
        elif(not(k in de)):
            de = de+[k]
    return de

#funzione che mi restituisce gli indici dell'elemento presente + volte nella lista
def get_indexes(el,lst):
    ind = []
    comp = lst
    i=0
    while(el in comp):
        ind = ind+[comp.index(el)+i]
        comp.remove(el)
        i=  i+1
    return ind

#funzione che sostituisce tutti gli elementi in el se questi sono presenti nella lista passata come secondo parametro
def replace(el,app,lst):
    res = []
    for cell in lst:
        reso=[]
        for k in cell:
            if (k in app):
                reso = reso+[el]
            else:
                reso = reso+[k]
        res = res+[reso]
    return res


   

def replace_toAll(V,CV):
    dop =  get_double_elements(V)
    for ver in dop:
        indexes = get_indexes(ver,V)
        CV = replace(indexes[0],indexes,CV)
    return CV




def diagram2cellMatrix(diagram):
   def diagramToCellMatrix0(master,cell):
      wdw = min(diagram[0]) + max(diagram[0])         # window3D
      cV = [master[0][v] for v in master[1][cell]] #mi da tutti i vertici coinvolti nelle celle
      vpt = min(cV) + max(cV)                      # viewport3D
      mat = zeros((4,4))
      mat[0,0] = (vpt[3]-vpt[0])/(wdw[3]-wdw[0])
      mat[0,3] = vpt[0] - mat[0,0]*wdw[0]
      mat[1,1] = (vpt[4]-vpt[1])/(wdw[4]-wdw[1])
      mat[1,3] = vpt[1] - mat[1,1]*wdw[1]
      mat[2,2] = (vpt[5]-vpt[2])/(wdw[5]-wdw[2])
      mat[2,3] = vpt[2] - mat[2,2]*wdw[2]
      mat[3,3] = 1
      return mat
   return diagramToCellMatrix0

"""funzione da ridefinire"""
def diagram2cell_2(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   #V = master[0] + diagram[0]  vengono causate le repliche dei vertici
   #V = union_list(master[0],diagram[0])
   V = master[0] + diagram[0] 
   offset = len(master[0])
   CV = [c for k,c in enumerate(master[1]) if k != cell] + [
         [v+offset for v in c] for c in diagram[1]]
   #CV = replace_toAll(V,CV)
   #V = remove_double(V)
   master = V, CV
   return master


master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
Vm,CVm = master
toNumber_faces(master)

diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
Vd,CVd = diagram
diagram = Vd,[cell for k,cell in enumerate(CVd) if not (k in [2])]
toNumber_faces(diagram)


"""Test"""
master = diagram2cell_2(diagram,master,31)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)
#toNumber_faces(master)

