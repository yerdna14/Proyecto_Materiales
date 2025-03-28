#Pronto mas en este 2025
import math
#Paquete de funciones para calcular el parametro de red a0  de diferentes estructuras cristalinas
def lat_sc(r):
	'''(num)-> float

	Retorna el parametro de red a0 de una estructura
	cristalina cubica simple de radio r en nm.

	>>> rad_sc(2)
	1.0
	>>> rad_sc(5)
	2.5
	'''
	return r*2

def lat_bcc(r):
	'''(num)-> float
	Retorna el parametro de red a0  de una estructura
	cristalina BCC con radio r en mm.

	>>> lat_bcc(4)
	1.7320508075688772
	>>> lat_bcc(5)
	2.1650635094610964
	'''
	c_bcc = math.sqrt(3)/4
	return r/c_bcc

def lat_fcc(r):
	'''(num)-> float
	
	Retorna el parametro de red a0 de una estructura cristalina
	FCC con radio r en nm.
	>>> lat_fcc(4)
	1.4142135623730951
	>>> lat_fcc(5.6568)
	1.9999808199080311
	'''
	c_fcc = math.sqrt(2)/4
	a_fcc = r/c_fcc
	return a_fcc
	
               

def lat_hcp(r):
	'''(num)-> tuple
	
	Retorna el radio de una estructura cristalina
	HCP con parametro de red a en nm.
	>>> lat_hcp(4)
	2.0
	>>> lat_hcp(8)
	4.0
	'''
	c_a = 1.6234
	a_hcp = 2*r
	c_hcp = a_hcp*c_a
	return (a_hcp,c_hcp)

import doctest
doctest.testmod()
#Pronto agregaremos mas en el 2024SS.
