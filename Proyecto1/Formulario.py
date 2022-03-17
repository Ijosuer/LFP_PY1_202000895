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


    def enviarEtiquetas(self,etiquetas):

        for tag in etiquetas:
            if tag['tipo'] == 'etiqueta':     #Esto es para labels      
                for key in tag:
                    if key == 'valor':
                        print(tag[key])
            if tag['tipo'] == 'texto':      #Estp es para input-texto     
                print(tag)
            if tag['tipo'] == 'grupo-radio':           
                print(tag)
            if tag['tipo'] == 'grupo-option':           
                print(tag)
            if tag['tipo'] == 'boton':           
                print(tag)


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