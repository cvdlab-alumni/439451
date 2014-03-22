'''
Created on 22/mar/2014

@author: Davide
'''

from pyplasm import *
from math import *

from exercise2 import *



""" per motivi tecnici, preferisco ridefinire i modelli, mandandoli direttamente in 3D rispettando i valori definiti negli esercizi
    precedenti, ma soprattutto anche per ridefinire i colori: quindi anche per questioni di comosdita"""
#holderColumnsBottom1x = T(3)(2) (PROD ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.3,3.8,-0.3])]))

"""I COLORI NON SONO UN GRANCHe... HO AVUTO PROBLEMI NELL APPLICARE L'RGB: HO DIVISO PER 255, MAAA.... STRANAMENTE NON MI USCIVANO I COLORI
   DESIDERATI, NON SO PERCHe. """

"""fasce verticali disposte orizzontalmente sulla ringhiera"""
set_complete_trasla = COLOR (WHITE) (T(3)(4.4225)(set_complete))


roof = T(3)(5.51) (PROD([QUOTE([4.4]),QUOTE([4.4])]))
roofTop = T(3)(7.31) (PROD ([QUOTE([-1.2,2]),QUOTE([-1.2,2])]))
"""colonne"""
bases =  (PROD([QUOTE([-0.4,0.2,-1.5,0.2,-1.5,0.2]),QUOTE([-0.4,0.2,-3.2,0.2,-0.4])]))

"""porte del balcone"""
doorsNordSud = COLOR (YELLOW) (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),QUOTE([-0.45,0,-3.5,0,-0.45]),Q(1.11)])))
doorsEstOvest = COLOR (YELLOW) (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.45,0,-3.5,0,-0.45]),QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),Q(1.11)])))

"""fasce verticali per la ringhiera"""
barsNordSud = COLOR(BROWN) (T(3)(4.4)(INSR (PROD) ([QUOTE([-0.25,0.74,-0.05,0.74,-0.05,0.74,-0.05,0.74,-0.05,0.74,-0.25]),QUOTE([-0.22,0,-3.96,0,-0.22]),Q(0.36)])))
barsEstOvest = COLOR (BROWN) (T(3)(4.4)(INSR (PROD) ([QUOTE([-0.22,0,-3.96,0,-0.22]),QUOTE([-0.25,0.74,-0.05,0.74,-0.05,0.74,-0.05,0.74,-0.05,0.74,-0.25]),Q(0.36)])))


bandsOvestEst = PROD ([QUOTE([-0.2,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05]),QUOTE([-0.2,0.05,-3.9,0.05,-0.2])])
bandsNordSud = PROD ([QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),QUOTE([-0.2,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05])])


ceilingHangerMiddle = COLOR (BROWN) (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.4,0.2,-3.2,0.2,-0.4]),QUOTE([-2.1,0.2,]),Q(1.11)])))


"""elementi che servono per ricavare  il sopratetto """
cilindro = R([1,3])(-PI/2) (CYLINDER([0.08,2.4])(20))
cilynder_t = T([1,2,3])([1,2.2,8.72])(cilindro)
pointsOverRoof = [[1,1],[3.4,1],[1,3.4],[3.4,3.4]]
baseOverRoof = T(3)(7.31)(JOIN(AA(MK)(pointsOverRoof)))







""" resto degli elementi in 3D"""
holderColumnsBottom1_3D = COLOR (WHITE) (T(3)(2) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.3,3.8,-0.3]),Q(0.18)])))
holderColumnsTop1_3D = COLOR (WHITE) (T(3)(4) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.1,4.2,-0.1]),Q(0.3)])))
overRailing1_3D = COLOR (WHITE) (T(3)(4.76) (INSR (PROD) ([QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),QUOTE([-0.15,4.1,-0.15]),Q(0.1)])))
overRailing2_3D = COLOR (WHITE) (T(3)(4.76) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),Q(0.1)])))
holderColumnsBottom2_3D = COLOR (WHITE) (T(3)(1) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45]),Q(0.18)])))
holderColumnsMedium2_3D = COLOR (WHITE) (T(3)(3) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45]),Q(0.18)])))
holderColumnsTop2_3D = COLOR (BROWN) (T(3)(4.2) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.18,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.18]),Q(0.16)])))
floor1_3D = COLOR (WHITE) (T(3)(4.36) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.15,4.1,-0.15]),Q(0.08)])))
bases3D = COLOR (BROWN) (PROD ([bases,Q(5.51)]))
bandsOvestEst_3D = COLOR (BROWN) (T(3)(4.4)(PROD([bandsOvestEst,Q(0.36)])))
bandsNordSud_3D = COLOR (BROWN) (T(3)(4.4)(PROD([bandsNordSud,Q(0.36)])))
roof_full = COLOR(BLACK) (JOIN([roof,roofTop]))
overRoof = COLOR (BROWN) (JOIN([baseOverRoof,cilynder_t]))




""" risistemiamo tutto con 2 variabili fino a quella finale"""
two_and_half_model_3D = STRUCT([holderColumnsBottom1_3D,holderColumnsTop1_3D,holderColumnsBottom2_3D,holderColumnsMedium2_3D,holderColumnsTop2_3D,
                                floor1_3D,overRailing1_3D,overRailing2_3D, roof_full,overRoof])
mock_up_3D = STRUCT([bases3D,bandsOvestEst_3D,bandsNordSud_3D,set_complete_trasla,doorsNordSud,doorsEstOvest,ceilingHangerMiddle])
solid_model_3D = STRUCT([two_and_half_model_3D,mock_up_3D])

#VIEW(solid_model_3D)

