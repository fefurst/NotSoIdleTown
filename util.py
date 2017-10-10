

def valor(recurso, msg):
    m = re.search(recurso+': ([0-9]*\.[0-9]*) ([K|M])', msg)
    #print(m.group(1))
    #print(m.group(2))
    valor = 0.0
    if m != None:
        valor = float(m.group(1))
        if m.group(2) == 'K':
            valor = valor * (10^3)    
        else if m.group(2) == 'M':
            valor = valor * (10^6)

    return valor
