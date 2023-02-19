# Bot that allows you to start pomodoro sessions of 25 minutes with a 5 minutes break and push a notification when it ends.

import asyncio
import asyncio
import datetime
from discord.ext import commands
from dataclasses import dataclass
import discord

bot_token = "MTA3Njg5NjI4NDcyNTc1NTkxNA.GgcH6l.BTkaeBIep30tonUKvSpBFKO1mTTnPtP2zt5ddY"
channel_id = 1076901441152757771


@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
session = Session()


@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(channel_id)
    await channel.send("Hello! Study bot is ready!")


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
        session.is_active = False
        await ctx.send("Take a 5 minutes break!")
        await asyncio.sleep(5 * 60)
        await ctx.send("Break ended!")


@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    await ctx.send("Session ended!")


@bot.command()
async def status(ctx):
    if session.is_active:
        await ctx.send("A session is active!")
    else:
        await ctx.send("No session is active!")


bot.run(bot_token)
