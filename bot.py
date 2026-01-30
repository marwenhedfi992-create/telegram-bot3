import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6484987137


async def handle_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    header = (
        "📩 محتوى جديد من البوت:\n\n"
        f"👤 الاسم: {user.full_name}\n"
        f"🔗 اليوزر: @{user.username if user.username else 'ما عندوش'}\n"
        f"🆔 ID: {user.id}\n\n"
    )

    # 📝 نص
    if update.message.text:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=header + "📝 رسالة:\n" + update.message.text
        )

    # 📸 صورة
    if update.message.photo:
        photo = update.message.photo[-1]
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=photo.file_id,
            caption=header + "📸 صورة"
        )

    # 🎤 صوت
    if update.message.voice:
        await context.bot.send_voice(
            chat_id=ADMIN_ID,
            voice=update.message.voice.file_id,
            caption=header + "🎤 رسالة صوتية"
        )

    # 📍 موقع
    if update.message.location:
        loc = update.message.location
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=header + f"📍 الموقع:\nLatitude: {loc.latitude}\nLongitude: {loc.longitude}"
        )

    # رد آلي
    await update.message.reply_text(
        "✅ تم إرسال المحتوى.\nيمكنك إرسال نص، صورة، صوت أو موقع."
    )


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
