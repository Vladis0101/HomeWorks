from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    id: int
    name: str
    age: int
    interests: Optional[List[str]] = None
    salary: float

class UserList(BaseModel):
    id: int
    name: str

class UserDetail(BaseModel):
    id: int
    name: str
    age: int
    interests: Optional[List[str]] = None
    salary: float

import json
from typing import List, Optional

data_file = 'some_file.json'


def add_user_to_file(user: UserCreate):
    try:
        with open(data_file, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    users.append(user.dict())

    with open(data_file, 'w') as f:
        json.dump(users, f, indent=4)

def get_all_users() -> List[UserList]:
    try:
        with open(data_file, 'r') as f:
            users = json.load(f)
        return [UserList(**user) for user in users]
    except FileNotFoundError:
        return []

def get_user_by_id(user_id: int) -> Optional[UserDetail]:
    try:
        with open(data_file, 'r') as f:
            users = json.load(f)
        for user in users:
            if user['id'] == user_id:
                return UserDetail(**user)
    except FileNotFoundError:
        return None


new_user = UserCreate(id=6, name="Vova", age=30, interests=["streams"], salary=6000.0)
add_user_to_file(new_user)

all_users = get_all_users()
print(all_users)

user = get_user_by_id(6)
print(user)
