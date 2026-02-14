from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("📊 قیمت لحظه‌ای", callback_data="prices"),
        InlineKeyboardButton("🔔 تنظیم هشدار", callback_data="alert"),
        InlineKeyboardButton("📈 تحلیل امروز", callback_data="analysis"),
        InlineKeyboardButton("⭐ ارتقا به VIP", callback_data="vip"),
        InlineKeyboardButton("👤 حساب من", callback_data="account"),
    )
    return keyboard
