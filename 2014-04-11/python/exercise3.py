from exercise2 import *
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, 'C:/Users/Davide/lar-cc/lib/py/')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from math import *
from morph import *
from mapper import *
from boolean1 import *
from boolean2 import *
from collections import *


"""definiamo un cortile di base su dove e situata la palafitta e altri edifici"""

modelCortile = larRod([11,0.6])([4,1])
modelCortile = COLOR([0.95686,0.6431,0.37647])(R([1,2])(PI/4)(STRUCT(MKPOLS(modelCortile))))

"""l'esterno del cortile"""
modelExternalCortile_sup =  larRod([14,0.6])([4,1])
modelExternalCortile_inf =  larRod([13,0.6])([4,1])
modelExternalCortile = DIFFERENCE([R([1,2])(PI/4)(STRUCT(MKPOLS(modelExternalCortile_sup))),R([1,2])(PI/4)(STRUCT(MKPOLS(modelExternalCortile_inf)))])


"""definisco il recinto"""
V=[[0.0,0.0,0.0],[1,0.0,0.0],[0.0,0.1,0.0],[1,0.1,0.0],[0.0,0.0,2.0],[1,0.0,2.0],[0.0,0.1,2.0],[1,0.1,2.0],[0.5,0.0,2.5],[0.5,0.1,2.5]]
FV = [range(len(V))]
fence_element = T([1,2,3])([1.5,9.65,0.6])(STRUCT(MKPOLS((V,FV))))


fence_complete_ovest1 = STRUCT(NN(8)([fence_element,T(1)(1)]))
fence_complete_ovest2 =  T(1)(-11)(fence_complete_ovest1)
fence_complete_ovest = T(2)(-0.1)(STRUCT([fence_complete_ovest1,fence_complete_ovest2]))

fence_element_nord = R([1,2])(PI/2)(fence_element)
fence_element_nord = T([1,2])([19.25,7])(fence_element_nord)
fence_complete_nord = STRUCT(NN(19)([fence_element_nord,T(2)(-1)]))
fence_complete_sud = T(1)(-19.1)(fence_complete_nord)
fence_complete_est = R([1,2])(PI/2)(fence_complete_nord)
fence_complete_est = T(2)(-19.1)(fence_complete_est)

fence_complete = COLOR([0.50196,0.50196,0.50196])(STRUCT([fence_complete_ovest,fence_complete_nord,fence_complete_sud,fence_complete_est]))

"""ora definisco un ponticello"""
base = COLOR([0.5882,0.29411,0]) (T([1,2,3])([-1.5,7.7,0.4])(COLOR (BROWN) (CUBOID([3,1.5,0.2]))))
band_est = T([1,2,3])([-1.5,7.7,1.4])(CUBOID([0.2,1.5,0.2]))
band_ovest = T(1)(2.8)(band_est)
band_vertical_element = CUBOID([0.1,0.1,1])
band_vertical_est = T([1,2,3])([-1.4,9,0.4])(STRUCT(NN(4)([band_vertical_element,T(2)(-0.4)])))
band_vertical_ovest = T(1)(2.8)(band_vertical_est)

"""definiamo l'entrata"""
band_pincipal_est = T([1,2,3])([-1.5,9.2,0.6])(CUBOID([0.2,0.65,3])) 
band_pincipal_ovest = T(1)(2.8)(band_pincipal_est)
band_principal_sup = T([1,2,3])([-1.7,9.4,2.5])(CUBOID([3.5,0.1,1]))

bridge = COLOR([0.5882,0.29411,0])(STRUCT([base,band_est,band_ovest,band_vertical_est,band_vertical_ovest]))
band_principal =  COLOR([0.50196,0.50196,0.50196]) (STRUCT([band_pincipal_est,band_pincipal_ovest,band_principal_sup]))

"""definiamo un piccolo fiume, con acqua moolto bassa"""
modelFiume = larRod([13,0.3])([4,1])
modelFiume = COLOR([0.27450,0.5098,0.70588])(R([1,2])(PI/4)(STRUCT(MKPOLS(modelFiume))))



"""inseriamo un'altra palafitta, come edificio extra (abbastanza semplificato)"""
#colonne
base_cilynder_element = STRUCT(MKPOLS(larRod([1,11])([64,1])))
base_cilynder_est = STRUCT(NN(4)([base_cilynder_element,T(1)(4)]))
base_cilynder_ovest = T(2)(6)(base_cilynder_est)
base_cilynder_complete = COLOR([0.5686,0.50588,0.31764])(STRUCT([base_cilynder_est,base_cilynder_ovest]))
base_cilynder_complete = T([1,2])([2.5,2.5])(base_cilynder_complete)

#tetto
t2 = POLYLINE([[0,0],[13,0],[12.5,4],[0.5,4],[0,0]])
t1 = POLYLINE([[0.5,0.5],[12.5,0.5],[12.25,3.5],[0.75,3.5],[0.5,0.5]])
tpr = SOLIDIFY(STRUCT([t2,t1]))
roof = PROD([tpr,Q(18)])
roof = R([2,3])(PI/2)(roof)
roof = R([1,2])(PI/2)(roof)
roof = COLOR([0.39607,0.26274,0.1294])(T([2,3])([-1,7])(roof))

#piano
floor =  COLOR([0.39607,0.26274,0.1294]) (T([1,2,3])([1.5,1.5,3])(CUBOID([14.1,8,0.6])))

#sbarre
bars_ovest = T([1,2,3])([1.5,1.5,3.6])(CUBOID([0.1,8,1]))
bars_est = T(1)(14)(bars_ovest)
bars_sud = T([1,2,3])([1.5,1.4,3.6])(CUBOID([14.1,0.1,1]))
bars_nord_1 = T([1,2,3])([1.5,9.5,3.6])(CUBOID([5.55,0.1,1])) 
bars_nord_2 = T(1)(8.55)(bars_nord_1)
bars = COLOR(BLACK)(STRUCT([bars_ovest,bars_est,bars_sud,bars_nord_1,bars_nord_2]))

other_mockup_3D = T([1,2,3])([-20,-20,0.6])(STRUCT([base_cilynder_complete,roof,floor,bars]))
other_mockup_3D = S([1,2,3])([0.3,0.3,0.3])(other_mockup_3D)
other_mockup_3D = R([1,2])(-PI/2)(other_mockup_3D)


"""inseriamo ancora un'altra palafitta, come edificio extra (abbastanza semplificato)"""
#colonne
colommuns_sud = T([1,2])([1.5,1.5])(STRUCT(NN(4)([CUBOID([0.1,0.1,5]),T(1)(1.1)])))
colommuns_nord = T(2)(3)(colommuns_sud)

#pareti
walls_ovest = T([1,2,3])([1.5,1.5,2.4])(STRUCT(NN(3)([CUBOID([0.1,3,0.8]),T(3)(0.9)])))
walls_est = T(1)(3.3)(walls_ovest)

walls_sud = T([1,2,3])([1.5,1.5,2.4])(STRUCT(NN(3)([CUBOID([3.4,0.1,0.8]),T(3)(0.9)])))
walls_nord = T(2)(3)(walls_sud)

walls = STRUCT([walls_ovest,walls_est,walls_sud,walls_nord])

#pavimenti
floor_inf = T([1,2,3])([1.5,1.5,2.4])(DIFFERENCE([CUBOID([3.4,3,0.4]),T([1,2])([1.3,1.3])(CUBOID([1,1,0.4]))]))

#tetto
base_floor_over = T([1,2,3])([1.5,1.5,5])(CUBOID([3.4,3.1,0.1]))
linea = T([1,2,3])([1.5,3,7])(CUBOID([3.4]))
roof_over = JOIN(STRUCT([base_floor_over,linea]))

other_mockup_3D_2 = COLOR([0.6,0.2,0])(STRUCT([colommuns_nord,colommuns_sud,walls,floor_inf,roof_over]))
other_mockup_3D_2 = T(2)(-8)(other_mockup_3D_2 )




"""inserisco delle scalette, una per ogni palafitta"""
#scala1
comp_1 = STRUCT(MKPOLS(larRod([0.1,4.5])([64,1])))
comp_2 = T(1)(1.1)(comp_1)
scalini = T([1,2,3])([0.08,-0.05,0.5])(STRUCT(NN(7)([CUBOID([0.95,0.1,0.1]),T(3)(0.6)])))
scale = T(3)(0.6)(STRUCT([comp_1,comp_2,scalini]))


scale1_for_one =  R([1,2])(PI/2)(scale)
scale1_for_one = T([1,2])([-1,0.7])(scale1_for_one)
scale1_for_one = R([1,3])(-PI/15)(scale1_for_one)

scale2_for_two = R([1,2])(PI/2)(scale)
scale2_for_two = T([1,2,3])([-2.01,5.2,1])(scale2_for_two)
scale2_for_two = S([2,3])([0.6,0.5])(scale2_for_two)
scale2_for_two = R([1,3])(PI/7)(scale2_for_two)

scale3_for_three = T([1,2,3])([5,-4.65,-1])(scale) 
scale3_for_three = S([1,3])([0.6,0.6])(scale3_for_three)
scale3_for_three = R([2,3])(-PI/22)(scale3_for_three)


scales = COLOR([0.7215,0.7419,0.2])(STRUCT([scale1_for_one,scale2_for_two,scale3_for_three]))



"""ora inseriamo un tavolo ed una sedia da inserire all'interno del mio edificio"""
#table
pilastro_x = QUOTE([0.05,-1,0.05,-1])
pilastro_y = QUOTE([0.05,-0.6,0.05,-0.6])
pilastri = (INSR (PROD)([pilastro_x,pilastro_y,Q(0.5)]))
stby = QUOTE([-0.005,0.025,-0.02,-0.6,-0.02,0.025,-0.005])
stbx = QUOTE([-0.05,1,-0.05])
sttb = INSR(PROD)([stbx,stby,Q(0.065)])
sttbT = T(3)(0.435)(sttb)
stlsx = QUOTE([-0.005,0.025,-0.02,-1,-0.02,0.025,-0.005])
stlsy = QUOTE([-0.05,0.6,-0.05])
stls = INSR(PROD)([stlsx,stlsy,Q(0.065)])
stlsT = T(3)(0.435)(stls)
portaCassetto = T([1,2,3])([0.45,0.005,0.435])(CUBOID([0.2,0.1,0.065]))
cassetto = T([1,2,3])([0.4,0,0.435])(CUBOID([0.3,0.005,0.065]))
tavola = T([1,2,3])([-0.0175,-0.0175,0.5])(CUBOID([1.135,0.735,0.02]))
table = COLOR([0.39607,0.26274,0.1294])(STRUCT([pilastri,sttbT,stlsT,portaCassetto,cassetto,tavola]))
 
table = T([1,2,3])([2,2,5.05])(table) 
 

#chair
pilastro_x = QUOTE([-0.35,0.05]*2)
pilastro_y = QUOTE([-0.35,0.05]*2)
four_pilastri = INSR(PROD)([pilastro_x,pilastro_y,Q(0.4)])
piano = T([1,2,3])([0.3,0.325,0.4])(CUBOID([0.5,0.5,0.03]))
albero = T([1,2,3])([0.545,0.39,0.1])(CUBOID([0.06,0.37,0.07]))
stx = QUOTE([-0.4,0.35])
sty = QUOTE([-0.36,0.03,-0.01]*2)
stt = INSR(PROD)([stx,sty,Q(0.07)])
sttT = T(3)(0.1)(stt)
btx = QUOTE([-0.75,0.05])
bty = QUOTE([-0.35,0.05]*2)
btt = INSR (PROD)([btx,bty,Q(0.5)])
bttT = T(3)(0.4)(btt)
sdr1 = T([1,2,3])([0.76,0.4,0.45])(CUBOID([0.03,0.35,0.15]))
sdr2 = T(3)(0.25)(sdr1)
sdra = STRUCT([sdr1,sdr2])
artIn = STRUCT([sttT,albero])
sopr = STRUCT([albero,four_pilastri])

chair =  COLOR([0.39607,0.26274,0.1294])(STRUCT([sdra,artIn,sopr,piano,bttT]))
chair = T([1,2,3])([2,1,5.05])(chair) 


""""""


 
mock_up_3D_complete = T(3)(0.6)(mock_up_3D_complete)

small_area_plan = STRUCT([modelCortile,modelExternalCortile,fence_complete,bridge,band_principal,modelFiume,mock_up_3D_complete,
                          other_mockup_3D,other_mockup_3D_2,scales,table,chair]) 


#VIEW(small_area_plan)

