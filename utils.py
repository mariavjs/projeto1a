import os
import json
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
    path = "templates/{template}".format(template=template)
    with open(path, "r") as arquivo:
        conteudo = arquivo.read()

    return conteudo


def add_note(nova_note):

    file_path = os.path.join(os.path.dirname(__file__), 'data', 'notes.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        note = json.load(file)
    note.append(nova_note)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(note, file, indent=4)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == "":
        resposta = "HTTP/1.1 {code} {reason}\n\n{body}" .format(code=code, reason=reason, headers=headers, body=body)

    else:
        resposta = "HTTP/1.1 {code} {reason}\n{headers}\n\n{body}" .format(code=code, reason=reason, headers=headers, body=body)

    return resposta.encode()
    
