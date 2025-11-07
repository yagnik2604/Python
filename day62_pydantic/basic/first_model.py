from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':  101, 'name':"yagnik", 'is_active': True}

user = User(**input_data)
print(user)



# import BaseModel
# type annotations 
# model init(always unpack the dictionary)
# automatic validation