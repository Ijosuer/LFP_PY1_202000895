import webbrowser

class Form:
    def __init__(self,tokens):
        self.tokens = tokens
        self.etiquetas = None

    def FormInicio(self,cadena):
        inicio =''
        salto = r'"\n"'
        inicio = ''' 
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>FORM</title>
                <link rel="stylesheet" href="archivos/Diseños.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
                    <script>
                    function info(){

                        
                        $(document).ready(function() {
                            $("#data").click(function(){
                                $('#serializearray').text(
                                        array = ($('form').serializeArray())

                                        );
                                        console.log(array)
                                        var cadena = ""
                                        for (let step = 0; step < array.length; step++) {
                                            cadena = cadena + array[step].value + '''+salto+'''
                                            // document.querySelector('#results').innerText = cadena;
                            localStorage.setItem('eslainfo',cadena)
                                        }})})
                            }
                    </script>
                    <script>
                    function entrada(){
                        cadena = '''+'`'+cadena+'`'+'''
                        localStorage.setItem('text',cadena)
                    }
                    </script>

            </head>
            
            <body class="Registro">
                    <div class="register">
                    <img class="avatar" src="archivos/avatardef.png">
                    <h1 class="restar">FORM GENERADO</h1>
                    <form name="form">  '''
        return inicio
    
    def Label(self):
        content =''

        for tag in self.etiquetas:
            if tag['tipo'] == 'etiqueta':     #Esto es para labels      
                for key in tag:
                    if key == 'valor':
                        content += '''
                        <!-- text  -->
                        <label for="'''+tag[key]+'''">'''+tag[key]+'''</label>
                        '''
                        print(tag[key])
        return content

    def Input(self):
        content =''

        for tag in self.etiquetas:
            if tag['tipo'] == 'texto':      #Esto es para input-texto     
                flag_valor = False
                flag_fondo = False
                value = ''
                fondo = ''
                for key in tag:
                    if key == 'valor':
                        value = tag[key]
                        flag_valor = True
                    elif key == 'fondo':
                        fondo = tag[key]
                        flag_fondo = True
                        # print(valor , tag[key], 'AKI ESTAAAA')
                    
                if flag_valor == True and flag_fondo == True:
                    content+='''
                    <input type="text" value="'''+value+'''"  name="'''+value+'''" placeholder="'''+fondo+'''" >
                    '''
                    print(content)
                    pass
                elif flag_fondo== False and flag_valor == True:
                    content+='''
                    <input type="text" value="'''+value+'''"  name="'''+value+'''" >
                    '''
                    print(content)
                    pass
                elif flag_valor== False and flag_fondo == True:
                    content+='''
                    <input type="text" placeholder="'''+fondo+'''"  name="'''+value+'''" >
                    '''
                    print(content)
                    pass
                else:
                    content+='''
                    <input type="text"  name="'''+value+''' >
                    '''
                    print(content)
                    pass
        return content

    def group_radio(self):
        content = ''
        for tag in self.etiquetas:
            if tag['tipo'] == 'grupo-radio': #Esto es para group-radio 
                print(tag)
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
                        content+='''
                        <!-- Radio  -->
                        <div class="divR">
                            <label  for="'''+tag[key]+'''">'''+tag[key]+'''</label>
                                '''
                    elif key == 'valores':
                        for i in tag[key]:
                            content+='''
                            <input type="radio" name="'''+i+'''" value="'''+i+'''">
                            <label style="color: rgb(146, 140, 140);" for="'''+i+'''">'''+i+'''</label>
                            '''
                            print(i)
                        content+='''</div>'''
                        content+='''<br>'''
        return content

    def group_option(self):
        content = ''
        for tag in self.etiquetas:
            if tag['tipo'] == 'grupo-option': #Esto es para group-option
                print(tag)
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
                        content+='''
                        <!-- Select -->
                                <label for="'''+tag[key]+'''" >'''+tag[key]+'''</label>
                                <select  name="'''+tag[key]+'''" >
                        '''
                    elif key == 'valores':
                        for i in tag[key]:
                            print(i)
                            content+='''
                            <option value="'''+i+'''">'''+i+'''</option>
                    
                            '''
                print('--------')
        return content 
    
    def boton(self):
        content = ''
        for tag in self.etiquetas:
            if tag['tipo'] == 'boton': #Esto es para el boton
                print(tag)
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
                        value = tag[key]
                    elif key == 'evento':
                        print(tag[key])
                        evento = ''
                        evento = tag[key]
                        if evento == 'info':
                            content+='''
                                </select>
                                <input type="button" id='data' onclick="info()" value="'''+value+'''">
                                    </form>
                                </div>''' 
                        elif evento == 'entrada':
                            content+='''
                                </select>
                                <input type="button" id='data' onclick="entrada()" value="'''+value+'''">
                                    </form>
                                </div>
                            ''' 
        return content
    
    def allEtiquetas(self):
        etiquetas = []
        for i in range(len(self.tokens)):
            componente = {}
            if self.tokens[i].tipo == 'reservada_tipo' and (self.tokens[i + 3].lexema == 'etiqueta' or self.tokens[i + 3].lexema == 'label'):
                componente[self.tokens[i].lexema] = self.tokens[i + 3].lexema
                for x in range(i,len(self.tokens)):
                    if self.tokens[x].lexema == '>':
                        break
                    if self.tokens[x].tipo == 'reservada_valor':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                etiquetas.append(componente)

            if self.tokens[i].tipo == 'reservada_tipo' and self.tokens[i + 3].lexema == 'texto':
                componente[self.tokens[i].lexema] = self.tokens[i + 3].lexema
                for x in range(i,len(self.tokens)):
                    if self.tokens[x].lexema == '>':
                        break
                    if self.tokens[x].tipo == 'reservada_valor':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                    if self.tokens[x].tipo == 'reservada_fondo':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                etiquetas.append(componente)

            if self.tokens[i].tipo == 'reservada_tipo' and self.tokens[i + 3].lexema == 'grupo-radio':
                componente[self.tokens[i].lexema] = self.tokens[i + 3].lexema
                for x in range(i,len(self.tokens)):
                    if self.tokens[x].lexema == '>':
                        break
                    if self.tokens[x].tipo == 'reservada_valor':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                    if self.tokens[x].tipo == 'reservada_valores':
                        grupo_radio = []
                        for h in range(x,len(self.tokens)):
                            if self.tokens[h].lexema == ']':
                                break
                            if self.tokens[h].tipo == 'Cadena X':
                                grupo_radio.append(self.tokens[h].lexema)
                        componente[self.tokens[x].lexema] = grupo_radio
                etiquetas.append(componente)

            if self.tokens[i].tipo == 'reservada_tipo' and self.tokens[i + 3].lexema == 'grupo-option':
                componente[self.tokens[i].lexema] = self.tokens[i + 3].lexema
                for x in range(i,len(self.tokens)):
                    if self.tokens[x].lexema == '>':
                        break
                    if self.tokens[x].tipo == 'reservada_valor':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                    if self.tokens[x].tipo == 'reservada_valores':
                        grupo_option = []
                        for h in range(x,len(self.tokens)):
                            if self.tokens[h].lexema == ']':
                                break
                            if self.tokens[h].tipo == 'Cadena X':
                                grupo_option.append(self.tokens[h].lexema)
                        componente[self.tokens[x].lexema] = grupo_option
                etiquetas.append(componente)

            if self.tokens[i].tipo == 'reservada_tipo' and self.tokens[i + 3].lexema == 'boton':
                componente[self.tokens[i].lexema] = self.tokens[i + 3].lexema
                for x in range(i,len(self.tokens)):
                    if self.tokens[x].lexema == '>':
                        break
                    if self.tokens[x].tipo == 'reservada_valor':
                        componente[self.tokens[x].lexema] = self.tokens[x + 3].lexema
                    if self.tokens[x].tipo == 'reservada_evento':
                        componente[self.tokens[x].lexema] = self.tokens[x + 2].lexema
                etiquetas.append(componente)
        self.etiquetas = etiquetas
    
    def doForm(self,cadena):
        text = ''
        text = self.FormInicio(cadena)
        text += self.Label()
        text += self.Input()
        text += self.group_radio()
        text += self.group_option()
        text += self.boton()

        text+= '''  
                    <div id="results">
                        <iframe name=miframeflotante src="archivos/iframe.html" width=200 height=200 frameborder="1" scrolling=1 marginwidth=2 marginheight=4 align=left> </iframe>
                    </div>
                    </body>
                    </html>
        '''
        print(text)
        form = open('./Formulario.html','w')
        form.write(text)
        form.close()
        webbrowser.open_new_tab('./Formulario.html')