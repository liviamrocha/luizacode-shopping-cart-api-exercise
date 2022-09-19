from fastapi import FastAPI
from shopping_cart.routers import adress, cart, product, user

app = FastAPI()

app.include_router(adress.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(cart.router)

@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')