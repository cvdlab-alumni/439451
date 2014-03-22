'''
Created on 22/mar/2014

@author: Davide
'''

from pyplasm import *

from exercise1 import *

"""porte in alto da nord a sud"""
nord = COLOR (PURPLE) (INSR (PROD) ([QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),QUOTE([-0.45,0,-3.5,0,-0.45]),Q(1.11)]))

"""porte in alto da ovest a est"""
ovest =  COLOR (PURPLE) (INSR (PROD) ([QUOTE([-0.45,0,-3.5,0,-0.45]),QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),Q(1.11)]))

"""pareti delle colonne di base"""
est = COLOR (BROWN) (INSR (PROD) ([QUOTE([-0.4,0,-3.6,0,-0.4]),QUOTE([-0.4,0.2,-3.2,0.2,-0.4]),Q(5.51)]))



"""definisco delle striscie che ricoprono la ringhiera"""
points = [[0.25,0.25],[4.15,0.25],[0.25,4.15],[4.15,4.15]]
square = MKPOL([points,[[1,2],[1,3],[3,4],[2,4]],None])
set1 = PROD([square,Q(0.0225)])
set2 = T(3)(0.045)(set1)
set3 = T(3)(0.045)(set2)
set4 = T(3)(0.045)(set3)
set5 = T(3)(0.045)(set4)
set6 = T(3)(0.045)(set5)
set7 = T(3)(0.045)(set6)
set8 = T(3)(0.045)(set7)
set_complete = STRUCT([set1,set2,set3,set4,set5,set6,set7,set8])
sud = COLOR (BLUE) (set_complete)


""" come richiesto, ho messo almeno 4 facciate verticali (anche di piu) """

mock_up_3D = STRUCT([two_and_half_model,T(3)(4.4)(nord),T(3)(4.4)(ovest),est,T(3)(4.4225)(sud)])
#VIEW(mock_up_3D)




