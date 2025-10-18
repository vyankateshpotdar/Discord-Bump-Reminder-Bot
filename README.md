# 🤖 Discord Bump Reminder Bot

A simple yet powerful **Discord bot** built with Python that keeps your server active by automatically sending bump reminders every 2 hours.

---

## 🧩 Features
- ⏰ Automated bump reminders every 2 hours  
- 🎯 Mentions a specific role to notify members  
- 💬 Command: `!nextbump` to check next reminder time  
- 🧠 Task scheduling using `discord.ext.tasks`  
- 🌐 Keeps running 24/7 using `keep_alive()`  

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/discord-bump-reminder-bot.git
cd discord-bump-reminder-bot
2. Install dependencies
pip install discord.py flask

3. Add your credentials

Edit the config section in the script:

TOKEN = "YOUR_DISCORD_BOT_TOKEN"
CHANNEL_ID = 123456789012345678
ROLE_ID = 987654321098765432

4. Run the bot
python main.py

🧠 How It Works

The bot starts and runs a scheduled loop (@tasks.loop(hours=2)).

Every 2 hours, it sends a message like:

⏰ @Bumpers Time to bump the server! Use /bump 🚀


Users can type !nextbump to see when the next reminder is coming.

keep_alive() helps it stay online 24/7 (e.g., on Replit).

🖼️ Example
⏰ @RoleName Time to bump the server! Use /bump 🚀
!nextbump
📅 Next bump reminder: 2025-10-20 02:00 PM

🚀 Future Plans

Slash command support (/nextbump)

Configurable reminder intervals

Analytics dashboard for bumps

Multi-server support

👨‍💻 Author

Vyankatesh Potdar
B.Tech CSE Student | MIT-ADT, Pune
🔗 LinkedIn

🪪 License

This project is open-source under the MIT License.
