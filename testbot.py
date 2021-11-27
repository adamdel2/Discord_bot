# testbot.py
import os
import discord
import config
from keep_alive import keep_alive
import json
import discord
from dotenv import load_dotenv
from discord.ext import commands


keep_alive()


# Get Discord information for server.
load_dotenv('.env.txt')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
user_data = "userData.json"


# Use AWS instead.
# def save_stars():
#     with open("userData.json", 'w') as json_data:
#         test_var = "test 1 2 1 23423423424"
#         json_data.write("test this\n")
#         json.dump(test_var, json_data)


# Character that signifies the start of a command
bot = commands.Bot(command_prefix='!')
# Text entered into Discord that activates star command.
star = 'goodjob'
test_star = 'getstars'


# Activates bot when !goodjob is entered in Discord.
# Prints a gold star, and adds a star to user star count (not complete).
@bot.command(name=star)
# Action taken when bot is activated.
async def good_job(ctx):
    spongebob_quote = 'Here\'s a gold star! :star:'
    await ctx.send(spongebob_quote)


# Activates bot when !getstars is entered in Discord.
# Prints star count for user.
@bot.command(name=test_star)
async def get_stars(ctx):
    user = get_id(ctx)
    # Need to set star_count to the star count for the user who passed the command.
    star_count = 3
    spongebob_quote = 'You have ' + str(star_count)
    await ctx.send(spongebob_quote)


# Retrieve Discord user id.
def get_id(ctx):
    user = ctx.author
    return user


# Executes bot command.
bot.run(TOKEN)
