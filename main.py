from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import ciphers
import uvicorn

api = FastAPI()

@api.get("/")
def index():
    return {"msg":"Welcome to the hottest place in hell"}

@api.get("/test")
def testing():
    return {"msg":"Hi from test"}

@api.get("/test/{name}")
def save_name(name:str):
    with open("names.txt", "a") as f:
        f.write(name)
    return {"msg":"Saved user"}


@api.post("/caesar")
def caesar_cipher(offset):
    body = {"text": str,
           "offset": int,
           "mode": "encrypt" or "decrypt"
    }
    return {"encrypted_text":""} or {"decrypted_text":""}

@api.get("/fence/encrypt?text={text}")
def fence_cipher_encryption():
    return {"encrypted_text":""}

@api.post("/fence/decrypt")
def fence_cipher_decryption():
    body = {"text":str
    }
    return {"decrypted":""}




