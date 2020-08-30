def division (a, b):
    type1 = type(a)
    type2 = type(b)
    if a is None:
        return b

    if b is None:
        return a

    #if type1 is not int:
    #    raise TypeError('First input parameter must be an int. Instead it is '+str(type1))

    #if type2 is not int:
    #    raise TypeError('Second input parameter must be an int. Instead it is '+str(type2))

    if type1 is None:
        raise TypeError('First input parameter must be an int. Instead it is Null')

    if type2 is None:
        raise TypeError('Second input parameter must be an int. Instead it is Null')





    return a / b