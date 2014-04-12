

from exercise3 import *

"""inseriamo delle panchine"""
leg_hanging_est = CUBOID([0.1,0.5,0.3])
leg_hanging_ovest = T(1)(1)(leg_hanging_est)
tablet = T([1,2,3])([-0.15,-0.05,0.3])(CUBOID([1.4,0.6,0.1]))

hanging = (STRUCT([leg_hanging_est,leg_hanging_ovest,tablet]))
hanging = T([1,2,3])([-2.5,-3.5,0.6])(hanging)
hanging_sud = STRUCT([hanging,T(1)(-4)(hanging)])
hanging_nord = T(2)(-2.5)(hanging_sud)
hangings = COLOR([0.96078,0.8705,0.70196])(STRUCT([hanging_nord,hanging_sud]))


"""inseriamo una piazzetta"""
modelPiazza = COLOR([0.75294,0.75294,0.75294])(EXPLODE(1.1,1.1,1)(MKPOLS(larSimplexGrid([6,4]))))
modelPiazza = T([1,2,3])([-7.2,-7,0.6])(modelPiazza)

"""inseriamo dei piccoli alberi(mooolto semplificati)"""
tree_cilynder = COLOR([0.58823,0.29411,0])(STRUCT(MKPOLS(larRod([0.2,1])([64,1]))))
tree_cone = T(3)(1) (COLOR([0.011764,0.75294,0.23523])(CONE([0.4,2])(32)))
tree = T([1,2,3])([7,7,0.6])(STRUCT([tree_cilynder,tree_cone]))
tree_sud = STRUCT([tree,T(1)(-14)(tree)])
tree_nord = T(2)(-14)(tree_sud)
trees = STRUCT([tree_nord,tree_sud])

"""inseriamo dei piccoli lampioni (anche qui molto semplificati)"""
lamp_cylinder = COLOR(BLACK)(STRUCT(MKPOLS(larRod([0.1,0.7])([64,1]))))
lamp_light = T(3)(0.7)(COLOR([0.9921,0.9137,0.0627])(STRUCT(MKPOLS(larBall(0.3)([18,36])))))
lamp_est = T([1,2,3])([-1.4,7.0,0.6])(STRUCT([lamp_cylinder,lamp_light]))
lamp_ovest = T(1)(2.8)(lamp_est)
lamp_middle = T([1,2,3])([-3.9,-4.8,0.6])(STRUCT([lamp_cylinder,lamp_light]))

lamps = STRUCT([lamp_est,lamp_ovest,lamp_middle])

"""inseriamo un marciapiede"""
modelSidewalk_sup =  larRod([17,0.6])([4,1])
modelSidewalk_inf =  larRod([14,0.6])([4,1])
modelSidewalk = COLOR(GRAY)(DIFFERENCE([R([1,2])(PI/4)(STRUCT(MKPOLS(modelSidewalk_sup))),R([1,2])(PI/4)(STRUCT(MKPOLS(modelSidewalk_inf)))]))

#VIEW(modelSidewalk)

"""inseriamo una piccola strada"""
street_1D = POLYLINE([[0,0],[27,0],[27,3],[3,3],[3,27],[0,27],[0,0]])
street_1D = T([1,2])([-15,-15])(street_1D)
street_1D = R([1,2])(-PI/2)(street_1D)
street_3D = COLOR([0.76470,0.6902,0.5686])(PROD([SOLIDIFY(street_1D),Q(0.4)]))

band = T([1,2,3])([-12,-14,0.4])(STRUCT(NN(4)([CUBOID([3,1]),T(1)(6)])))
band_sud = R([1,2])(-PI/2)(band)
band_nord = T([1,2])([0,27])(band)
bands = STRUCT([band_nord,band_sud])

"""altro marciapiede esterno"""
Sidewalk_1D = POLYLINE([[0,0],[28,0],[28,1],[1,1],[1,28],[0,28],[0,0]])
Sidewalk_1D = T([1,2])([-16,-16])(Sidewalk_1D)
Sidewalk_1D = R([1,2])(-PI/2)(Sidewalk_1D)
Sidewalk_3D = COLOR(GRAY)(PROD([SOLIDIFY(Sidewalk_1D),Q(0.6)]))

"""inseriamo lampioni da marciapiede"""
lamp_sidewalk_base = COLOR([0.5960,0.46274,0.32941])(STRUCT(MKPOLS(larRod([0.2,4])([32,1]))))
lamp_sidewalk_light = (T(3)(4)(COLOR([1,0.8,0])(STRUCT(MKPOLS(checkModel(larSphere(0.5)([4,4])))))))
lamp_sidewalk = STRUCT([lamp_sidewalk_base,lamp_sidewalk_light])
lamp_sidewalks_1 =  (STRUCT(NN(4)([lamp_sidewalk,T(1)(6.2)])))
lamp_sidewalks_1 = T([1,2,3])([-9,11.5,0.6])(lamp_sidewalks_1)
lamp_sidewalks_2 = T(2)(-1)(R([1,2])(PI/2)(lamp_sidewalks_1))
lamp_sidewalks = STRUCT([lamp_sidewalks_1,lamp_sidewalks_2])


"""definiamo un segnale stradale"""
signal_base = COLOR([0,0.2784,0.67058])(SOLIDIFY(CIRCUMFERENCE(0.4)(64)))
arrow = SOLIDIFY(POLYLINE([[-0.24,-0.08],[-0.24,0.08],[0.16,0.08],[0.16,0.16],[0.32,0],[0.16,-0.16],[0.16,-0.08],[-0.24,-0.08]]))
signal =R([1,2])(PI)(STRUCT([signal_base,arrow]))
pole = COLOR([0.7607,0.69803,0.50196])(STRUCT(MKPOLS(larRod([0.1,2])([64,1]))))
signal = T([2,3])([0.1,1.6])(R([2,3])(-PI/2)(signal))
road_sign = T([1,2,3])([11.5,-11.7,0.6])(STRUCT([pole,signal]))
road_sign = R([1,2])(PI)(road_sign)


""""""

mockup_3D_urban_area = STRUCT([small_area_plan,hangings,modelPiazza,trees,lamps,modelSidewalk,street_3D,bands,Sidewalk_3D,lamp_sidewalks,road_sign])




#VIEW(mockup_3D_urban_area)
