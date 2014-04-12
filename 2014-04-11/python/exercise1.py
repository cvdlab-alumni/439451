

from pyplasm import *


"""alcune componenti utili che serviranno per portarle facilmente in 3D"""
roof = T(3)(5.51) (PROD([QUOTE([4.4]),QUOTE([4.4])]))
roofTop = T(3)(7.31) (PROD ([QUOTE([-1.2,2]),QUOTE([-1.2,2])]))
bandsOvestEst = PROD ([QUOTE([-0.2,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05]),QUOTE([-0.2,0.05,-3.9,0.05,-0.2])])
bandsNordSud = PROD ([QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),QUOTE([-0.2,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05,-0.74,0.05])])




"""STRUTTURE ORIZZONTALI"""

holderColumnsBottom1_3D = COLOR ([0.6980,0.6980,0.6980]) (T(3)(2) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.3,3.8,-0.3]),Q(0.18)])))
holderColumnsTop1_3D = COLOR ([0.6980,0.6980,0.6980]) (T(3)(4) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.1,4.2,-0.1]),Q(0.3)])))
holderColumnsBottom2_3D = COLOR ([0.6980,0.6980,0.6980]) (T(3)(1) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45]),Q(0.18)])))
holderColumnsMedium2_3D = COLOR ([0.6980,0.6980,0.6980]) (T(3)(3) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45]),Q(0.18)])))
holderColumnsTop2_3D = COLOR (BROWN) (T(3)(4.2) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.18,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.18]),Q(0.16)])))
overRailing1_3D = COLOR (WHITE) (T(3)(4.76) (INSR (PROD) ([QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),QUOTE([-0.15,4.1,-0.15]),Q(0.1)])))
overRailing2_3D = COLOR (WHITE) (T(3)(4.76) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),Q(0.1)])))
floor1_3D = COLOR ([0.9686,0.9098,0.6235]) (T(3)(4.36) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.15,4.1,-0.15]),Q(0.08)])))
ceilingHangerMiddle_3D = COLOR ([0.6980,0.6980,0.6980]) (T(3)(4.4) (INSR (PROD) ([QUOTE([-0.4,0.2,-3.2,0.2,-0.4]),QUOTE([-2.1,0.2,]),Q(1.11)])))
colommuns_3D =  COLOR ([0.37254,0.37254,0.37254]) ((INSR (PROD) ([QUOTE([-0.4,0.2,-1.5,0.2,-1.5,0.2]),QUOTE([-0.4,0.2,-3.2,0.2,-0.4]),Q(5.51)])))
roof_full = COLOR(BLACK) (JOIN([roof,roofTop]))
bandsOvestEst_3D = COLOR (BROWN) (T(3)(4.4)(PROD([bandsOvestEst,Q(0.36)])))
bandsNordSud_3D = COLOR (BROWN) (T(3)(4.4)(PROD([bandsNordSud,Q(0.36)])))

"""definisco il sopra tetto"""
cilindro = R([1,3])(-PI/2) (CYLINDER([0.08,3])(20))
cilynder_t = COLOR ([0.85490,0.6470,0.12549]) (T([1,2,3])([0.65,2.2,8.72])(cilindro))
baseOverRoof = T([1,2,3])([0.95,0.95,7.31])(CUBOID([2.5,2.5]))
linea = T([1,2,3])([0.95,2.2,8.75])(CUBOID([2.5]))
OverRoofComplete_3D = COLOR ([0.85490,0.6470,0.12549])(JOIN(STRUCT([baseOverRoof,linea])))




"""aggiunta di qualche elemento rispetto al primo homework"""
#trave da soffitto
beamceiling_3D_sud = T([1,2,3])([0.4,0.35,5.41])(CUBOID([3.6,0.3,0.1]))
beamceiling_3D_nord = T(2)(3.4)(beamceiling_3D_sud)
beamceiling_3D_ovest = T([1,2,3])([0.35,0.4,5.41])(CUBOID([0.3,3.6,0.1])) 
beamceiling_3D_est = T(1)(3.4)(beamceiling_3D_ovest)             

beamceiling_3D_complete = COLOR ([0.25098,0.25098,0.25098]) (STRUCT([beamceiling_3D_sud,beamceiling_3D_nord,beamceiling_3D_ovest,beamceiling_3D_est]))


mock_up_3D_horizontal_planes = STRUCT([holderColumnsBottom1_3D,holderColumnsTop1_3D,holderColumnsBottom2_3D,holderColumnsMedium2_3D,holderColumnsTop2_3D,floor1_3D,
                                       overRailing1_3D,overRailing2_3D,colommuns_3D,ceilingHangerMiddle_3D,beamceiling_3D_complete,roof_full,bandsOvestEst_3D,bandsNordSud_3D,
                                       cilynder_t,OverRoofComplete_3D])

                  

#VIEW(mock_up_3D_horizontal_planes)