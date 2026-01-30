import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# بدّل هذا بالـ Telegram ID متاعك
ADMIN_ID = 6484987137  # مثال

MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📸 ابعث صورة")],
        [KeyboardButton("🎤 ابعث تسجيل صوتي")],
        [KeyboardButton("📍 ابعث موقعك", request_location=True)],
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبا 👋\n"
        "اختر شنوّة تحب تبعث:\n"
        "📸 صورة\n🎤 صوت\n📍 موقع",
        reply_markup=MENU
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    caption = f"📸 صورة من: {update.message.from_user.full_name}"
    await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo.file_id, caption=caption)
    await update.message.reply_text("تمّ إرسال الصورة ✅")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    caption = f"🎤 تسجيل صوتي من: {update.message.from_user.full_name}"
    await context.bot.send_voice(chat_id=ADMIN_ID, voice=voice.file_id, caption=caption)
    await update.message.reply_text("تمّ إرسال الصوت ✅")

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loc = update.message.location
    text = (
        "📍 موقع جديد\n"
        f"من: {update.message.from_user.full_name}\n"
        f"Latitude: {loc.latitude}\n"
        f"Longitude: {loc.longitude}"
    )
    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("تمّ إرسال الموقع ✅")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
