'''
Created on 22/mar/2014

@author: Davide
'''

from pyplasm import *
from math import *
from exercise3 import *

"""funzioni utili"""

def listascale(n):
    q = n*0.2
    dist = n*0.2
    return T(1)(dist)(CUBOID([0.2,0.5,q]))

def trasla1(ar):
    return [x+1 for x in ar]

"""definisco i scalini"""
scale = map (listascale,trasla1(range(5)))

"""definisco anche una scaletta esterna"""
pedins = INSR (PROD) ([QUOTE([-0.29,0.1,-0.01]*6),QUOTE([0.2]*3),Q(0.1)])
cilindro1 = R([1,3])(-PI/2) (CYLINDER([0.1,3])(20))
cilindro2 = T(2)(0.6)(cilindro1)
cilindri = STRUCT([cilindro1,cilindro2])
cilindri_t = T(1)(-0.018)(cilindri)
scaletta = STRUCT([pedins,cilindri_t])
scaletta_r = R([1,3])(PI/2.6)(scaletta)


"""i scalini INTERNI sono all'interno dell'edificio, si visualizzano utilizzando il mouse"""
scaleTranslate = T([1,2,3])([1.2,1.2,4.4])(STRUCT(scale))
scaletta_r_translate= COLOR (RED) (T([1,2])([1.2,1.2])(scaletta_r))

solid_model_3D_with_scale_internal_external = STRUCT([solid_model_3D,scaleTranslate,scaletta_r_translate])

#VIEW(solid_model_3D_with_scale_internal_external)




