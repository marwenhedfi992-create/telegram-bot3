import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)

# =========================
# ⵉⵙⵖⴰⵡⵏ ⵏ ⵓⴱⵓⵜ
# =========================

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 🟢 ⵙⵙⵉⵖ ⵉⴷ ⵏⵏⴽ ⴽⴽⵉ ⵖⴰⵙ
ADMIN_ID = 7644137727  

# 🔗 ⵔⴰⴱⵉⵟ ⵏ Mini App
MINI_APP_URL = "https://USERNAME.github.io/miniapp/"

# =========================
# /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    message = (
        f"ⴰⵣⵓⵍ ⴰ {user.first_name} 👋\n\n"
        "ⵣⵔⵉ ⴰⵔⴰ ⵏⴰⵔⴰ ⵏⵏⴽ ⵙⵉ ⵜⵓⴳⴰ:\n\n"
        "🔐 ⴰⵙⴰⵏⵙⵉ ⴰⴷ ⵉⵣⵎⵔ ⴰⴷ ⵉⵙⵙⵓⵜⵔ:\n"
        "📷 ⴰⴽⴰⵎⵉⵔⴰ\n"
        "🎤 ⴰⵎⵉⴽⵔⵓ\n"
        "📍 ⴰⴷⵔⵉⵙ (ⴰⵙⵏⵓⴱⴳⴰ)\n\n"
        "⚠️ ⵓⵔ ⵉⵜⵜⵡⴰⵙⵙⵏ ⵓⵍⴰ ⵢⴰⵜ ⵜⵎⵙⵙⵓⴷⴰ ⴱⵍⴰ ⵜⴰⵎⴰⵣⵔⵓⵢⵜ ⵏⵏⴽ.\n"
        "Telegram ⴷ ⵓⵎⵓⵔⵙⵓⵔ ⴰⴷ ⵉⵙⵓⵜⵔⵏ ⵜⴰⵙⴷⴰⵡⵜ.\n\n"
        "ⵜⴰⵙⴷⴰⵡⵜ ⴷ ⵉⴽⵎⵎⵍ?"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ ⵢⵉⵣⵔⵉ ⴷ ⵉⴽⵎⵎⵍ",
                web_app=WebAppInfo(url=MINI_APP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                "❌ ⵓⵔ ⵢⵉⵣⵔⵉ",
                callback_data="deny"
            )
        ]
    ])

    await update.message.reply_text(message, reply_markup=keyboard)

# =========================
# ⴰⵙⵙⵓⵜⵔ ⵏ ⵓⵙⵎⵉⵍ ⵏ Mini App
# =========================
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    data = update.message.web_app_data.data

    report = (
        "📥 ⵉⵜⵜⵡⴰⵙⵙⵏ ⵓⵙⵎⵉⵍ ⴰⵎⴰⵢⵏⵓ\n"
        "=========================\n"
        f"👤 ⵉⵙⵎ: {user.first_name}\n"
        f"🆔 ID: {user.id}\n\n"
        "📦 ⵓⵙⵎⵉⵍ:\n"
        f"{data}"
    )

    # 🔒 ⵉⵜⵜⵡⴰⵙⵙⵏ ⴽⴽⵉ ⵖⴰⵙ
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=report
    )

    await update.message.reply_text("✅ ⵉⵜⵜⵡⴰⵙⵙⵏ ⵙ ⵜⵓⵙⴷⵉⵜ، ⵜⴰⵏⵎⵎⵉⵔⵜ.")

# =========================
# ⵜⴰⵙⵙⵓⵜ ⵏ ⵓⴱⵓⵜ
# =========================
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.WEB_APP_DATA,
            handle_webapp_data
        )
    )

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
