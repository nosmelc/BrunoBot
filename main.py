import os
from keep_alive import keep_alive
from discord.ext import commands, tasks
import discord
import asyncio
import random


client = discord.Client()

bot = commands.Bot(
	command_prefix="b!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 140241867542364160  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

# Shit we cares about starts here!!

@bot.event
async def on_message(message):
    id = bot.get_guild(809148317187440670)

    if message.content.find("hello") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/809148317187440672/809192365449150484/tenor.gif") 
    elif message.content.find("bye") != -1:
        await message.channel.send("I am still Bruno mars") 
    if message.content.find("b!commands") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/809148317187440672/809334168924323860/bruno.png") 
    elif message.content.find("b!kiss") != -1:
        await message.channel.send("https://tenor.com/view/bruno-mars-mwah-kiss-kissy-face-kisses-gif-7308595")

# Trivia
    elif message.content.find("b!trivia") != -1:
        factList = [
        "he is the only singer with a planet named after him! :rocket:",
        "he is half swagapino! :flag_ph:",
        "he played an integral role in Rio 2! :movie_camera:",
        "Mars, at the age of 24, was arrested with a bag of cocaine in the bathroom of the Las Vegas Hard Rock Hotel & Casino in September 2010. :oncoming_police_car:",
        "Bruno Mars is a hooligan",
        "he's coming for us oh god oh fuck",
        "his real name is Peter Gene Bayot Hernandez! :mag:",
        "he was an Elvis impersonator at just 4! :musical_note:",
        "his Twitter is @BrunoMars! :bird:",
        "when Bruno was 15 years old, he had a crush on his teacher (over twice his age) and he gave her a love letter with his mums ring in, which he had stolen from her! The teacher told his mother, and gave her the ring back! What a simp! :ring:",
        "his first written song was called ‘Sugar Mama’, and he admits it was horrible! :thumbsdown:",
        "out of desperation, Bruno Mars once accepted a job as a DJ! But because he doesn’t know a thing about DJing, he was fired right after his first gig! What a fucking loser! :joy::point_right: <:mars:809172688735830056>",
        "he wrote an entire song because he was scared of losing his girlfriend who for some damn reason hasn't broken up with him yet.  What a little bitch!",
        "he would catch a grenade for you... :bomb::heart:",
        "bruno mars fuckin sucks",
        "he is awesome!!",
        "he is a mere 5 feet and 5 inches tall. pathetic"]
        await message.channel.send("<:mars:809172688735830056> Bruno Mars Trivia! <:mars:809172688735830056> \n"
        + factList[random.randint(0, 16)])
# Trivia Images
    elif message.content.find ("Bruno Mars is a hooligan") != -1:
        await message.channel.send("https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/931/524/bruno-mars-ap.jpg?ve=1&tl=1")
    elif message.content.find("Las Vegas Hard Rock Hotel & Casino") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/809148317187440672/809189144889786429/unknown.png")
    elif message.content.find("he's coming for us oh god oh fuck") != -1:
        await message.channel.send("https://i.ytimg.com/vi/fLexgOxsZu0/maxresdefault.jpg")
    elif message.content.find("elvis") != -1:
	await message.channel.send("https://img.buzzfeed.com/buzzfeed-static/static/2017-03/23/17/tmp/buzzfeed-prod-fastlane-01/tmp-name-2-1118-1490303701-4_dblbig.jpg")
# End Trivia
    elif message.content.find("cutie") != -1:
        await message.channel.send("https://tenor.com/view/bruno-mars-gif-11251108")
    elif message.content.find("You're amazing") != -1:
        await message.channel.send("Just the way you are :heart:", tts=True)
# Strip
    elif message.content.find("strip") != -1:
        shirtList = ["https://i.dailymail.co.uk/i/newpix/2018/08/29/22/4F823AB700000578-0-image-a-94_1535577712146.jpg",
        "https://64.media.tumblr.com/6d8501e1d22f6ae0c47c94b1dbd7cee8/tumblr_pea5dnOCds1ut162yo1_500.gifv",
        "https://cdn.discordapp.com/attachments/809148317187440672/809188362903617546/dcpdex4-0d45534a-80a4-4752-826a-4c647452cd3a.png",
        "https://cdn.discordapp.com/attachments/809148317187440672/809189273018040350/bruno_mars_1___muscle_morph_by_alfab400_dcofatz-200h.png",
        "https://data.whicdn.com/images/133324473/original.jpg",
        "https://pbs.twimg.com/media/BzZTYHzCYAEyvhK.jpg",
        "https://i.pinimg.com/474x/50/84/08/5084081360087b6e12c45b61f57b849f.jpg",
        "https://i.pinimg.com/originals/46/3a/7d/463a7d63bf9de7e6ca14f0ef719a8062.jpg","I would rather not at this time. Frankly, the request alone discomforts me."]
        await message.channel.send(shirtList[random.randint(0, 8)])
# End Strip
    elif message.content.find("Keitho Mars") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/200032422664994816/809195589006393384/20210210_175257.jpg")
    elif message.content == "boo":
        await message.channel.send("Aah!")
    elif message.content == "Aah!":
        await message.channel.send("https://kennethseah.files.wordpress.com/2011/04/brunomars-4-600.jpg?w=768")
    elif message.content.find("gunna") != -1 or message.content.find("mcdonalds") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/546473515679875102/805194084619780126/video0.mp4")
    elif message.content.find("obama") != -1:
        await message.channel.send("https://cdn.discordapp.com/attachments/809148317187440672/809232343365189672/tumblr_ournmeZc541vl9w4bo1_1280.png")
# Number Commands
    elif message.content.find("24") != -1:
      twentyFour = random.randint(1,3)
      if message.author != bot.user:
        if twentyFour == 3:
          await message.channel.send("https://rb.gy/hwfz2k")
    elif message.content.find("27") != -1:
      twentySeven = random.randint(1,3)
      if message.author != bot.user:
        if twentySeven == 3:
          await message.channel.send("https://rb.gy/q8lxny")
# Random Message
    x = random.randint(1, 100)
    brunoMars = [
    "I am Bruno Mars",
    "I got a beach house in Miami",
    ":arrow_up: That's what I like :arrow_up:",
    "Baby squirrel, you's a sexy mother-fucker",
    "It's a beautiful night... we're lookin' for somethin' dumb to do.",
    "Do do doh do doh do do do (in the tune of *Uptwon Funk*)",
    "Shut the fuck up loser",
    "Tyler has to wait in line if he wants to stab me.",
    "<:mars:809172688735830056>",
    "https://cdn.discordapp.com/attachments/809148317187440672/809242038574776320/tenor.gif",
    "I love the Sex...",
    "My demo was horrible, I sounded like a chipmunk",
    "Out here drippin' in finesse",
    "I was born on October 8th, 1985.",
    "I didn't go to college because I am not smart",
    "Treasure, that is what you are!",
    "I am Bruno Mars"
    ]
    if message.author != bot.user:
      if x == 100:
        await message.channel.send(brunoMars[random.randint(0, 16)])
  
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=1, name='Uptown Funk', url='https://www.youtube.com/watch?v=ngywvbPkIZA', platform='YouTube'))

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot
