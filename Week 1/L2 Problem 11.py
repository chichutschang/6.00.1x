varA = "hola"
varB = -2

if (type(varA) or type(varB) == str):
    print "string involved"

else:
    if (varA == varB):
        print "equal"

    elif (varA > varB):
        print "bigger"

    else:
        print "smaller"