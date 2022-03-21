from Token import Token
from Error import Error
from prettytable import PrettyTable
import webbrowser
import time

class Scanner:
    def __init__(self):
        self.buffer = ''
        self.fila = 1
        self.columna = 1
        self.estado = 0
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0
        self.flag_comillas = False
    
    def agregar_Token(self,caracter,fila,columna,token):
        self.listaTokens.append(Token(caracter,fila,columna,token))
        self.buffer = ''
    
    def agregar_Error(self,caracter,fila,columna):
        if ord(caracter)>= 48 and ord(caracter)<= 57:
            self.listaErrores.append(Error('Caracter \'' + caracter + '\' error de tipo Numero',fila,columna))
        else:
            self.listaErrores.append(Error('Caracter \'' + caracter + '\' error de tipo Simbolo',fila,columna))
    def s0(self,caracter):
        '''Estado 0'''
        if (caracter.isalpha() and not self.flag_comillas):
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == '~':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == ']':
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
        elif (caracter.isalpha() or (ord(caracter)>= 48 and ord(caracter)<= 57)) and self.flag_comillas:
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
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
            self.fila += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.agregar_Error(caracter,self.fila,self.columna)
    
    def s1(self,caracter):
        '''Estado 1'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            if (self.buffer.lower() == 'formulario' or self.buffer.lower() == 'tipo' 
            or self.buffer.lower() == 'valor' or self.buffer.lower() == 'fondo' or self.buffer.lower() == 'valores' 
            or self.buffer.lower() == 'evento'): 
                self.agregar_Token(self.buffer,self.fila,self.columna,'reservada_' + self.buffer)
                self.estado = 0
                self.i -= 1
            elif self.buffer in ['entrada', 'info']:
                self.agregar_Token(self.buffer,self.fila,self.columna,'evento_' + self.buffer)
                self.estado = 0
                self.i -= 1


    def s2(self):
        '''Estado 2'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Virgulilla')
        self.estado = 0
        self.i -= 1
    
    def s3(self):
        '''Estado 3'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo Abre corchete')
        self.estado = 0
        self.i -= 1
    
    def s4(self):
        '''Estado 4'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo Cierra corchete')
        self.estado = 0
        self.i -= 1
    
    def s5(self):
        '''Estado 5'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo de Comillas')
        self.estado = 0
        self.i -= 1
        if self.flag_comillas:
            self.flag_comillas = False
        else:
            self.flag_comillas = True
    
    def s6(self):
        '''Estado 6'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo Comillas Simple')
        self.estado = 0
        self.i -= 1
        if self.flag_comillas:
            self.flag_comillas = False
        else:
            self.flag_comillas = True
    
    def s7(self,caracter):
        '''Estado 7 - cadenas'''
        if caracter.isalpha():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter in ['+','!','*','@',' ','-',':',';','#','%','^','&','?',',','.','|']:
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_Token(self.buffer,self.fila,self.columna,'Cadena X')
            self.estado = 0
            self.i -= 1

    def s8(self):
        '''Estado 8'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo Menor Q')
        self.estado = 0
        self.i -= 1
    
    def s9(self):
        '''Estado 9'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo Mayor Q')
        self.estado = 0
        self.i -= 1
    
    def s10(self):
        '''Estado 10'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo de dos puntos')
        self.estado = 0
        self.i -= 1
    
    def s11(self):
        '''Estado 11'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo coma')
        self.estado = 0
        self.i -= 1

    def s12(self):
        '''Estado 12'''
        self.agregar_Token(self.buffer,self.fila,self.columna,'Signo coma')
        self.estado = 0
        self.i -= 1
        
        # self.agregar_Token
    def analizar(self,cadena):
        '''Realiza los cambios de estados'''
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
        x.field_names = ["Lexema","fila","Columna","Tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema,token.fila,token.columna,token.tipo])
        print(x)
    
    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripción","fila","Columna"]
        for error in self.listaErrores:
            x.add_row([error.descripcion,error.fila,error.columna])
        print(x)
    
    def crearTTokens(self):
        texto = ''
        f = open('./ReporteTokens.html','w')
        texto += '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Reporte Tokens</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We"
            crossorigin="anonymous"
            />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
        </head>
        <body style="background-color: rgb(243, 240, 235);">
        <div class="container">
        <br>
        <h2 class="text-center" style="font-weight: bold; color: rgb(36, 36, 179);">Tabla de Tokens</h2>
        <br>
        <h6 style="font-weight:600 ;">A continuacion se presentan tabla de tokens encontrados en el lenguaje:</h6>
        <table class="table table-hover">
            <thead class="thead-dark">
        <tr>
        <th class="text-center">LEXEMA</th>
        <th class="text-center">FILA</th>
        <th class="text-center">COLUMNA</th>
        <th class="text-center">TIPO</th>
        </tr>
        </thead>
        <tbody>'''
        for token in self.listaTokens:
            texto +='''
        <tr>
            <td class="text-center">'''+token.lexema+'''</td>
            <td class="text-center">'''+str(token.fila)+'''</td>
            <td class="text-center">'''+str(token.columna)+'''</td>
            <td class="text-center">'''+token.tipo+'''</td>
        </tr>   '''
        texto +='''
        </tbody>
        </table>
        <br>
                    
        </body>
        <hr>
        <footer>
            <h5 style="text-align: right; font-weight: bolder;">Josue Gramajo - 202000895</h5>
            <h6 style="text-align: right; font-weight: bold;">Reporte generado:'''+time.ctime()+'''</h6>
        </footer>
        </html>
        '''
        mensaje = texto 
        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('ReporteTokens.html')

    def crearTErrores(self):
        texto = ''
        f = open('./ReporteErrores.html','w')
        texto += '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Reporte Tokens</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We"
            crossorigin="anonymous"
            />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
        </head>
        <body style="background-color: rgb(243, 240, 235);">
        <div class="container">
        <br>
        <h2 class="text-center" style="font-weight: bold; color: rgb(36, 36, 179);">Tabla de Errores</h2>
        <br>
        <h6 style="font-weight:600 ;">A continuacion se presentan tabla de errores encontrados en el lenguaje:</h6>
        <table class="table table-hover">
            <thead class="thead-dark">
        <tr>
        <th class="text-center">Descripcion</th>
        <th class="text-center">fila</th>
        <th class="text-center">COLUMNA</th>
        </tr>
        </thead>
        <tbody>'''
        for error in self.listaErrores:
            texto +='''
        <!-- ASI SE CREA UNA FILA -->
        <tr>
            <td class="text-center">'''+error.descripcion+'''</td>
            <td class="text-center">'''+str(error.fila)+'''</td>
            <td class="text-center">'''+str(error.columna)+'''</td>
        </tr>   '''
        texto +='''
        </tbody>
        </table>
        <br>
                    
        </body>
        <hr>
        <footer>
            <h5 style="text-align: right; font-weight: bolder;">Josue Gramajo - 202000895</h5>
            <h6 style="text-align: right; font-weight: bold;">Reporte generado:'''+time.ctime()+'''</h6>
        </footer>
        </html>
        '''
        mensaje = texto 
        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('ReporteErrores.html')