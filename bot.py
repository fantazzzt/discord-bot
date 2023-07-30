import discord
import response
from discord.ext import commands, tasks
from datetime import datetime
import pytz


bot = commands.Bot(command_prefix='.',intents=intents)

channel_id =  # Put your channel id here

async def send_message_gif(message, user_message):
    try:
        gif_url = response.handle_response(user_message)
        await message.channel.send(gif_url)
    except Exception as e:
        print(e)

def get_time_until_launch():
    cst = pytz.timezone('US/Central')
    now = datetime.now(cst)
    launch_time = datetime(2023, 6, 15, 10, 0, 0, tzinfo=cst)  # June 14th, 2023 at 10:00 AM CST
    if now >= launch_time:
        return None  # Return None after the launch time has passed
    else:
        time_until_launch = launch_time - now
        return time_until_launch.total_seconds() // 3600  # Convert to hours

def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        launch_countdown.start()


    @tasks.loop(hours=1)
    async def launch_countdown():
        time_until_launch = get_time_until_launch()
        channel = await client.fetch_channel(channel_id)
        if time_until_launch is None:
            await channel.send("battlebit has released.")
            launch_countdown.stop()
        else:
            await channel.send(f"{time_until_launch} hours until battlebit launch!")




    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        # if not assert_cooldown():
        #     return
        #Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
        await send_message_gif(message, user_message)

    client.run(TOKEN)


