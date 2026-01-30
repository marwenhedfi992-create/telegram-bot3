from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 🔴 حط ID متاعك هنا
ADMIN_ID = 7644137727 

MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📷 صورة"), KeyboardButton("🎤 صوت")],
        [KeyboardButton("📍 موقعي", request_location=True)],
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبا 👋\n"
        "أي حاجة تبعثها توصل مباشرة للإدارة ✅",
        reply_markup=MENU
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 رسالة جديدة:\n{update.message.text}"
    )
    await update.message.reply_text("✔️ تم الاستلام")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption="📷 صورة جديدة"
    )
    await update.message.reply_text("✔️ تم إرسال الصورة")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    await context.bot.send_voice(
        chat_id=ADMIN_ID,
        voice=voice.file_id,
        caption="🎤 تسجيل صوتي"
    )
    await update.message.reply_text("✔️ تم إرسال الصوت")

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loc = update.message.location
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📍 موقع جديد:\nLatitude: {loc.latitude}\nLongitude: {loc.longitude}"
    )
    await update.message.reply_text("✔️ تم إرسال الموقع")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
