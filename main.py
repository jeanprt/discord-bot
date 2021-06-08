import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True

bot = commands.Bot(command_prefix="!", intents=default_intents)


@bot.event
async def on_ready():
    print("Le bot est connecté.")

@bot.event
async def on_message(message):
    #Ping - Pong pour tester le bot
    if message.content.lower() == "ping":
        await message.channel.send("Pong")
    #message drole aleatoire
    if message.content.lower == "!hello":
        await message.channel.send(random.choice(('Salut,\n Ça va ?!', 'Bonjour à toi!', 'Heyy Bro', 'Salutt, tu fais quoa ?!')))
    #surprendre l'utilisateur
    if message.content == "@John's Bot":
        await message.channel.send("Yeah, It's me!")
        await message.channel.send("Que puis-je faire pour toi ?!")
    elif message.content == "@John's Bot#4035":
        await message.channel.send("Yeah, It's me!")
        await message.channel.send("Que puis-je faire pour toi ?!")

@bot.event
async def on_member_join(member):
    print(f"Un nouveau membre est arrivé : {member.display_name}")


@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()


bot.run(os.getenv("TOKEN"))
