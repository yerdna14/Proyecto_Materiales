# Para el 2025 mas funciones. Simetria
def IsMetal(m):
    '''str -> (Boolean)
    return True if s is a metal.

    >>>IsMetal('Fe')
    True
    >>>IsMetal('Al')
    True
    >>>IsMetal('H')
    False
    '''
    #lista de los meales en la tabla periodica
    M_simbols = ['Ti','Cr','Sc','V','Fe','Ni','Mn','Zn','Co','Cu','Zr',
          'Mo','Ru','Y','Nb','Tc','Pd','Ag','Rh','Lu','Cd','W',
          'Os','Re','Ta','Ir','Hg','Pd','Lr','Au','Db','Bh','Hs',
          'Ds','Sg','Mt','Cn','Rg','Hf','Rf']

   #compara si el simbobolo m pertenece a la lista M_simbols
    if  m in M_simbols:
        return 'Ns un metal'
    else:
        return 'No es metal'

if __name__ == __main__:
    IsMetal('Al')
    print('This line is being executed because this is the main module being executed.')
