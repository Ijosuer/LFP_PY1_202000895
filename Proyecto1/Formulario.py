class Componentes:
    def getComponentes(self,tokens):
        componentes = []
        for i in range(len(tokens)):
            componente = {}
            if tokens[i].tipo == 'reservada_tipo' and (tokens[i + 3].lexema == 'etiqueta' or tokens[i + 3].lexema == 'label'):
                print(tokens[i].tipo,tokens[i].columna,tokens[i].lexema ,'|', tokens[i+3].tipo,tokens[i+3].columna,tokens[i+3].lexema)
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                componentes.append(componente)
            else:
                print('ERROR EN LA ENTRADA', tokens[i].tipo)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'texto':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_fondo':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                componentes.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-radio':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_valores':
                        gruporadio = []
                        for h in range(x,len(tokens)):
                            if tokens[h].lexema == ']':
                                break
                            if tokens[h].tipo == 'valor':
                                gruporadio.append(tokens[h].lexema)
                        componente[tokens[x].lexema] = gruporadio
                componentes.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-option':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_valores':
                        grupooption = []
                        for h in range(x,len(tokens)):
                            if tokens[h].lexema == ']':
                                break
                            if tokens[h].tipo == 'valor':
                                grupooption.append(tokens[h].lexema)
                        componente[tokens[x].lexema] = grupooption
                componentes.append(componente)

            if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'boton':
                componente[tokens[i].lexema] = tokens[i + 3].lexema
                for x in range(i,len(tokens)):
                    if tokens[x].lexema == '>':
                        break
                    if tokens[x].tipo == 'reservada_valor':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                    if tokens[x].tipo == 'reservada_evento':
                        componente[tokens[x].lexema] = tokens[x + 3].lexema
                componentes.append(componente)
        return componentes 