
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = "8710296743:AAFtyE4f7R9aCwv9lA2r9H4Aq6eVXfHtwM0" GEMINI_API_KEY = "AQ.Ab8RN6JYsUYLJ0v4YpZAwLROgnTDE6DVSMo64Iyif_g2gz_jng"
genai.configure(api_key=GEMINI_API_KEY) model = genai.GenerativeModel("gemini-1.5-flash")
logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "Assalomu alaykum! Men Gemini AI botman. Istalgan savolingizni yuboring, javob beraman!" )
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): user_text = update.message.text await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
try:
    response = model.generate_content(user_text)
    await update.message.reply_text(response.text)
except Exception as e:
    logging.error(f"Xatolik: {e}")
    await update.message.reply_text("Kechirasiz, xatolik yuz berdi. Birozdan so'ng qayta urinib ko'ring.")
if name == 'main': app = ApplicationBuilder().token(TELEGRAM_TOKEN).build() app.add_handler(CommandHandler('start', start)) app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)) print("Bot muvaffaqiyatli ishga tushdi...") app.run_polling()
