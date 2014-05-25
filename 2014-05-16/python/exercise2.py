'''
Created on 16/mag/2014

@author: Davide
'''
from exercise1 import *



V,CV = master_apartment
DRSM = COMP([STRUCT,MKPOLS])
DRAW = COMP([VIEW,STRUCT,MKPOLS])


V_s = scalePoints(V,[-1,1,1])
master_apartment_s = V_s,CV 
#VIEW(STRUCT([DRSM(master_apartment_s),DRSM(master_apartment)]))


condominio = assemblyDiagramInit([3,2,11])([[20,6,20],[17,3],[1]+[6,2]*5])
hpc_c = numbers_faces(condominio)
#VIEW(hpc_c)



"""inserisco i piani al condominio"""
condominio = condominio[0],[cell for k,cell in enumerate(condominio[1]) if not (k in range(11,22)+range(22,33)+range(55,66))]
hpc_c = numbers_faces(condominio)
#VIEW(hpc_c)
condominio =  insert_into_cell(master_apartment,condominio,[31,29,27,25,23])
condominio =  insert_into_cell(master_apartment_s,condominio,[9,7,5,3,1])

hpc_c = numbers_faces(condominio)
#VIEW(hpc_c)


"""NOTA IMPORTANTE"""
#PER COLORARLO COME NELL EXERCISE1.PY SAREBBE STATA UN IMPRESA (PER L ENORME QUANTITA DI CELLE) IN QUANTO IL CONDOMINIO LHO COSTRUITO USANDO IL
#DIAGRAM2CELL E QUINDI LE STESSE TECNICHE USATE NELL EXERCISE1.PY. POTREI USARE DELLE TRASLAZIONI O DEGLI SCALE PER COSTRUIRE IL CONDOMINIO ANZICHE
#USARE IL DIAGRAM2CELL, MA NON SO SE L ESERCIZIO2 PREVEDEVA ANCHE EVENTUALMENTE DI USARE QUESTA BANALE METODOLOGIA...ALTRIMENTI IL PROBLEMA NON SI SAREBBE 
#POSTO. DISPIACE MOSTRARE QUESTA ORRENDA COLORAZIONE.... MA NON SAPEVO FARE ALTRIMENTI
condominio = COLOR([0.8117,0.7098,0.23137])(DRSM(condominio))


"""inserisco dei pianerottoli esterni"""
landing = ([[0,0,0],[6,0,0],[1,10,0],[5,10,0],[0,0,2],[6,0,2],[1,10,2],[5,10,2],[0,17,0],[1,15,0],[0,17,2],[1,15,2],[5,15,0],[6,17,0],[5,15,2],[6,17,2]],
           [range(8),[0,2,4,6,8,9,10,11],[1,3,5,7,12,13,14,15],[8,9,10,11,12,13,14,15]])
#VIEW(STRUCT(MKPOLS(landing)))
landing = larApply(t(20,0,7))(landing)
landings = larMoltiply(landing,4,8,[2])
landings = COLOR([0.6,0.2,0])(DRSM(landings))


"""inserisco un tetto"""
roof = COLOR([0.32549,0.10588,0])(DRSM(([[0,0,41],[0,20,41],[46,0,41],[46,20,41],[20,10,50],[26,10,50]],[range(6)])))



"""inserisco una superficia solida curva"""
dom = larDomain([36])
dom2D = larModelProduct([larDomain([20]),larDomain([20])])

curv_1 = larBezierCurve([[0,0],[13,2],[18,4.5],[13,7.5],[8,8.5],[4.5,11.5],[7,15]])
curv_2 = larBezierCurve([[0,2],[7,3.5],[10.5,5.5],[7,7.5],[3,8.5],[1.5,11],[4.5,15]])

c1 = larMap(curv_1)(dom)
c2 = larMap(curv_2)(dom)
floor = larMap(larBezier(S2)([curv_1,curv_2]))(dom2D)
floor = larApply(t(0,-28))(floor)
gardens =  COLOR([0.0117,0.75294,0.23529]) (PROD([STRUCT(MKPOLS(floor)+MKPOLS(larApply(t(17.3,0))(floor))+MKPOLS(larApply(t(34,0))(floor))),Q(1)]))

"""inseriamo delle piazzole rette e curve"""
lat_1 = larBezierCurve([[-10,0],[-8,60],[31.5,85],[58,0]])
lat_2 = larBezierCurve([[-10,0],[-8,-60],[31.5,-85],[58,0]])
extern = larMap(larBezier(S2)([lat_1,lat_2]))(dom2D)
extern = COLOR([0.7607,0.698,0.50196]) (PROD([(STRUCT(MKPOLS(extern))),Q(0.2)]))


"""INCOMINCIO A USARE QUALCOSA CON PLASM (MA NON TUTTO), PERCHE ALTRIMENTI IL PROGRAMMA SI IMPESANTISCE IN MANIERA ECCESSIVA:
   LO FACCIO ANCHE PERCHE, QUESTA ROBA IS SECONDARIA AI FINI DELL'ESERCIZIO E ANCHE DEL PROGETTO DEL FUTURO"""

pz_1 = COLOR(GREEN)(T([1,2])([-78,-155])(CUBOID([68,280])))
pz_2 = COLOR(GRAY)(T([1,2])([-10,-155])(CUBOID([68,280])))
pz_3 = COLOR(GREEN)(T([1,2])([58,-155])(CUBOID([68,280])))

pz_t = STRUCT([pz_1,pz_2,pz_3])



"""inseriamo dei gradini"""
gr1 = T([1,2])([-11,-155])(CUBOID([1,280,3]))
gr2 = T(1)(69)(gr1)
grad =  COLOR([0.5960,0.41176,0.37647]) (STRUCT([gr1,gr2]))


"""inseriamo degli alberi molto semplificati"""
oak = larApply(t(-30,0,0))(larRod(4,25)())
ball_of_leaves =  larApply(t(-30,0,25))(larBall(10)())
tree = STRUCT([COLOR([0.48235,0.10588,0.00784])(STRUCT(MKPOLS(oak))),COLOR([0,0.6588,0.4196])(STRUCT(MKPOLS(ball_of_leaves)))])
trees_est = T(2)(-125)(STRUCT(NN(6)([tree,T(2)(46)])))
trees_ovest = T(1)(108)(trees_est)
trees = STRUCT([trees_est,trees_ovest])


"""inseriamo delle scale a chiocciola per l entrata e una colonna per reggerla"""
scale = spiralStair(width=0.2,R=2,r=0.25,riser=0.1,pitch=2.2,nturns=37,steps=36)
scale = larApply(t(23,12,0))(scale)
column = larApply(t(23,12,0))(larRod(0.25,41)())
column = COLOR([0.50196,0.50196,0.50196]) (DRSM(column))
scale = COLOR([0.466666,0.53333,0.6])(DRSM(scale))
scale_column = STRUCT([scale,column])

#mockup = STRUCT([condominio,coloumns_1,roof,ring,ground_floor,extern])
mockup = STRUCT([condominio,roof,gardens,extern,pz_t,grad,landings,trees,scale_column])

VIEW(mockup)


