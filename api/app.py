import dotenv
from fastapi import FastAPI
from api.controller import client_router, dish_router, order_router, restaurant_router, order_router, menu_router

dotenv.load_dotenv(override=True)


app = FastAPI()

'''ici on inclut les routers définis dans le controller de notre application API'''
app.include_router(restaurant_router.router)
app.include_router(client_router.router)
app.include_router(order_router.router)
app.include_router(menu_router.router)
app.include_router(dish_router.router)
