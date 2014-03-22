from pyplasm import *

"""travi da est a ovest"""
holderColumnsBottom1 = COLOR (BLACK) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.3,3.8,-0.3])]))
holderColumnsTop1 =  COLOR (BLACK) (INSR (PROD) ([QUOTE([-0.45,0.1,-1.6,0.1,-1.6,0.1]),QUOTE([-0.1,4.2,-0.1])]))

"""travi da nord a sud"""
holderColumnsBottom2 = COLOR (YELLOW) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45])]))
holderColumnsMedium2 =  COLOR (YELLOW) (INSR (PROD) ([QUOTE([-0.3,3.8,-0.3]),QUOTE([-0.45,0.1,-3.3,0.1,-0.45])]))
holderColumnsTop2 = COLOR (ORANGE) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.18,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.885,0.1,-0.18])]))

"""fasce superiori della ringhiera"""
overRailing1 = INSR (PROD) ([QUOTE([-0.2,0.05,-3.9,0.05,-0.2]),QUOTE([-0.15,4.1,-0.15])]) 
overRailing2 = COLOR (WHITE) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.2,0.05,-3.9,0.05,-0.2])]))

"""unico pavimento"""
floor1 = COLOR (RED) (INSR (PROD) ([QUOTE([-0.15,4.1,-0.15]),QUOTE([-0.15,4.1,-0.15])]))

"""base del tetto"""
roof = COLOR (BLUE) (INSR (PROD) ([QUOTE([4.4]),QUOTE([4.4])]))

"""base del sopra-tetto"""
roofTop =  COLOR (GREEN) (INSR (PROD) ([QUOTE([-1.2,2]),QUOTE([-1.2,2])]))

"""piani per le colonne"""
bases = COLOR (WHITE) (PROD([QUOTE([-0.4,0.2,-1.5,0.2,-1.5,0.2]),QUOTE([-0.4,0.2,-3.2,0.2,-0.4])])) 



two_and_half_model = STRUCT([T(3)(2)(holderColumnsBottom1),T(3)(4)(holderColumnsTop1),T(3)(4.76)(overRailing1),T(3)(4.36)(floor1),
                             T(3)(4.76)(overRailing2),T(3)(1)(holderColumnsBottom2),T(3)(3)(holderColumnsMedium2),T(3)(4.2)(holderColumnsTop2), 
                             T(3)(5.51)(roof),T(3)(7.31)(roofTop),bases])
#VIEW(two_and_half_model)
