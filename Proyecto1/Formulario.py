class Form:
    def __init__(self):
        self.boton = 0
        self.text = 0 
        self.radio = 0
        self.label = 0
        self.select = 0 
        self.getSelect = ''
        self.getElements = ''
        self.getRadio = ''

    def FormInicio():
        inicio =''
        inicio = ''' 
    !DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>FORM</title>
                <link rel="stylesheet" href="/archivos/Diseños.css">
            </head>
            
            <body class="Registro">
                    <div class="register">
                    <img class="avatar" src="/archivos/avatardef.png">
                    <h1 class="restar">FORM GENERADO</h1>
                    <form name="form">  '''
        return inicio

    def enviarEtiquetas(self,etiquetas):
        content =''

        for tag in etiquetas:
            if tag['tipo'] == 'etiqueta':     #Esto es para labels      
                for key in tag:
                    if key == 'valor':
                        content += '''
                        <!-- text  -->
                        <label for="'''+tag[key]+'''">'''+tag[key]+'''</label>
                        '''
                        print(tag[key])

                print('--------')

            elif tag['tipo'] == 'texto':      #Esto es para input-texto     
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
                    <input type="text" value="'''+value+'''"  id="'''+value+'''" placeholder="'''+fondo+'''" >
                    '''
                    print(content)
                    pass
                elif flag_fondo== False and flag_valor == True:
                    content+='''
                    <input type="text" value="'''+value+'''"  id="'''+value+'''" >
                    '''
                    print(content)
                    pass
                elif flag_valor== False and flag_fondo == True:
                    content+='''
                    <input type="text" placeholder="'''+fondo+'''"  id="'''+value+'''" >
                    '''
                    print(content)
                    pass
                else:
                    content+='''
                    <input type="text"  id="'''+value+''' >
                    '''
                    print(content)
                    pass

                print('--------')

            elif tag['tipo'] == 'grupo-radio': #Esto es para group-radio 
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
                            <input type="radio" id="'''+i+'''" name="fav_language" value="'''+i+'''">
                            <label style="color: rgb(146, 140, 140);" for="'''+i+'''">'''+i+'''</label>
                            '''
                            print(i)
                        content+='''</div>'''
                        content+='''<br>'''
                print('--------')
                
            elif tag['tipo'] == 'grupo-option': #Esto es para group-option
                print(tag)
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
                        content+='''
                        <!-- Select -->
                                <label for="'''+tag[key]+'''" >'''+tag[key]+'''</label>
                                <select  id="'''+tag[key]+'''" >
                        '''
                    elif key == 'valores':
                        for i in tag[key]:
                            print(i)
                            content+='''
                            <option value="'''+i+'''">'''+i+'''</option>

                            '''
                print('--------')

            elif tag['tipo'] == 'boton': #Esto es para el boton
                print(tag)
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
                        value = tag[key]
                    elif key == 'evento':
                        print(tag[key])
                        evento = ''
                        evento = tag[key]
                content+='''
                    <input type="button" onclick="registrar()" value="'''+value+'''">
                        </form>
                    </div>
                '''
        print(content)
    def allEtiquetas(self,tokens):
        etiquetas = []
        for i in range(len(tokens)):
            componente = {}
            if tokens[i].tipo == 'reservada_tipo' and (tokens[i + 3].lexema == 'etiqueta' or tokens[i + 3].lexema == 'label'):
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                etiquetas.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'texto':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_fondo':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                etiquetas.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-radio':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_valores':
                        grupo_radio = []
                        for h in range(x,len(tokens)):
                            if tokens[h].lexema == ']':
                                break
                            if tokens[h].tipo == 'Cadena X':
                                grupo_radio.append(tokens[h].lexema)
                        componente[tokens[x].lexema] = grupo_radio
                etiquetas.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-option':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_valores':
                        grupo_option = []
                        for h in range(x,len(tokens)):
                            if tokens[h].lexema == ']':
                                break
                            if tokens[h].tipo == 'Cadena X':
                                grupo_option.append(tokens[h].lexema)
                        componente[tokens[x].lexema] = grupo_option
                etiquetas.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'boton':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_evento':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                etiquetas.append(componente)
        return etiquetas 