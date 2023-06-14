import discord
import response
from discord.ext import commands, tasks
from datetime import datetime
import pytz


# async def send_message(message, user_message, is_private):
#     try:
#         respons = response.handle_response(user_message)
#         await message.author.send(respons) if is_private else await message.channel.send(respons)
#     except Exception as e:
#         print(e)
intents = discord.Intents.all()
# WHEN = time(18, 0, 0)  # 6:00 PM
bot = commands.Bot(command_prefix='.',intents=intents)

channel_id =  # Put your channel id here

async def send_message_gif(message, user_message):
    try:
        gif_url = response.handle_response(user_message)
        await message.channel.send(gif_url)
    except Exception as e:
        print(e)


# async def called_once_a_day():  # Fired every day
#     await bot.wait_until_ready()
#     channel = bot.get_channel(channel_id)
#     gif_url = response.handle_response('what day is it')
#     await channel.send(gif_url)

# async def background_task():
#     now = datetime.utcnow()
#     if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start
#     while True:
#         now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
#         seconds_until_target = (target_time - now).total_seconds()
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
#         await called_once_a_day()  # Call the helper function that sends the message
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration













# COOLDOWN_AMOUNT = 180.0  # seconds
# last_executed = time.time()
# def assert_cooldown():
#     global last_executed  # you can use a class for this if you wanted
#     if last_executed + COOLDOWN_AMOUNT < time.time():
#         last_executed = time.time()
#         return True
#     return False
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


