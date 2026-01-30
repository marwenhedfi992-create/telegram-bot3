from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
import os

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 6484987137  # الإيدي متاعك

async def start(update, context):
    await update.message.reply_text(
        "👋 مرحبا!\n"
        "ابعثلي رسالة، صورة، صوت، أو موقع.\n"
        "وسيتم تحويلها للإدارة."
    )

async def forward_all(update, context):
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, forward_all))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
