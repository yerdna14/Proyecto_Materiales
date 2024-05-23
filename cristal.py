#Cristalino 

def v_cubic(a): 
	'''
        (num) -> float
	
	Retorna el volumen de una estructura cubica 
	con parametro de red a.

	>>> v_cubic(2)
	8.0
	>>> v_cubic(3)
	27.0
    '''
	return a**3

def v_tet(a,b):
	'''(number, number) -> number
	Retorna el volumen de un solido con estructura 
	tetaedrica con parametros de red a,b.

	>>> v_tet(2,3)
	12
	>>> v_tet(3,2)
	18
	'''
	return a**2*b 

def v_orto(a,b,c):
	'''(number,number,number) -> number
	Retorna el volumen de un solido con estructura
	ortorombica con parametros de red a,b y c.

	>>> v_orto(2,3,4)
	24
	>>> v_orto(4,5,9)
	180
	'''
	return a*b*c
			