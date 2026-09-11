import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import google.generativeai as genai

# Token va API kalitlarini kiritish
TELEGRAM_TOKEN = "8710296743:AAFtyE4fR9aCwv9lA2r9H4Aq6eVXFHtWM0"
GEMINI_API_KEY = "GEMINI_API_KALITINGIZNI_SHU_YERGA_YOZING"

# Gemini AI sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Logging (xatoliklarni kuzatib borish uchun)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men Gemini AI asosida ishlaydigan botman. Menga istalgan savolni yozib yuboring!"
    )

# Foydalanuvchi xabarlarini qabul qilib, Gemini'ga yuborish uchun funksiya
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    try:
        # Gemini'dan javob olish
        response = model.generate_content(user_message)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Kechirasiz, javob olishda xatolik yuz berdi.")

# Asosiy ishga tushirish qismi
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Komandalar va xabarlarni ulash
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
