from __future__ import annotations

from typing import List, Optional
import strawberry

datas = None

class Datas:
    def getDatas(key):
        return datas[key]

    
def get_books(id=None, author_id=None) -> List[Book]:
    datas = Datas.getDatas("books")
    
    if author_id: 
        datas = filter(lambda x: x.author_id == author_id, datas)
    
    if id:
        datas = filter(lambda x: x.id == id, datas)
        
    return list(datas)
    
def get_authors(id: Optional[int] = None) -> List[Author]:
    datas = Datas.getDatas("authors")
    
    if id:
        datas = filter(lambda x: x.id == id, datas)
    
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
        return get_books(id=id, author_id=self.id)

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
    datas = {
        "books": [
            Book(id=1, title="L'etrange histoir", author_id=1),
            Book(id=2, title="Bleee", author_id=1),
            Book(id=3, title="Harry Potter 1", author_id=2),
            Book(id=4, title="Harry Potter 2", author_id=2),
            Book(id=5, title="Harry Potter 3", author_id=2),
            Book(id=6, title="Romeo and Juliet", author_id=3),
        ],
        "authors": [
            Author(id=1, name="Mr. Scott"),
            Author(id=2, name="JK Rowling"),
            Author(id=3, name="Shakspear"),
        ]
    }
    schema = strawberry.Schema(query=Query)
