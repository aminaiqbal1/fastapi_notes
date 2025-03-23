from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/login_info")
async def login_info():
    try:
        return {"name ": "amina iqbal",
                "gmail_id": "amminaiqball@gmail.com",
                "password": "a544121i.",
                "age": "25",
                "login": "success"}
    except Exception as e:
        return {"this error in your code ": str(e)}
    # uvicorn main:app, host 0.0.0.0, port 9000, workers 4
# path parameter  s mn hum ak limited value pass krty hain jesy name, id, etc
# Conclusion:
# Use Path Parameters → Jab unique resource ko access karna ho (e.g., user ID, product ID).
# Use Query Parameters → Jab optional values ya filtering karni ho.
# Kab Use Karna Chahiye?
# Path parameters tab use kiye jate hain jab resource (data) ka unique identifier URL ka hissa ho.
# Agar aap kisi specific item ya user ka data lena chahte hain, to path parameters best choice hain.
# Best Practice: Path parameters sirf tab use karein jab required aur unique identifier ho!
# Jab multiple values pass karni ho
# Path parameters sirf ek value handle kar sakte hain.
# ✅ Query parameters multiple values ke liye best hain:
@app.get("/login_info/{name}/{gmail_id}/{password}/{age}/{login}")
async def login_info(name,gmail_id,password,age, login):
    try:
        return {"name ": name,
                "gmail_id": gmail_id,
                "password": password,
                "age":age,
                "login": login}
    except Exception as e:
        return {"this error in your code ": str(e)}
    


# Query parameters are additional kev-value pairs in the URL. usually after the ?
@app.get("/items/")
async def get_items(category: str = None, price: int = 100):
    return {"category": category, "price": price}
# 4. Query Parameters mn raout ka under kuch ni ata or function mn sb kuch define hota ha
@app.get("/info/")
def info(name : str, age : int, email : str):
    return {"name": name, "age": age, "email": email}
@app.get("/sinup/")
def sinup(name : str, age : int, email : str, qualification : int):
    return {"name": name, "age": age, "email": email , "qualification": qualification}
# 5. Request Bodies this  mthode use for private data like dabit card number, password etc
# FastAPI allows handling JSON data in request bodies, using Pydantic models for validation and type-checking.
from pydantic import BaseModel
# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None
# @app.post("/items/")
# async def create_item(item: Item):
#     try:
#         # return {"item_name" : item.name,"item_description" : item.description, "item_price": item.price}
#         return{ "data" :item}
#     except Exception as e:
#         return {"massage" : e}
# s mn hum path, query and body parameter ko use kr rhy hain 
# Hum POST Method Q Use Kar Rahe Hain aur GET Q Nahi?
# ✅ POST Method Use Karne Ki Wajah:
# Data Send Karne Ke Liye → POST method client se server tak new data bhejne ke liye use hota hai (e.g., database me naye records create karne ke liye).

# Request Body Support → POST request body parameters accept karti hai, jo JSON ya complex objects bhejne ke liye zaroori hai.

# Sensitive Data Handling → POST requests data URL me show nahi karti (secure hoti hai).

# ❌ GET Method Q Nahi Use Kar Rahe?
# GET sirf data retrieve karne ke liye hoti hai, usme request body nahi hoti.

# GET URL me parameters bhejti hai, jo large ya sensitive data ke liye sahi nahi hota.
# CRUD maen create read uppdate and dilate  yr hr rount ka lia use hota hai example login ka ak crud banta hai crud opration applay krna khaty hain
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
@app.post("/items/{id}")
async def create_item(id : int,  item: Item,gmail: Optional[str]=None):
    try:
        # return {"item_name" : item.name,"item_description" : item.description, "item_price": item.price}
        return{ "data" :item,
               "id" : id,
               "gmail": gmail}
    except Exception as e:
        return {"massage" : e}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


