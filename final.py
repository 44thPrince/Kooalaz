#Dependencies: Discord, dotenv
import asyncio, os
from pathlib import Path
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("token.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix = "-")

#To do: add functionality for multiple clubs and rosters.

#ATTENDANCE STARTS

@client.event
#triggers on program start
async def on_ready():
    global rosterList
    rosterRead = open(str(Path().absolute()) + "\\roster.txt", "w+")
    rosterRawList = rosterRead.readlines()
    rosterList = []
    for i in rosterRawList:
        string = i.strip().split('|')
        tempArr = []
        for j in string:
            tempArr.append(j)
            print(j)
        rosterList.append(tempArr)
    rosterRead.close()

@client.event
async def on_command_error(ctx, error):
    pass
@client.command(pass_context = True)
async def register(ctx, fname, lname, id, grade):
    global endMethod
    global rosterList
    endMethod = False
    await ctx.send('Is this correct? Your first name is {}, your last name is {}, your student ID is {}, and your grade level is {}th? Type -confirm or -cancel.'.format(fname, lname, id, grade))
    user = str(ctx.message.author.id)
    strings = [fname, lname, id, grade, user + "\n"]
    rosterAppend = open(str(Path().absolute()) + "\\roster.txt", "a")
    @client.command(pass_context = True)
    async def confirm(ctx):
        global endMethod
        global rosterList
        if str(ctx.message.author.id) == user:
            if not(check(user)):
                await ctx.send("Registered successfully.")
                rosterAppend.write('|'.join(strings))
                rosterList.append('|'.join(strings))
                endMethod = True
                return #placeholder, send data to database
            else:
                await ctx.send("You're already registered.")
                endMethod = True

        else:
            return
    @client.command(pass_context = True)
    async def cancel(ctx):
        global endMethod
        if str(ctx.message.author.id) == user:
            await ctx.send("Cancelled.")
            endMethod = True
            return
        else:
            return
    if endMethod:
        rosterAppend.close()
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
    global rosterList
    attendanceRoster = open(str(Path().absolute()) + "\\attendance.txt", "a")
    user = str(ctx.message.author.id) #send this info to the database, tell it to update
    for userList in rosterList:
        print (user)
        print(userList)
        if str(user) in userList:
            print("Did something.")
            temp = userList
            temp.pop()
            print("Did something after.")
            await ctx.send("You have been marked as present")
            attendanceRoster.write(" ".join(temp))
            attendanceRoster.close()
            return
    await ctx.send("You are not registered yet! Do -register to register or -info to learn how to register.")
    attendanceRoster.close()
    return

def check(user):
    global rosterList
    for userID in rosterList:
        if str(user) in userID:
            return True
    return False

#CALENDAR BEGINS

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

@client.command(pass_context=True)
async def remove(ctx, event):
    try:
        filename = str(ctx.message.guild.id) + "_calendar.txt"
        file = open(filename, mode="r")
        events = file.readlines()
        file.close()

        fixed = ""
        for i in range(len(events)):
            if event in events[i]:
                events[i] = ""
            fixed += events[i]

        file = open(filename, mode="w")
        file.write(fixed)
        file.close()

        await ctx.send("All events containing the keyword {} have been removed from the calendar.".format(event))
    except(IOError):
        await ctx.send("This club has no calendar set up!")
@remove.error
async def remove_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please include a keyword to search for and remove.")

client.run(DISCORD_TOKEN)
