import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# এখানে নিজের Telegram Channel / Post-এর লিংক বসাবেন
BUTTONS = [
    ("🌐 সকল ভিডিও", "https://t.me/+HfXNYs7PPsYzZmY1"),
    ("🔥 নতুন ভিডিও", "https://vairallink.site/post/totini-viral-link-trending-social-media-buzz-latest-updates-details"),
    ("🎬 জনপ্রিয় ভিডিও", "https://vairallink.site/post/mehazabien-chowdhury-special-moments-latest-updates-photo-highlights"),
]

WELCOME_MESSAGE = (
    "👋 <b>স্বাগতম!</b>\n\n"
    "📢 আপনার পছন্দের ভিডিও দেখতে নিচের বাটনে ক্লিক করুন।\n\n"
    "👇 <b>Choose a channel below:</b>"
)


def make_keyboard():
    rows = [
        [InlineKeyboardButton(label, url=url)]
        for label, url in BUTTONS
    ]
    return InlineKeyboardMarkup(rows)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=make_keyboard(),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("বট ব্যবহার করতে /start লিখুন।")


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            body = b"Telegram button bot is running"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return


def start_health_server():
    port = int(os.environ.get("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    Thread(target=server.serve_forever, daemon=True).start()


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable সেট করুন।")

    start_health_server()

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
