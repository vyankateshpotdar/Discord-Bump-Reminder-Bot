import os
import discord
from discord.ext import commands, tasks
import datetime
from flask import Flask
from threading import Thread

# === WEB SERVER (keep_alive replacement) ===
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Discord Bump Reminder Bot is running on Koyeb!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# === CONFIG ===
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
ROLE_ID = int(os.getenv("ROLE_ID", 0))

# === SETUP ===
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    bump_reminder.start()

# === BUMP REMINDER LOOP ===
@tasks.loop(hours=2)
async def bump_reminder():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        role_mention = f"<@&{ROLE_ID}>"
        await channel.send(f"⏰ {role_mention} Time to bump the server! Use `/bump` 🚀")

# === CHECK NEXT BUMP TIME ===
@bot.command()
async def nextbump(ctx):
    """Show time of next bump reminder"""
    next_time = bump_reminder.next_iteration
    if next_time:
        formatted = next_time.strftime('%Y-%m-%d %I:%M %p')
        await ctx.send(f"📅 Next bump reminder: `{formatted}`")
    else:
        await ctx.send("The reminder hasn't started yet.")

if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
