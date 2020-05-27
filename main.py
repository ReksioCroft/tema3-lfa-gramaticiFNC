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
                        if gramatica[ i ][ j ] == simbol:
                            gramatica[ i ][ j ] = '$'
                        else:
                            gramatica[ i ][ j ] = gramatica[ i ][ j ].replace( simbol, "" )
                            if len( gramatica[ i ][ j ] ) == 0:
                                gramatica[ i ][ j ] = '$'
            else:
                gramatica[ simbol ].remove( '$' )
                for i in gramatica:
                    if i != simbol:
                        for j in gramatica[ i ]:
                            if '$' in j:
                                s = [ j ].replace( simbol, "" )
                                if len( s ) == 0:
                                    s = '$'
                                gramatica[ i ].pop( j )
                                gramatica[ i ].insert( s )
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
