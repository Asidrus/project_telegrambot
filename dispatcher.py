import aiohttp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from config import *
from order import order, OrderStatus


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")


@dp.message_handler(commands="help")
async def help(message: types.Message):
    # await dp.bot.send_message("936364717", "")
    await message.answer(f"/help - show all commands\n"
                         f"/took - took the order\n"
                         f"/gave - gave the order")


@dp.message_handler(commands=["took", "gave"])
async def change_status(message: types.Message):
    status = {"/took": OrderStatus.onTheWay, "/gave": OrderStatus.delivered}
    async with aiohttp.ClientSession() as session:
        async with session.post(WEBSITE_UPL+"/order/updateStatus",
                                data={"orderID": order.id, "status": status[message["text"]]}) as response:
            pass


if __name__ == "__main__":
    pass