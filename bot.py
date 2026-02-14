import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from database import add_user
from keyboards import main_menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    add_user(message.from_user.id, message.from_user.username)

    text = f"""
👋 سلام {message.from_user.first_name}

به ربات سرمایه‌یار خوش اومدی 📊

اینجا میتونی:
✔ قیمت لحظه‌ای بگیری
✔ هشدار قیمت تنظیم کنی
✔ تحلیل بازار ببینی
✔ حساب VIP فعال کنی

یکی از گزینه‌ها رو انتخاب کن 👇
"""

    await message.answer(text, reply_markup=main_menu())


@dp.callback_query_handler()
async def callbacks(callback: types.CallbackQuery):

    if callback.data == "prices":
        await callback.message.answer("📊 بزودی اتصال به قیمت لحظه‌ای فعال میشه...")
    
    elif callback.data == "alert":
        await callback.message.answer("🔔 بزودی امکان تنظیم هشدار قیمت فعال میشه...")
    
    elif callback.data == "analysis":
        await callback.message.answer("📈 تحلیل امروز بازار بزودی اضافه میشه...")
    
    elif callback.data == "vip":
        await callback.message.answer("⭐ بخش VIP بزودی فعال میشه...")
    
    elif callback.data == "account":
        await callback.message.answer("👤 اطلاعات حساب شما بزودی نمایش داده میشه...")

    await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
