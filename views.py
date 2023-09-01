from utils import *
from urllib.parse import unquote_plus
import json
from database import *

db = Database("./data/banco")


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):

            chave, valor = chave_valor.split("=")
            params[unquote_plus(chave)] = unquote_plus(valor)
            
        titulo = params.get('titulo', '')
        descricao = params.get('detalhes', '')

        #add_note(novo)
        db.add(Note(title=titulo, content=descricao))

        return build_response(code=303, reason='See Other', headers='Location: /')

    
    note_template = load_template('components/note.html')

    notes_li = [
        note_template.format(title=dado.title, content=dado.content)
        for dado in db.get_all()
    ]

    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))


def delete(request, id_entry):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):

            chave, valor = chave_valor.split("=")
            params[unquote_plus(chave)] = unquote_plus(valor)
            
        titulo = params.get('titulo', '')
        descricao = params.get('detalhes', '')

        #add_note(novo)
        db.delete(id_entry)

        return build_response(code=303, reason='See Other', headers='Location: /')

    
    note_template = load_template('components/note.html')

    notes_li = [
        note_template.format(title=dado.title, content=dado.content)
        for dado in db.get_all()
    ]

    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))
