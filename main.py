from discord.ext import commands
import json

with open("settings.json") as f:
    try:configfile = json.load(f)
    except:configfile = {}

token = configfile['discordKey']
print(token)
prefix = "./"
bot = commands.Bot(command_prefix=prefix)

def main():

    @bot.event
    async def on_ready():
        print("Bot is online.")

    @bot.command()
    async def echo(ctx, *, content:str):
        await ctx.send(content)

    bot.run(token)  # Where 'TOKEN' is your bot token


if __name__ == "__main__":
    main()
