SIMPLE TELEGRAM BUTTON BOT

1) Open bot.py and replace the three sample links:
   https://t.me/your_channel
   https://t.me/your_channel2
   https://t.me/your_channel3

2) Install:
   pip install -r requirements.txt

3) Set BOT_TOKEN as an environment variable:
   Linux/macOS:
     export BOT_TOKEN="YOUR_BOTFATHER_TOKEN"
     python bot.py

   Windows PowerShell:
     $env:BOT_TOKEN="YOUR_BOTFATHER_TOKEN"
     python bot.py

4) Render:
   - Upload bot.py and requirements.txt to a GitHub repository.
   - Create a Render Web Service connected to that repository.
   - Build Command: pip install -r requirements.txt
   - Start Command: python bot.py
   - Health Check Path: /health
   - Add Environment Variable BOT_TOKEN with your real token.
   - Deploy, then send /start to your bot in Telegram.

IMPORTANT:
- Never upload your real token to GitHub.
- The buttons open the URLs you set in BUTTONS.
- Telegram Bot API does not let bots set custom inline-button colors;
  the Telegram app controls how these buttons look.
- Render free web services may sleep and local files are not persistent.
  This bot has no database, so no user data is stored.
