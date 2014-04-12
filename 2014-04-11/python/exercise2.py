from exercise1 import *


"""RESTO DEI COMPONENTI VERTICALI (sono veramente pochi)"""

"""definisco delle striscie che ricoprono la ringhiera"""
points = [[0.25,0.25],[4.15,0.25],[0.25,4.15],[4.15,4.15]]
square = MKPOL([points,[[1,2],[1,3],[3,4],[2,4]],None])
striscia = PROD([square,Q(0.0225)])
set_complete = T(3)(4.4225) (STRUCT(NN(8)([striscia,T(3)(0.045)])))

"""definisco le porte scorrevoli"""
doorsNordSud =  (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45]),Q(1.11)])))
doorsEstOvest = (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.45,-3.5,0,-0.45]),QUOTE([-0.6,1.5,-0.2,1.5,-0.6]),Q(1.11)])))
doorEst = (T([1,2,3])([0.45,2.3,4.4]) (CUBOID([0,1.5,1.11])))

"""una porta e semi-aperta"""
half_open_door =  (T([1,2,3])([0.45,1.8,4.4]) (CUBOID([0,0.3,1.11])))
doors_complete = COLOR([0.43921,0.25882,0.0784])(STRUCT([doorsNordSud,doorsEstOvest,doorEst,half_open_door]))
#doorsEstOvest = DIFFERENCE(STRUCT([doorsEstOvest,half_open_door]))

"""altro componente per il sopra tetto"""
band = T([1,2,3])([0.91,1.2,7.34])(CUBOID([2.6,2,0.02]))
band_complete =  COLOR ([0.72156,0.52549,0.0431]) (STRUCT(NN(10)([band,T(3)(0.08)])))




"""NOTA IMPORTANTISSIMA: questa variabile 'mock_up_3D_vertical_planes' comprende le strutture verticali (pareti, fasce, muri ecc..), in tal caso e
                        questa la variabile di riferimento per la quale si riferisce al secondo esercizio"""
mock_up_3D_vertical_planes = STRUCT([set_complete,doors_complete,band_complete])


"""UNIONE DELLE 2 COMPONENTI (PARTIZIONI ORIZZONTALI E VERTICALI)"""
mock_up_3D_complete = STRUCT([mock_up_3D_horizontal_planes,mock_up_3D_vertical_planes])


#VIEW(mock_up_3D_complete)