from fastapi import FastAPI
from fastapi.openapi.models import Response

from typing import Union

from aiogram.utils import executor
from aiogram.utils.executor import Executor
from dispatcher import dp
from order import Order, order


app = FastAPI()

my_id = "936364717"


@app.on_event("startup")
async def on_startup():
    import asyncio
    loop = asyncio.get_event_loop()
    ex = Executor(dp, loop=loop)
    loop.create_task(ex.dispatcher.start_polling(reset_webhook=None, timeout=20, relax=.1, fast=True,
                                                 allowed_updates=None))
    app.dp = dp


@app.on_event("shutdown")
async def on_shutdown():
    pass


@app.post("/order")
async def new_order(_order: Order):
    order.__dict__ = _order.__dict__
    print(order)
    await dp.bot.send_message("936364717", f"Got a new order!\nNumber: {order.id}\nAddress: {order.address}\nPhone: {order.phone}")