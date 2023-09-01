import sqlite3

class Database:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.conn = sqlite3.connect('{nome}.db'.format(nome=self.nome))
        self.cur = self.conn.cursor()
        self.res = self.conn.execute('CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')
        

    def add(self, Note):
        id = Note.id
        title = Note.title
        content = Note.content
        self.conn.execute("INSERT INTO note (title, content) VALUES ('{title}', '{content}');".format(title=title, content=content))
        self.conn.commit()
        

    def get_all(self):
        notes = []
        cursor = self.conn.execute('SELECT id, title, content FROM note')
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            notes.append(Note(id, title, content))

        return notes
    
    def update(self, entry):
        id = entry.id
        title = entry.title
        content = entry.content
        cursor = self.conn.execute("UPDATE note SET title = '{title}', content = '{content}' WHERE id = {id}".format(title =title, content=content,id=id))
        self.conn.commit()

    def delete(self, note_id):
        cursor = self.conn.execute("DELETE FROM note WHERE id = '{id}'".format(id=note_id))
        self.conn.commit()



class Note:
    
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content