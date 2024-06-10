import math

def rad_sc(a):
	'''(num)-> float

	Retorna el radio de una estructura
	cristalina cubica simple de paramentro
	de red a en nm.

	>>> rad_sc(2)
	1.0
	>>> rad_sc(5)
	2.5
	'''
	return a/2

def rad_bcc(a):
	'''(num)-> float
	Retorna el radio de una estructura
	cristalina BCC con paramentro de red 
	a en mm.

	>>> rad_bcc(4)
	1.7320508075688772
	>>> rad_bcc(5)
	2.1650635094610964
	'''
	c_bcc = math.sqrt(3)/4
	return c_bcc*a

def rad_fcc(a):
	'''(num)-> float
	
	Retorna el radio de una estructura cristalina
	FCC con parametro de red a en nm.
	>>> rad_fcc(4)
	1.4142135623730951
	>>> rad_fcc(5.6568)
	1.9999808199080311
	'''
	c_fcc = math.sqrt(2)/4
	return c_fcc*a

def rad_hcp(a):
	'''(num)-> float
	
	Retorna el radio de una estructura cristalina
	HCP con parametro de red a en nm.
	>>> rad_hcp(4)
	2.0
	>>> rad_hcp(8)
	4.0
	'''
	c_hcp = 2
	return a/c_hcp

import doctest
doctest.testmod()
