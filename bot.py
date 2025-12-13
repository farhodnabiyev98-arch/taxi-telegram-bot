import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚕 Taxi botga xush kelibsiz!\n\n"
        "🚗 Qayerdan → Qayerga\n"
        "🕒 Vaqt\n"
        "📞 Telefon\n\n"
        "Shu formatda yozing."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        "✅ Buyurtma qabul qilindi!\n\n"
        f"📌 Buyurtma:\n{text}\n\n"
        "Haydovchilar ko‘radi."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
