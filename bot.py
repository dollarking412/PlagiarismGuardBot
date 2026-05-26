import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 *PlagiarismGuard Bot Active!*\n\nSend me any text and I'll check it for plagiarism.\n\n"
        "📝 *How it works:*\n"
        "• Send text (min 50 characters)\n"
        "• I'll check against web sources\n"
        "• Get similarity score + sources\n\n"
        "⚠️ *Note:* Free tier has rate limits. Send /help for more.",
        parse_mode="Markdown"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *Help Guide*\n\n"
        "• Send any text to check for plagiarism\n"
        "• Maximum 5000 characters per check\n"
        "• Results include percentage and sources\n\n"
        "*Commands:*\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/about - About this bot",
        parse_mode="Markdown"
    )

# About command
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *PlagiarismGuard Bot v1.0*\n\n"
        "Helps students, writers, and professionals check content originality.\n\n"
        "Made with ❤️ for Telegram",
        parse_mode="Markdown"
    )

# Plagiarism check function (simulated - replace with real API later)
async def check_plagiarism(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    # Validation
    if len(text) < 50:
        await update.message.reply_text("⚠️ Please send at least 50 characters for accurate checking.")
        return
    
    if len(text) > 5000:
        await update.message.reply_text("⚠️ Text too long! Maximum 5000 characters allowed.")
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text("🔍 Analyzing your text... Please wait.")
    
    # Simulated result (in production, call real plagiarism API here)
    # Replace this block with actual API call to Copyleaks, Prepostseo, etc.
    import random
    percentage = random.randint(0, 100)
    
    if percentage < 20:
        result = f"✅ *Excellent!*\n\nSimilarity Score: {percentage}%\nStatus: Very Low risk\nYour content appears to be highly original."
    elif percentage < 50:
        result = f"⚠️ *Caution*\n\nSimilarity Score: {percentage}%\nStatus: Medium risk\nConsider rephrasing some sections."
    else:
        result = f"❌ *High Similarity Detected*\n\nSimilarity Score: {percentage}%\nStatus: High risk\nRewrite significantly or add proper citations."
    
    await processing_msg.edit_text(result, parse_mode="Markdown")

# Main function
def main():
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_plagiarism))
    
    # Start bot
    print("🤖 PlagiarismGuard Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
