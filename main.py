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
                    for j in range( len( gramatica[ i ] ) ):
                        if gramatica[ i ][ j ] == simbol:  # daca apare doar simbolul, in inlocuim cu lambda
                            gramatica[ i ][ j ] = '$'
                        else:  # altfel il eliminam
                            gramatica[ i ][ j ] = gramatica[ i ][ j ].replace( simbol, "" )
                            if len( gramatica[ i ][ j ] ) == 0:
                                gramatica[ i ][ j ] = '$'
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
                for j in gramatica[ i ]:
                    for litera in j:
                        if j.isupper() == True and vizitate[ j ] == False:
                            dfs( j )

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
