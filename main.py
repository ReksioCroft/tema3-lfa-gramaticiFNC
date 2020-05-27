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
                                gramatica[ i ][j] = '$'
            else:
                gramatica[ simbol ].pop( gramatica[ simbol ].index( '$' ) )
                for i in gramatica:
                    if i != simbol:
                        for j in range( len( gramatica[ i ] ) ):
                            if simbol in gramatica[ i ][ j ]:
                                s = gramatica[ i ][ j ].replace( simbol, "" )
                                if len( s ) == 0:
                                    s = '$'
                                gramatica[ i ].append( s )
    return gramatica


def eliminareRedenumiri( gramatica ):

    return gramatica


fin = open( "date.in" )
gramatica = dict()
for i in fin:
    l = i.split( "->" )
    gramatica[ l[ 0 ].strip() ] = [ x.strip( "|" ) for x in l[ 1 ].replace( "|", " " ).split() ]
print( gramatica )

gramatica = eliminareLProductii( gramatica )
print( gramatica )
gramatica = eliminareRedenumiri( gramatica )
print(gramatica)