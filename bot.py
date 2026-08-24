import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('স্বাগতম! আপনার ফেক ডকুমেন্ট জেনারেটর মিনি অ্যাপটি ব্যবহার করতে পারেন।')

def main() -> None:
    TOKEN = "8834569438:AAHbBg4ZiERupKvSjjC7QFpj89H4nm-IQSI"
    
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
