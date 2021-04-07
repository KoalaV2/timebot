from discord.ext import commands
import json
import sqlite3

with open("settings.json") as f:
    try:configfile = json.load(f)
    except:configfile = {}

conn = sqlite3.connect('database.db')
c = conn.cursor()
token = configfile['discordKey']
prefix = "./"
bot = commands.Bot(command_prefix=prefix)

def createdatabase():
    c.execute('''CREATE TABLE IF NOT EXISTS users (userid,timezone)''')
    conn.commit()
    conn.close()

def main():

    @bot.event
    async def on_ready():
        print("Bot is online.")

    @bot.command()
    async def echo(ctx, *, content:str):
        await ctx.send(content)

    bot.run(token)  # Where 'TOKEN' is your bot token

if __name__ == "__main__":
    createdatabase()
    #main()
