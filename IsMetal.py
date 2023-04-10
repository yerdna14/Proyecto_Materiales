def IsMetal(s):
    '''str -> (Boolean)
    return True if s is a metal

    >>>IsMetal('Fe')
    True
    >>>IsMetal('Al')
    True
    >>>IsMetal('H')
    False
    '''
    Metals = ['Ti','Cr','Sc','V','Fe','Ni','Mn','Zn','Co','Cu','Zr',
          'Mo','Ru','Y','Nb','Tc','Pd','Ag','Rh','Lu','Cd','W',
          'Os','Re','Ta','Ir','Hg','Pd','Lr','Au','Db','Bh','Hs',
          'Ds','Sg','Mt','Cn','Rg','Hf','Rf']

    return  s in Metals 