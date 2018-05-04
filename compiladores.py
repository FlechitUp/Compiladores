# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
file = open('codigoFuente.txt', 'r')
data = file.readlines()
file.close()
listaTokens = []

# Comentarios
#-----------------------------------------------------------------------------
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remueve los comentarios de varias filas (/*COMMENT */)
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remueve todos los comentarios de una sola linea (//COMMENT\n )
    if (re.compile("//*.*"), "", string):
        string = re.sub(re.compile("//*.*"), "#@", string)
        print("cadena: "+string);
    return string




# Diccionario Tokens
# -----------------------------------------------------------------------------
exp_ID = re.compile('[a-zA-Z]+[a-zA-Z1-9/_]*')
exp_Num = re.compile('[0-9]+')

select = 'PR_select'
from_ = 'PR_from'
where = 'PR_where'
insert = 'PR_insert'
into = 'PR_into'
update = 'PR_update'
set_ = 'PR_set'
del_ = 'PR_delete'
values = 'PR_values'
innerJ = 'PR_inner'
leftJ = 'PR_left'
rightJ = 'PR_right'
join = 'PR_join'
on = 'PR_on'
groupBy = 'PR_GBy'
by = 'PR_By'
funct = 'PR_funct'
coment = 'PR_comentario'
op_arti = 'OP_aritmetica'
op_rel = 'OP_relacional'
op_bool = 'OP_booleano'
id_ = 'PR_id'
op_pc = 'OP_puntuacion'
int_= 'PR_int'
float_ = 'PR_float'
string_ = 'PR_string'
double_ = 'PR_double'
agrup = 'PR_agrupa'


# Preprocesamiento
#-----------------------------------------------------------------------------
def preprocesamiento():
    contador = 0
    contCar = 0
    linea = 1
    lexema = []
    numLinea = []
    token = []
    inicio = []

    for renglon in data:
        noCommetns = removeComments(renglon)
        #print("sin comentario: "+renglon)
        for palabra in  noCommetns.split(' '):
        #    if palabra == "":
        #        continue

            #print("palabra:"+palabra+"n")
            subpalabras = list(filter(None, re.split(r"([+]|-|[*]|[/]|;|,|[.]|[']|=|<=|>=|<|>|[(]|[)]|[[]|[]]|{|}|[\r])", palabra)))
            #se sacan las subpalabras que pueden haber ejem. 2+4 -> 2 + 4
            for delimitadores in subpalabras:
                if(delimitadores == "#@"):
                    print ("Error de comentario en la Linea: ",linea)
                    contador += 1
                    break
                contador += 1
                #print '%s) %s' % (str(contador), delimitadores)
                if(delimitadores != ('\n')):
                    if (delimitadores != ('\r')):
                        lexema.append(delimitadores)
                        numLinea.append(linea)
                    #    contCar = noCommetns.index(delimitadores)
                    #    inicio.append(contCar)
                        token.append("PR_Undefined")
        linea = linea + 1

    x=0;
    numToken = 0;
    while x < len(lexema):
        lista = []
        lexem = lexema[x].replace('\n','')
        temp = lexem.lower()
        """    lista.append(lexema[x].replace('\n',''))
            lista.append(numLinea[x])
            lista.append(token[x])
            lista.append(inicio[x])
        """
                #print ('temp '+temp)
                ##falta poner esto
        if  temp == "'":
            if (x+1) and re.match(exp_ID, lexema[x+1]):
                    #print m;

                if lexema[x+2] == "'" :
                    lexem += lexema[x+1]+lexema[x+2]
                    ##    listaTokens[x][2] = op_pc
                    lista.append(lexem)
                    lista.append(numLinea[x])
                    lista.append(token[x])
                        # lista.append(inicio[x])
                    listaTokens.append(lista)
                    listaTokens[numToken][2] =  "PR_string"
                    numToken+=1
                    x = x + 2

        #    lista.append(lexem)
        #    lista.append(numLinea[x])
        #    lista.append(token[x])
        #    # lista.append(inicio[x])
        #    listaTokens.append(lista)
        #    listaTokens[numToken][2] = "OP_comilla"
        #    numToken+=1
        elif temp == "true" or temp == "false":
        #    listaTokens[x][2] = "PR_bool"
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
        #    # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] = "PR_bool"
            numToken+=1

        elif temp == "(" or temp == ")" or temp == "{" or temp == "}" or temp == "[" or  temp == "]":
            #listaTokens[x][2] = agrup
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] = agrup
            numToken+=1

            #    elif temp == "&&" ||  temp == "||":

            #        listaTokens[x][2] = "tkn_And"

            #        listaTokens[x][2] = "tkn_Or"

        elif temp == "<" or temp == "=" or temp == ">" or temp == "<=" or temp == ">=" or temp == "==" or temp == "!=":
        #    listaTokens[x][2] = op_rel
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] = op_rel
            numToken+=1

        elif temp == "+" or temp == "-" or temp == "*" or temp == "/":
        #    listaTokens[x][2] = op_arti
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] = op_arti
            numToken+=1

        elif temp == "select":
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] = select
            numToken+=1

        elif temp == "from":
            #listaTokens[x][2] = from_
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  from_
            numToken+=1
        elif temp == "where":
            #listaTokens[x][2] = where
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  where
            numToken+=1
        elif temp == "insert":
            #listaTokens[x][2] = insert
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  insert
            numToken+=1
        elif temp == "into":
        #    listaTokens[x][2] = into
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  into
            numToken+=1
        elif temp == "update":
        ##    listaTokens[x][2] = update
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  update
            numToken+=1
        elif temp == "set":
        ##    listaTokens[x][2] = set_
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  set_
            numToken+=1
        elif temp == "delete":
        #    listaTokens[x][2] = del_
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  del_
            numToken+=1
        elif temp == "values":
        #    listaTokens[x][2] = values
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  values
            numToken+=1
        elif temp == "inner":
        #    listaTokens[x][2] = innerJ
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  innerJ
            numToken+=1
        elif temp == "left":
        #    listaTokens[x][2] = leftJ
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  leftJ
            numToken+=1
        elif temp == "right":
            #listaTokens[x][2] = rightJ
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  rightJ
            numToken+=1
        elif temp == "join":
        ##    listaTokens[x][2] = join
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  join
            numToken+=1
        elif temp == "on":
        #    listaTokens[x][2] = on
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  on
            numToken+=1
        elif temp == "group":
        ##    listaTokens[x][2] = groupBy
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  groupBy
            numToken+=1
        elif temp == "by":
        #    listaTokens[x][2] = by
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  by
            numToken+=1
        elif temp == "null":
        #    listaTokens[x][2] = 'PR_null'
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  'PR_null'
            numToken+=1
        elif temp == "count" or  temp == "max" or temp == "min" or temp == "avg" or temp == "sum":
        #    listaTokens[x][2] = funct
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  funct
            numToken+=1

        #    exp_bool = re.compile('[all | and | any | between | exists | in | like | not | or ]')
        elif temp == "and" or temp == "or" or  temp == "any" or temp == "in" or temp == "like" or temp == "not":
            ##listaTokens[x][2] = op_bool
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  op_bool
            numToken+=1


        elif re.match(exp_ID, temp):
            m = re.match(exp_ID, temp)
                    #print m;
            if len(m.group(0)) == len(temp):
                    #    print ('m:     '+m.group(0));
        #        listaTokens[x][2] = id_
                lista.append(lexem)
                lista.append(numLinea[x])
                lista.append(token[x])
                # lista.append(inicio[x])
                listaTokens.append(lista)
                listaTokens[numToken][2] =  id_
                numToken+=1
            else:
                print ("Error cadena no encontrada en la Linea: ", listaTokens[x][1])

        elif re.match(exp_Num, temp): #evaluar exp reg
            m = re.match(exp_Num, temp)
            #es un float
            if (x+1)<len(lexema) and lexema[x+1] == "." and re.match(exp_Num, lexema[x+2] ):
                lexem += lexema[x+1]+lexema[x+2]
            ##    listaTokens[x][2] = op_pc
                lista.append(lexem)
                lista.append(numLinea[x])
                lista.append(token[x])
                # lista.append(inicio[x])
                listaTokens.append(lista)
                listaTokens[numToken][2] =  "PR_float"
                numToken+=1
                x = x + 2
            elif len(m.group(0)) == len(temp):
                lista.append(lexem)
                lista.append(numLinea[x])
                lista.append(token[x])
                # lista.append(inicio[x])
                listaTokens.append(lista)
                listaTokens[numToken][2] = "PR_int"
                numToken+=1
            #    listaTokens[x][2] = "PR_int"
            #    print ('m:     '+m.group(0));
            else:
                print ("Error cadena no encontrada en la Linea: ", temp)
        elif temp == ";" or temp == "," or temp == "." :
            lista.append(lexem)
            lista.append(numLinea[x])
            lista.append(token[x])
            # lista.append(inicio[x])
            listaTokens.append(lista)
            listaTokens[numToken][2] =  op_pc
            numToken+=1
        else:
            print ("Error cadena no encontrada en la Linea: ",temp)

        x+=1;


                ###fin del while
                    #Agregar a tabla de errores
################################################################3333

    #    print ("lista "),
    #    print (lista)


# Tabla de Símbolos
#-----------------------------------------------------------------------------
tablaSimbolos = {}

# Hasta antes de Semántico, solo registra los identificadores en la TS.
def tablaSim(listaTokens):
    for id in range(0,len(listaTokens)):
        tam = len(listaTokens[id][0])
        if listaTokens[id][2] == id_:
            if (tablaSimbolos.has_key(listaTokens[id][0]) == False):
                tablaSimbolos[listaTokens[id][0]] = {'Lexema': listaTokens[id][0], 'Tam': tam , 'Token':listaTokens[id][2], 'Linea': [listaTokens[id][1]]}
#"""'Inicio': [listaTokens[id][3]],"""
            #Else actualiza linea.
    #       if (tablaSimbolos.has_key(listaTokens[id][0]) == False):
    #            if listaTokens[id][2] == "TKN_id":

#                tablaSimbolos[listaTokens[id][0]] = {'Lexema': listaTokens[id][0], 'Valor': '','Tam': '', 'Type':'','Linea': [listaTokens[id][1]]}
            else:
                tablaSimbolos[listaTokens[id][0]]['Linea'].append(listaTokens[id][1])

                # Si ya están indexados, se actualiza numLínea
                #porque se tienen que poner en todas las lineas en donde se enceuntre


def imprimirTS():
    for key in tablaSimbolos:
        print key, ":", tablaSimbolos[key]




# Imprimir
#-----------------------------------------------------------------------------
def imprimir(listaTokens):
    cont = 0
    for x in range(0, len(listaTokens)):
        cont += 1
        print (str(cont) +") " ),
        print ( listaTokens[x])
    print ("***********************************************")



class noTerminal:
    def __init__(self):
        self.name = None
        self.terminal = None  # Me permite acceder a mi TS en la pos "lexema"
        self.produccion = None



noTerminales = ['S','C','R','F','W','J','Q','Z','L','O','I','V','A','B','U']
terminales = [
 'PR_select', 'PR_from', 'PR_where',
 'PR_insert', 'PR_into', 'PR_update',
 'PR_set','PR_delete', 'PR_values'
 'PR_IJ', 'PR_LJ', 'PR_RJ',
 'PR_join', 'PR_on', 'PR_GBy',
 'PR_By', 'PR_funct', 'PR_comentario',
 'OP_aritmetica', 'OP_relacional',
 'OP_booleano', 'PR_id', 'OP_puntuacion',
 'PR_int', 'PR_float','PR_string',
'PR_double','PR_agrupa']
S = noTerminal();
S.name = 'S'
S.terminal = [[ 'PR_select', 'C', 'R','W'],
              ['PR_delete', 'R', 'W'],
              ['PR_update', 'U', 'W'],
              ['PR_insert', 'PR_into', 'I']]
S.produccion = [ 'PR_select',
              'PR_delete',
              'PR_update',
              'PR_insert']

C = noTerminal();
C.name = 'C'
C.terminal = [['OP_aritmetica'],
              ['E'],
              ['F', 'V']]
C.produccion = ['OP_aritmetica',
              'PR_id',
              'PR_funct']


E = noTerminal();
E.name = 'E'
E.terminal = [['L','D'],
              ['L','D'],
              ['L','D'],
              ['L','D'],
              ['L','D']]
E.produccion = ['PR_id',
                'PR_int',
                'PR_float',
                'PR_bool',
                'PR_string']

D = noTerminal();
D.name = 'D'
D.terminal = [[],
              ['OP_puntuacion','E'],[],
              [],[],[],[],[],[]]
D.produccion = ['PR_from',
                'OP_puntuacion',
                'PR_where',
                'PR_inner',
                'PR_left',
                'PR_right',
                'OP_relacional',
                'OP_booleano',
                '$']

R = noTerminal();
R.name = 'R'
R.terminal = [['PR_from', 'PR_id']]
R.produccion = ['PR_from']


F = noTerminal();
F.name = 'F'
F.terminal = [['PR_funct'],]
F.produccion = ['PR_funct']


W = noTerminal();
W.name = 'W'
W.terminal = [['PR_where','Q'],
              ['J','PR_join','PR_id','PR_on','Q'],
              ['J','PR_join','PR_id','PR_on','Q'],
              ['J','PR_join','PR_id','PR_on','Q'],
              []]
W.produccion = ['PR_where',
              'PR_inner',
              'PR_left',
              'PR_right',
              '$']

J = noTerminal();
J.name = 'J'
J.terminal = [['PR_inner'],
              ['PR_left'],
              ['PR_right']]
J.produccion = ['PR_inner',
              'PR_left',
              'PR_right']


Q = noTerminal();
Q.name = 'Q'
Q.terminal = [['E','Z'],
              ['E','Z'],
              ['E','Z'],
              ['E','Z'],
              ['E','Z']]
Q.produccion = ['PR_id',
                'PR_int',
                'PR_float',
                'PR_bool',
                'PR_string']


Z = noTerminal();
Z.name = 'Z'
Z.terminal = [[],[],
              [],[],
              ['O','Q'],
              ['O','Q'],
              ['$']]
Z.produccion = ['PR_where',
                'PR_inner',
                'PR_left',
                'PR_right',
                'OP_relacional',
                'OP_booleano',
                '$']

L = noTerminal();
L.name = 'L'
L.terminal = [['PR_id'],
              ['PR_int'],
              ['PR_float'],
              ['PR_bool'],
              ['PR_string']]
L.produccion = ['PR_id',
                'PR_int',
                'PR_float',
                'PR_bool',
                'PR_string']

O = noTerminal();
O.name = 'O'
O.terminal = [['OP_relacional'],
              ['OP_booleano']]
O.produccion = ['OP_relacional',
                'OP_booleano']

I = noTerminal();
I.name = 'I'
I.terminal = [['PR_id','V','PR_values','V']]
I.produccion = ['PR_id']

V = noTerminal();
V.name = 'V'
V.terminal = [['PR_agrupa','A','PR_agrupa']]
V.produccion = ['PR_agrupa']

A = noTerminal();
A.name = 'A'
A.terminal = [['L', 'B'],
              ['L', 'B'],
              ['L', 'B'],
              ['L', 'B'],
              ['L', 'B']]
A.produccion = ['PR_id',
                'PR_int',
                'PR_float',
                'PR_bool',
                'PR_string']


B = noTerminal();
B.name = 'B'
B.terminal = [[],
              ['OP_puntuacion','A'],
              []]
B.produccion = ['PR_agrupa',
                'OP_puntuacion',
                '$']

U = noTerminal();
U.name = 'U'
U.terminal = [['PR_id','PR_set','Q']]
U.produccion = ['PR_id']

tablaSintactica = [S,C,E,D,R,F,W,J,Q,Z,L,O,I,V,A,B,U]


def pilaSintac(listaTokens):
    listaErrores=[]
    pila =['$','S']
    lista = []
    lista.append('$')
    linea=[2]
    lista.append(linea)
    lista.append('$')
    listaTokens.append(lista)
    t=0
    error =0
    i=0
    #for i in range (0,len(listaTokens)):
    while i < len(listaTokens) and error !=2:
        print ''
        print listaTokens[i][2]+" -> "+listaTokens[i][0]
        while t <len(tablaSintactica) :
            if tablaSintactica[t].name == pila[len(pila)-1]:
                print tablaSintactica[t].name
                error = 0

                for j in range (0,len(tablaSintactica[t].produccion)):
                    if tablaSintactica[t].produccion[j] == listaTokens[i][2]:
                        error = 1
                        print 'Produccion: ',tablaSintactica[t].terminal[j]
                        pila.pop(len(pila)-1);
                        #vamos a buscar la produccion
                        #hay que poner la produccion en la pila al revez
                        for k in range (len(tablaSintactica[t].terminal[j])-1,-1,-1):
                            pila.append(tablaSintactica[t].terminal[j][k]);
                        print "agregando al revez"
                        print pila
                if error==0:
                    error =1
                    listaE=[]
                    listaE.append(listaTokens[i][1])
                    listaE.append(tablaSintactica[t].produccion)
                    listaErrores.append(listaE)
                #    listaTokens[i][2]=tablaSintactica[t].produccion[0]
                    i+=1
                    ##me salto el error
                    print '-------------------ERROR--------------------'
                #    break
            t+=1
        #    print pila
        if pila[len(pila)-1]== listaTokens[i][2]:
            pila.pop(len(pila)-1);
            print "eliminado"
            print pila
        else:
            i-=1
        i+=1
        t=0
        print pila
        
    print ''
    print '*********************************************************************'
    for value in listaErrores:
        print ''
        print 'Error en la linea:',value[0]
        print 'Produccion esperada: '
        print value[1]




preprocesamiento()
#tokens(listaTokens)
imprimir(listaTokens)
tablaSim(listaTokens)
imprimirTS()
pilaSintac(listaTokens)
