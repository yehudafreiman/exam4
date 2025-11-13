from fastapi import FastAPI
from pydantic import BaseModel
import json
import ciphers
import uvicorn

class Request(BaseModel):
    text: str
    offset: int | None
    mode: str | None  #"encrypt" or "decrypt"

api = FastAPI()

# home page
@api.get("/")
def index():
    return {"msg":"Welcome to the hottest place in hell"}

# show msg
@api.get("/test")
def testing():
    return {"msg":"Hi from test"}

# save path parameter in file
@api.get("/test/{name}")
def save_name(name:str):
    with open("names.txt", "a") as f:
        f.write(name)
    return {"msg":"Saved user"}

# encryption and decryption in caesar cipher
@api.post("/caesar")
def caesar_cipher(request:Request):
    if request.mode == "encrypt":
        # Use a helper method from cipher.py
        encrypted_text = ciphers.encode_ceaser(decode=request.text, offset=request.offset)
        return {"encrypted_text": encrypted_text}
    else:
        # Use a helper method from cipher.py
        decrypted_text = ciphers.decode_ceaser(encode=request.text, offset=request.offset)
        return {"decrypted_text":decrypted_text}

# encryption in fence cipher
@api.get("/fence/encrypt")
def fence_cipher_encryption(text:str):
    # Use a helper method from cipher.py
    encrypted_text = ciphers.encode_fence(text)
    return {"encrypted_text": encrypted_text}

# decryption in fence cipher
@api.post("/fence/decrypt")
def fence_cipher_decryption(request:Request):
    # Use a helper method from cipher.py
    decrypted_text = ciphers.decode_fence(encode=request.text)
    return {"decrypted_text": decrypted_text}


if __name__ == "__main__":
    uvicorn.run(api, host="localhost", port=8000)




