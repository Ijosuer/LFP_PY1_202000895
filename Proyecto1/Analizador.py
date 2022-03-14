from Token import Token
from Error import Error
from prettytable import PrettyTable
class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0
        self.abierto = False
    
    def agregar_Token(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''
    
    def agregar_Error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter \'' + caracter + '\' no reconocido',linea,columna))

    def s0(self,caracter):
        '''Estado 0'''
        if caracter.isalpha() and not self.abierto:
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == '~':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\"':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\'':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter.isalpha() and self.abierto:
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == ']':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.agregar_Error(caracter,self.linea,self.columna)
    
    def s1(self,caracter):
        '''Estado 1'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_Token(self.buffer,self.linea,self.columna,'reservada_' + self.buffer)
            self.estado = 0
            self.i -= 1

    def s2(self):
        '''Estado 2'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'virgulilla')
        self.estado = 0
        self.i -= 1
    
    def s3(self):
        '''Estado 3'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'menorQue')
        self.estado = 0
        self.i -= 1
    
    def s4(self):
        '''Estado 4'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'mayorQue')
        self.estado = 0
        self.i -= 1
    
    def s5(self):
        '''Estado 5'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'comillas')
        self.estado = 0
        self.i -= 1
        if self.abierto:
            self.abierto = False
        else:
            self.abierto = True
    
    def s6(self):
        '''Estado 6'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'comillaSimple')
        self.estado = 0
        self.i -= 1
        if self.abierto:
            self.abierto = False
        else:
            self.abierto = True
    
    def s7(self,caracter):
        '''Estado 7'''
        if caracter.isalpha():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == ' ':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_Token(self.buffer,self.linea,self.columna,'valor')
            self.estado = 0
            self.i -= 1

    def s8(self):
        '''Estado 8'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'corcheteIzquierdo')
        self.estado = 0
        self.i -= 1
    
    def s9(self):
        '''Estado 9'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'corcheteDerecho')
        self.estado = 0
        self.i -= 1
    
    def s10(self):
        '''Estado 10'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'dosPuntos')
        self.estado = 0
        self.i -= 1
    
    def s11(self):
        '''Estado 11'''
        self.agregar_Token(self.buffer,self.linea,self.columna,'coma')
        self.estado = 0
        self.i -= 1

    def analizar(self,cadena):
        cadena += '$'
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2()
            elif self.estado == 3:
                self.s3()
            elif self.estado == 4:
                self.s4()
            elif self.estado == 5:
                self.s5()
            elif self.estado == 6:
                self.s6()
            elif self.estado == 7:
                self.s7(cadena[self.i])
            elif self.estado == 8:
                self.s8()
            elif self.estado == 9:
                self.s9()
            elif self.estado == 10:
                self.s10()
            elif self.estado == 11:
                self.s11()
            self.i += 1
    
    def imprimirTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema","Linea","Columna","Tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema,token.linea,token.columna,token.tipo])
        print(x)
    
    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripción","Linea","Columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion,error.linea,error.columna])
        print(x)