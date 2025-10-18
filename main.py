import discord
from discord.ext import commands, tasks
import datetime
from keep_alive import keep_alive
keep_alive()

# === CONFIG ===
TOKEN = "" 
CHANNEL_ID = 
ROLE_ID = 
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

bot.run(TOKEN)
