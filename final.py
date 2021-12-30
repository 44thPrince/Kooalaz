'''
The plan:
Create a channel where users can register for attendance.

Commands:

-register:
The user registers by calling command -register (first name) (last name) (student id) (grade level). Then the bot confirms by asking the user to type in confirm. (Bot needs to only accept this from the user registering.) Then the bot adds this information and the user's id to the database (WIP).

-attend:
The user types -attend to mark themselves present. If the user is not registered, it prompts them to register.
'''



#Dependencies: Discord
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#client = discord.Client()
client = commands.Bot(command_prefix = "-")

@client.event
async def on_command_error(ctx, error):
    pass
@client.command(pass_context = True)
async def register(ctx, fname, lname, id, grade):
            
    await ctx.send('Is this correct? Your first name is {}, your last name is {}, your student ID is {}, and your grade level is {}th? Type -confirm or -cancel.'.format(fname, lname, id, grade))

    @client.command(pass_context = True)
    async def confirm(ctx):
        await ctx.send("Registered successfully.")
        return #placeholder, send data to database
    
    @client.command(pass_context = True)
    async def cancel(ctx):
        await ctx.send("Cancelled.")
        return

@register.error
async def example_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        return await ctx.send("Did you put your full name, student ID and grade level? Example: -register Benjamin Darby 0445062 11")

@client.command(pass_context = True)
async def info(ctx):
    await ctx.send("Usage: -register (Your first name) (Your last name) (Your student ID) (Your grade level). Example: -register Benjamin Darby 0445062 11")

client.run(DISCORD_TOKEN)