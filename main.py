from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Set

app = FastAPI()

#simple endpoint
@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/movies")
def getMovies():
    # This function will return a list of movies
    movies = [
        {"id": 1, "title": "The Shawshank Redemption", "year": 1994},
        {"id": 2, "title": "The Godfather", "year": 1972},
        {"id": 3, "title": "The Dark Knight", "year": 2008},
        {"id": 4, "title": "Pulp Fiction", "year": 1994},
        {"id": 5, "title": "Forrest Gump", "year": 1994}
    ]
    return movies

# if this was below then it would be considered as a path parameter and not a static path
@app.get('/user/admin')
def admin_profile():
    return "Hello, Mi Amor!"

#path parameter with type
@app.get("/user/{name}")
def user_profile(name: str):
    return f"Hello dear {name}! Say melon and enter!"

@app.get('/secretpath')
def secret_path():
    return "Ich bin Galadriel, ich komme aus Lothlorien. Ich brauche Kaffee mit Milch und Zucker. Ich spiele tennis. Wir sind sehr lustig. Danke, tschüss!"

# Query parameter
@app.get('/product')
def get_product(pname: str, price: float=None):
    return f"this is the product : {pname}, this is price : {price}"

""" Request body """
class Profile(BaseModel): #data model for request body
    name: str = Field(description="name of the user", min_length=3, max_length=50)
    age: int = Field(description="age of the user", gt=0, le=120)
    email: str
    status: str = 'pending' #default value
    tags: Set[str] = set() #python data type inside a model

@app.post('/profile/{id}')
def create_profile(id: int, profile: Profile, place: str = 'middle earth'):
    profile.status='success'
    #return {"message": f"Profile successfully created for {profile.name}, age {profile.age}, email {profile.email}, status {profile.status}"}
    return {"id": id, "profile": profile, "place": place}

