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
            subpalabras = list(filter(None, re.split(r"([+]|-|[*]|[/]|;|,|[.]|=|<=|>=|<|>|[(]|[)]|[[]|[]]|{|}|[\r])", palabra)))
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
                        contCar = noCommetns.index(delimitadores)
                        inicio.append(contCar)
                        token.append("PR_Undefined")
        linea = linea + 1

    for x in range(0, len(lexema)):
        lista = []
        lista.append(lexema[x].replace('\n',''))
        lista.append(numLinea[x])
        lista.append(token[x])
        lista.append(inicio[x])
        listaTokens.append(lista)
    #    print ("lista "),
    #    print (lista)



# Diccionario Tokens
# -----------------------------------------------------------------------------
tknIdentificador = re.compile('[a-zA-Z]+[a-zA-Z1-9/_]*')
tknNumero = re.compile('[0-9]+')
exp_ID = re.compile('[0-9]+')
#    exp_num= re.compile('[0-9]')
#    exp_arit = re.compile('[+|-|*]')
#    exp_rel = re.compile('[= | <=> | <> | != | > | >= | < | <=]')
#    exp_bool = re.compile('[all | and | any | between | exists | in | like | not | or ]')
#    exp_funct= re.compile('[count | max | min | avg | sum]')
#    exp_coment = re.compile('[/* | */ | --]')
#    exp_pc = re.compile('[.|;]')


select = 'PR_select'
from_ = 'PR_from'
where = 'PR_where'
insert = 'PR_insert'
into = 'PR_into'
update = 'PR_update'
set_ = 'PR_set'
del_ = 'PR_delete'
values = 'PR_values'
innerJ = 'PR_IJ'
leftJ = 'PR_LJ'
rightJ = 'PR_RJ'
join = 'PR_join'
on = 'PR_on'
groupBy = 'PR_GBy'
by = 'PR_By'
funct = 'PR_funct'
coment = 'PR_comentario'
op_arti = 'OP_aritmetica'
op_rel = 'OP_relacional'
op_bool = 'OP_booleano'
id_ = 'ID'
op_pc = 'OP_puntuacion'
int_= 'PR_int'
float_ = 'PR_float'
string_ = 'PR_string'
double_ = 'PR_double'
agrup = 'PR_agrupa'


# Autómatas
#-----------------------------------------------------------------------------
def  tokens(listaTokens):
    for token in range(0,len(listaTokens)):
        temp = listaTokens[token][0].lower()
        #print ('temp '+temp)
        if temp == "int":
            listaTokens[token][2] = int_
        elif temp == "float":
            listaTokens[token][2] = float_
        elif temp == "string":
            listaTokens[token][2] = string_
        elif temp == "double":
            listaTokens[token][2] = double_
        elif temp == "true" or temp == "false":
            listaTokens[token][2] = "PR_bool"

        elif temp == "(" or temp == ")" or temp == "{" or temp == "}" or temp == "[" or  temp == "]":
            listaTokens[token][2] = agrup

        elif temp == ";" or temp == "," or temp == "." :
            listaTokens[token][2] = op_pc
    #    elif temp == "&&" ||  temp == "||":

    #        listaTokens[token][2] = "tkn_And"

    #        listaTokens[token][2] = "tkn_Or"

        elif temp == "<" or temp == "=" or temp == ">" or temp == "<=" or temp == ">=" or temp == "==" or temp == "!=":
            listaTokens[token][2] = op_rel

        elif temp == "+" or temp == "-" or temp == "*" or temp == "/":
            listaTokens[token][2] = op_arti

        elif temp == "select":
            listaTokens[token][2] = select
        elif temp == "from":
            listaTokens[token][2] = from_
        elif temp == "where":
            listaTokens[token][2] = where
        elif temp == "insert":
            listaTokens[token][2] = insert
        elif temp == "into":
            listaTokens[token][2] = into
        elif temp == "update":
            listaTokens[token][2] = update
        elif temp == "set":
            listaTokens[token][2] = set_
        elif temp == "delete":
            listaTokens[token][2] = del_
        elif temp == "values":
            listaTokens[token][2] = values
        elif temp == "inner":
            listaTokens[token][2] = innerJ
        elif temp == "left":
            listaTokens[token][2] = leftJ
        elif temp == "right":
            listaTokens[token][2] = rightJ
        elif temp == "join":
            listaTokens[token][2] = join
        elif temp == "on":
            listaTokens[token][2] = on
        elif temp == "group":
            listaTokens[token][2] = groupBy
        elif temp == "by":
            listaTokens[token][2] = by
        elif temp == "null":
            listaTokens[token][2] = 'PR_null'
        elif temp == "count" or  temp == "max" or temp == "min" or temp == "avg" or temp == "sum":
            listaTokens[token][2] = funct
#    exp_bool = re.compile('[all | and | any | between | exists | in | like | not | or ]')
        elif temp == "and" or temp == "or" or  temp == "any" or temp == "in" or temp == "like" or temp == "not":
            listaTokens[token][2] = op_bool


        elif re.match(tknIdentificador, temp):
            m = re.match(tknIdentificador, temp)
            #print m;
            if len(m.group(0)) == len(temp):
            #    print ('m:     '+m.group(0));
                listaTokens[token][2] = "TKN_id"
            else:
                print ("Error cadena no encontrada en la Linea: ", listaTokens[token][1])

        elif re.match(tknNumero, temp): #evaluar exp reg
            m = re.match(tknNumero, temp)
            if len(m.group(0)) == len(temp):
                listaTokens[token][2] = "PR_int"
            #    print ('m:     '+m.group(0));
            else:
                print ("Error cadena no encontrada en la Linea: ", listaTokens[token][1])
        else:
            print ("Error cadena no encontrada en la Linea: ",listaTokens[token][1])
            #Agregar a tabla de errores

# Tabla de Símbolos
#-----------------------------------------------------------------------------
tablaSimbolos = {}

# Hasta antes de Semántico, solo registra los identificadores en la TS.
def tablaSim(listaTokens):
    for id in range(0,len(listaTokens)):
        tam = len(listaTokens[id][0])
        if listaTokens[id][2] == "TKN_id":
            if (tablaSimbolos.has_key(listaTokens[id][0]) == False):
                tablaSimbolos[listaTokens[id][0]] = {'Lexema': listaTokens[id][0], 'Inicio': [listaTokens[id][3]],'Tam': tam , 'Token':[listaTokens[id][2]], 'Linea': [listaTokens[id][1]]}

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




preprocesamiento()
tokens(listaTokens)
imprimir(listaTokens)
tablaSim(listaTokens)
imprimirTS()

#for key in tablaSimbolos:
#    print key, ":", tablaSimbolos[key]
