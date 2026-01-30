
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            KeyboardButton(
                "🌐 Mini App",
                web_app=WebAppInfo(
                    url="https://marwenhedfi992-create.github.io/miniapp/"
                )
            )
        ]
    ]

    await update.message.reply_text(
        "ⴰⵣⵓⵍ 👋\n"
        "ⴰⴷ ⵜⵙⵙⵉⵔ ⵉ Mini App ⵏⴽ",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
