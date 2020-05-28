import random

alfabet = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z' }


def eliminareLProductii( gramatica ):
    ok = 0
    while ok == 0:
        ok = 1
        simbol = None
        for i in gramatica:
            if '$' in gramatica[ i ]:
                simbol = i
                ok = 0
                break
        if simbol is not None:
            if len( gramatica[ simbol ] ) == 1:
                gramatica.pop( simbol, None )
                for i in gramatica:
                    for j in gramatica[ i ]:
                        if j == simbol:  # daca apare doar simbolul, in inlocuim cu lambda
                            gramatica[ i ].remove( simbol )
                            gramatica[ i ].add( '$' )
                        else:  # altfel il eliminam
                            s = j.replace( simbol, "" )
                            if len( s ) == 0:
                                s = '$'
                            gramatica[ i ].remove( j )
                            gramatica[ i ].add( s )
            else:
                gramatica[ simbol ].remove( '$' )
                for i in gramatica:
                    if i != simbol:
                        ok = True
                        while ok:  # cat timp set-ul se modifica
                            ok = False
                            try:
                                for j in gramatica[ i ]:
                                    if simbol in j:
                                        for litera in range( len( j ) ):
                                            if j[ litera ] == simbol:
                                                cuvNou = j[ :litera ] + j[ litera + 1: ]
                                                if cuvNou == "":
                                                    cuvNou = "$"
                                                gramatica[ i ].add( cuvNou )
                            except RuntimeError:
                                ok = True
    return gramatica


def eliminareRedenumiri( gramatica ):
    for i in gramatica:
        ok = 1
        while ok == 1:  # cat timp set-ul curent din dict se modifica
            ok = 0
            try:  # daca se modifica set-ul curent,e aruncata exceptie
                for j in gramatica[ i ]:
                    if len( j ) == 1 and j.isupper() == True:
                        gramatica[ i ].update( gramatica[ j ] )
                        gramatica[ i ].remove( j )
            except RuntimeError:
                ok = 1
    return gramatica


def eliminareInutile( gramatica ):
    def inaccesibil():

        def dfs( neterminal ):
            vizitate[ neterminal ] = True
            for i in gramatica[ neterminal ]:
                for litera in i:
                    if litera.isupper() == True and vizitate[ litera ] == False:
                        dfs( litera )

        vizitate = { x: False for x in gramatica }
        dfs( 'S' )
        for i in vizitate:
            if vizitate[ i ] == False:
                gramatica.pop( i, None )

    def neterminate():
        eliminate = set()

    inaccesibil()  # eliminam starile inaccesibile
    neterminate()  # eliminam starile ce nu se termina
    return gramatica


def addNeterminale( gramatica ):
    def verif( litera ):  # verific daca exista un neterminal care are ca produs o unica litera
        for i in gramatica:
            if len( gramatica[ i ] ) == 1:
                for cuv in gramatica[ i ]:
                    if cuv == litera:
                        return i
        return False

    def potInlocui( verifCuv ):

        for verifLitera in verifCuv:
            if verifLitera.isupper() == True:
                return True

        return False

    alfabetFolosit = set( gramatica )
    ok = True
    while ok == True:  # cat timp se modifica dictionarul, trb sa am grija la exceptie
        ok = False
        try:
            for i in gramatica:
                for j in gramatica[ i ]:
                    for pozLitera in range( len( j ) ):
                        if j[ pozLitera ].islower() == True:

                            if potInlocui( j ) == False:  # inlocuiesc doar daca litera mica se afla langa o lutera mare
                                continue
                            verificare = verif( j[ pozLitera ] )
                            if verificare == False:
                                if j[pozLitera].upper() not in gramatica:
                                    lit = j[pozLitera].upper()
                                else:
                                    lit = random.choice( list( alfabet - alfabetFolosit ) )
                                gramatica[ lit ] = set( j[ pozLitera ] )
                                s = j[ :pozLitera ] + lit + j[ pozLitera + 1: ]
                                gramatica[ i ].remove( j )
                                gramatica[ i ].add( s )
                                alfabetFolosit.add( lit )
                            else:
                                s = j[ :pozLitera ] + verificare + j[ pozLitera + 1: ]
                                gramatica[ i ].remove( j )
                                gramatica[ i ].add( s )
        except RuntimeError:
            ok = True

    return gramatica


def maximDouaProductii( gramatica ):
    def cautare( valCautata ):
        for i in gramatica:
            if len(gramatica[ i ])==1 and valCautata in gramatica[i]:
                return i
        return False

    ok = True
    while ok == True:
        ok = False
        try:
            for i in gramatica:
                for j in gramatica[ i ]:
                    if len( j ) > 2:
                        productii = j
                        gramatica[ i ].remove(j)
                        vechiStr = productii[0]
                        nouStr = productii[ 1: ]
                        posibil = cautare( nouStr )
                        if posibil == False:
                            alfabetFolosit = set( gramatica )
                            litera = random.choice( list( alfabet - alfabetFolosit ) )
                            gramatica[ litera ] = { nouStr }
                            gramatica[ i ].add( vechiStr+litera )
                        else:
                            gramatica[ i ].add( vechiStr+posibil )
        except RuntimeError:
            ok = True
    return gramatica


fin = open( "date.in" )
gramatica = dict()
for i in fin:
    l = i.split( "->" )
    gramatica[ l[ 0 ].strip() ] = set( [ x.strip( "|" ) for x in l[ 1 ].replace( "|", " " ).split() ] )
print( gramatica )

gramatica = eliminareLProductii( gramatica )
print( gramatica )
gramatica = eliminareRedenumiri( gramatica )
print( gramatica )
gramatica = eliminareInutile( gramatica )
print( gramatica )
gramatica = addNeterminale( gramatica )
print( gramatica )
gramatica = maximDouaProductii( gramatica )
print( gramatica )
