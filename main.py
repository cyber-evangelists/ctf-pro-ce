from fastapi import FastAPI, Body, Depends, HTTPException
from models.model import User, Ping, Cart
from hash_pass import hash_password
from database import check_user, execute_query
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from auth.auth_handler import decodeJWT
from services.pinger import ping_me
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(user: User):
    hashed_password = hash_password(user.password)
    response = check_user(user.username, hashed_password)
    if response:
        token = signJWT(user.username)
        return {"token": token}
    elif response == False:
        raise HTTPException(status_code=401, detail="invalid password")
    elif response == None:
        raise HTTPException(status_code=404, detail="user not found")
    
    
@app.post("/ping", dependencies=[Depends(JWTBearer())])
def ping(host: Ping):
    blocked_char = [" ", "|", "&", "||", ";", ";;"]
    for i in blocked_char:
        if i in host.host:
            if "&&" in host.host and i == "&":
                continue
            raise HTTPException(status_code=422, detail="!")
    response = ping_me(host.host)
    print(response)
    if response:
        return {"output": response}
    raise HTTPException(status_code=422, detail="invalid command")

@app.post("/cart")
def add_to_cart(cart: Cart):
    cart = cart.card_value.strip()
    if "*" in cart:
        return {"message": ""}
    if cart.isdigit():
        return {"message": f"{cart} added to database"}
    response = execute_query(cart)
    return {"message": response}
        

