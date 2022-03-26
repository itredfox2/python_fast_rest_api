#####################
# Imports           #
#####################

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#####################
# Globals           #
#####################

app = FastAPI()

#####################
# Classes           #
#####################

class Item(BaseModel):
    '''parse requests'''
    
    id: int
    name: str
    description: str
    price: int
    on_offer: bool
   
#####################
# Functions         #
#####################

@app.get('/')
def index():
    return  {
                'message': 'Hello World'
            }

@app.get('/greet/{name}')
def greet_name(name:str):
    return  {
                'greeting': f'Hello {name}'
            }

@app.get('/greet')
def greet_user_name(name:Optional[str] = 'user'):
    return  {
                'message': f'Hello {name}'
            }

@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
    return  {
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'on_offer': item.on_offer
            }
