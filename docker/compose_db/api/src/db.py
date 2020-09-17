from peewee import *
from datetime import date
from pprint import pprint as pp

db = SqliteDatabase(':memory:')

class BaseModel(Model):
    class Meta:
        database = db
        
class Author(BaseModel):
    name = CharField()
    
class Book(BaseModel):
    title = CharField()
    author = ForeignKeyField(Author, backref='books')
        

def connect():
    db.connect()
def close():
    db.close()
    
def create_db():
    db.create_tables([Author, Book])

def fill_db():
    bob = Author.create(name='Bob')
    jk = Author.create(name='jk')
    
    hp1 = Book.create(title="hp1", author=jk)
    hp2 = Book.create(title="hp2", author=jk)
    hp2 = Book.create(title="l'etrange histoire", author=bob)
    
if(__name__ == "__main__"):
    connect()
    create_db()
    fill_db()
    
    import pdb; pdb.set_trace()
    
    close()
