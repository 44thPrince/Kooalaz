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
    user = str(ctx.message.author.id)


    @client.command(pass_context = True)
    async def confirm(ctx):
        if str(ctx.message.author.id) == user:
            await ctx.send("Registered successfully." + " " + user)
            return #placeholder, send data to database
        else:
            return
    @client.command(pass_context = True)
    async def cancel(ctx):
        if str(ctx.message.author.id) == user:
            await ctx.send("Cancelled.")
            return
        else:
            return

@register.error
async def example_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        return await ctx.send("Did you put your full name, student ID and grade level? Example: -register Benjamin Darby 0445062 11")

@client.command(pass_context = True)
async def info(ctx):
    await ctx.send("Usage: -register (Your first name) (Your last name) (Your student ID) (Your grade level). Example: -register Benjamin Darby 0445062 11")

@client.command(pass_context = True)
async def attend(ctx):
    user = str(ctx.message.author.id) #send this info to the database, tell it to update 
    #To do: check if user is registered in database, tell user if they aren't, otherwise say it was successful. 

@client.command(pass_context=True)
async def schedule(ctx, month, day, year, event):
    try:
        int(month)
        int(day)
        int(year)

        filename = str(ctx.message.guild.id) + "_calendar.txt"
        file = open(filename, mode="a")
        file.write("Scheduled for {}/{}/{}: {} \n".format(month, day, year, event))
        file.close()

        await ctx.send("{} successfully scheduled for {}/{}/{}. \n".format(event, month, day, year))
    except(TypeError):
        await ctx.send("the month, day, and year should all be numbers!")
@schedule.error
async def schedule_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter your information in this format: \n"
        + "-schedule <month> <day> <year> <event> - <event> must be formatted as one word!")

@client.command(pass_context=True)
async def calendar(ctx):
    try:
        filename = str(ctx.message.guild.id) + "_calendar.txt"
        file = open(filename, mode="r")
        calendar = file.read()
        file.close()

        await ctx.send(calendar)
    except(IOError):
        await ctx.send("This club has no calendar set up!")

client.run(DISCORD_TOKEN)
