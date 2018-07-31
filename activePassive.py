def activePassive(np_1,v,np_2):
    aux='has '
    det='the '
    np_2=det+np_2
    
    print(np_1+aux+v+np_2)
    print(np_2+aux+'been '+v+'by '+np_1)

print(activePassive('Mr. Hoffa ','struck ','match '))
