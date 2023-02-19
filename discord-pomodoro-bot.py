# Author: @youcefzaid
# Description: A discord bot that helps you study using the pomodoro technique

# import the required libraries and modules
from dataclasses import dataclass
from discord.ext import commands
import asyncio
import datetime
import discord

# Bot token and channel id. You can get the bot token from the discord developer portal and the channel id from the discord client
bot_token = "BOT_TOKEN"
channel_id = CHENNEL_ID


# Dataclass to store the session data
@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0
    completed_sessions: int = 0


# Create the bot and the session
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
session = Session()


# When the bot is ready, send a message to the channel
@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(channel_id)
    await channel.send("Hello! Study bot is ready!")


# starts a session
@bot.command()
async def start(ctx, sessions: int = 1):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    for i in range(sessions):
        session.start_time = datetime.datetime.now()
        session.is_active = True
        await ctx.send("Session started!")

        await asyncio.sleep(25 * 60)
        await ctx.send("Session ended!")
        completed_sessions = + 1
        session.is_active = False
        await ctx.send("Take a 5 minutes break!")
        await asyncio.sleep(5 * 60)
        await ctx.send("Break ended!")

    await ctx.send("All sessions completed!")


# returns the number of completed sessions
@bot.command()
async def completed(ctx):
    await ctx.send(f"Completed sessions: {session.completed_sessions}")


# ends the session
@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    await ctx.send("Session ended!")


# pauses the session
@bot.command()
async def pause(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    await ctx.send("Session paused!")


# resumes the session
@bot.command()
async def resume(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return

    session.is_active = True
    await ctx.send("Session resumed!")


# returns the time elapsed since the start of the session
@bot.command()
async def elapsed(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    time_elapsed = datetime.datetime.now() - session.start_time
    await ctx.send(f"Time elapsed: {time_elapsed}")


# returns the status of the session
@bot.command()
async def status(ctx):
    if session.is_active:
        await ctx.send("A session is active!")
    else:
        await ctx.send("No session is active!")

# Run the bot
bot.run(bot_token)
