'''
Created on 16/mag/2014

@author: Davide
'''
from exercise1 import *
from boolean1 import *

V,CV = master_apartment
DRSM = COMP([STRUCT,MKPOLS])
DRAW = COMP([VIEW,STRUCT,MKPOLS])


V_s = scalePoints(V,[-1,1,1])
master_apartment_s = V_s,CV 
#VIEW(STRUCT([DRSM(master_apartment_s),DRSM(master_apartment)]))


condominio = assemblyDiagramInit([3,1,8])([[20,3,20],[15],[4,2]*4])
#DRAWS(condominio)
hpc_c = numbers_faces(condominio)
#VIEW(hpc_c)



"""inserisco i piani al condominio"""
condominio =  insert_into_cell(master_apartment,condominio,[22,20,18,16])
condominio =  insert_into_cell(master_apartment_s,condominio,[6,4,2,0])


hpc_c = numbers_faces(condominio)
#VIEW(hpc_c)
V,CV = condominio
condominio = V,[cell for k,cell in enumerate(CV) if not (k in [0,1,2,3,12,13,14,15])]
condominio = T(3)(8)(DRSM(condominio))
#DRAW(condominio)


"""inserisco colonne"""
coloumns_1 = COLOR([0.25098,0.25098,0.25098])(PROD([PROD([QUOTE([0.1,-19.8,0.1,-3,0.1,-19.8,0.1]),QUOTE([0.1,-7.35,0.1,-7.35,0.1])]),Q(38)]))

"""inserisco un tetto"""
roof = COLOR([0.4823,0.10588,0.00784])(T(3)(38)(JOIN([CUBOID([43,15]),MK([21.5,7.5,8])])))

ring = COLOR ([0.11764,0.5647,1]) (STRUCT([CUBOID([43,0.1,0.3]),T(2)(14.9)(CUBOID([43,0.1,0.3])),CUBOID([0.1,15,0.3]),T(1)(42.9)(CUBOID([0.1,15,0.3]))]))


"""inserisco una superficia curva"""
dom = larDomain([36])
dom2D = larModelProduct([larDomain([20]),larDomain([20])])

curv_1 = larBezierCurve([[0,0],[13,2],[18,4.5],[13,7.5],[8,8.5],[4.5,11.5],[7,15]])
curv_2 = larBezierCurve([[0,2],[7,3.5],[10.5,5.5],[7,7.5],[3,8.5],[1.5,11],[4.5,15]])

c1 = larMap(curv_1)(dom)
c2 = larMap(curv_2)(dom)

supr = STRUCT(MKPOLS(larMap(larBezier(S2)([curv_1,curv_2]))(dom2D)))
ground_floor = COLOR ([0.11764,0.5647,1]) (PROD([(STRUCT([supr,T(1)(14)(supr),T(1)(28)(supr)])),Q(0.1)]))
#extern = COLOR([0.7607,0.698,0.50196])(T([1,2])([-10,-10])(CUBOID([63,35])))

lat_1 = larBezierCurve([[-10,7.5],[31.5,55],[53,0]])
lat_2 = larBezierCurve([[-10,7.5],[31.5,-45],[53,0]])
extern = COLOR([0.7607,0.698,0.50196]) (STRUCT(MKPOLS(larMap(larBezier(S2)([lat_1,lat_2]))(dom2D))))



condominio =  COLOR([0.9686,0.9098,0.6235])(condominio)


mockup = STRUCT([condominio,coloumns_1,roof,ring,ground_floor,extern])

#VIEW(mockup)


