import strawberry


@strawberry.type
class User:
    name: str
    age: int
    # id: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info) -> User:
        return User(
            name="Patrick", 
            age=100,
            # id=1
        )


schema = strawberry.Schema(query=Query)
