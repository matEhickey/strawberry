from __future__ import annotations

from typing import List, Optional
import strawberry
import db

class Datas:
    def getDatas(key):
        if(key == "books"):
            return db.Book.select()
        if(key == "authors"):
            return db.Author.select()

    
def get_books(id=None, author=None) -> List[Book]:
    if author: 
        datas = author.books
    else:
        datas = Datas.getDatas("books")
        
    if id:
        datas = datas.where(db.Book.id == id)
        
    return list(datas)
    
def get_authors(id: Optional[int] = None) -> List[Author]:
    datas = Datas.getDatas("authors")
    
    if id:
        datas = datas.where(db.Author.id == id)
    
    return list(datas)
        
@strawberry.type
class Book:
    id: int
    title: str
    author_id: int
    
    @strawberry.field
    def author(self, info) -> Author:
        return get_authors(id=self.author_id)[0]
    
@strawberry.type
class Author:
    id: int
    name: str
    
    @strawberry.field
    def books(self, info, id: Optional[int] = None) -> List[Book]:
        # import pdb; pdb.set_trace()
        return get_books(id=id, author=self)

@strawberry.type
class Query:
    @strawberry.field
    def books(self, info) -> List[Book]:
        return get_books()
        
    @strawberry.field
    def book(self, info, id: int) -> Book:
        return get_books(id)[0]
    
    @strawberry.field
    def authors(self, info) -> List[Author]:
        return get_authors()
        
    @strawberry.field
    def author(self, info, id: int) -> Author:
        return get_authors(author_id=id)[0]
    
    @strawberry.field
    def name(self, optional_argument: Optional[str] = None) -> str:
        return "Name"

if __name__ == "app":
    db.connect()
    db.create_db()
    db.fill_db()
    schema = strawberry.Schema(query=Query)
    
    # db.close()
