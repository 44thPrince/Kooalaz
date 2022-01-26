# Kooalaz
Kooalaz is a service made to assist student groups at TERRA. Our goal is to assist in managing the following: attendance, events, sharing club information, and gathering sponsors.
We do this in two parts: a discord bot and a website. Our discord bot allows groups to create profiles for each student and mark their attendance through the bot commands, we plan on expanding the bot to include an event manager for each club. Our website (currently under construction) is aimed towards storing club information and goals to share with potential sponsors.

You can invite our bot to your server <a href="https://discord.com/api/oauth2/authorize?client_id=922674232230563930&permissions=274946181121&scope=bot%20applications.commands">here</a>.

# Help Menu:
Need help on any of our discord bot's commands? This is the place for look for everything you need.

Our bot's prefix is -

__info__ Links to this page.

__register__ This command registers you with the database so that you can record your attendance to a certain club. It takes four parameters: First name, last name, student ID, and grade.

__attend__ Marks you for attendance in the club whose server this command is run in.

__schedule__ Schedule a club event. It takes four parameters: Month, day, year, and the event (the event must be enclosed with quotes if it is more than one word long).

__calendar__ Retrieves this club's calendar, and sends it in the chat.

__remove__ Removes all events that contain a certain keyword from the calendar. It takes one argument: The keyword (If the keyword is more than one word long it must be enclosed with quotes).

__server__ Returns the server ID, which is what all the files are stored under.

__setup__ Post the club information in a file. This takes one argument: The club summary. It does not have to be enclosed in quotes.

__summary__ Retrieves this club's information, and sends it in the chat.

All these things can alternatively be accessed directly from the database.
# Database:
This is where you will find the link to all our data. Data is stored using __server ID's__ and not the server name. To get your Discord server's ID, run __-server__ on our bot.

<a href="https://drive.google.com/drive/folders/1ZiS1raUGa1o982C8-pyf7vxjC1A6vU4s?usp=sharing">Files</a>
