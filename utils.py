def extract_route(request):
    barra = request.find("/")
    http = request.find("HTTP")

    route = request[barra+1:http-1]

    return route

def read_file(path):
    with open(path, "rb") as arquivo:
        texto = arquivo.read()

    
    return texto

import json

def load_data(arq):
    path = "data/{nome}".format(nome=arq)
    with open(path, "r") as arquivo:

        dict = json.load(arquivo)

    return dict


def load_template(template):
    path = "docs/{template}".format(template=template)
    with open(path, "r") as arquivo:

        conteudo = arquivo.read()

    return conteudo

def build_response(body='', code=200, reason='OK', headers=''):
    resposta = "HTTP/1.1 {code} {reason}\n{headers}\n\n{body}" .format(code=code, reason=reason, headers=headers, body=body)
    return resposta.encode()