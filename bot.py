# bot by Luwak Daisuki

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "nyaa gs":
        await client.send_message(message.channel, "Di mohon bantuannya untuk mengisi #data-gs-playerwajib, di sana sudah ada BOT yg mencatat GS para player, intinya jadi lebih mudah. dgn adanya GSBOT ini player bisa mengisi & mencatat GS nya masing-masing tolong di sertakan dgn FOTO Charnya, jgn foto KTP. saya harap semua player WAJIB mengisinya & mulai sekarang jgn ada FAKE GS/apapun percuma gw cari bot susah-susah anjing gk ada yg ngisi. & di harapkan jgn ada kata malu-malu nunjukin GS di #data-gs-playerwajib di situ bukan ajang PAMER GS/ NEBAR GAREM EA ANJING data gs emank di perlukan buat posisi char lu di NW/SW. gmn cara ngisinya? https://media.discordapp.net/attachments/385410916511907842/451984665016795137/gsbot.png")

    if message.content == "nyaa party":
        await client.send_message(message.channel, "Mulai hari Jum'at - Minggu ini, mhn bantuannya utk mengisi DATA di #data-party-nodewar di sana tinggal ISI GOOGLE DOCUMENT FN/IGN aja secara otomatis data akan tersimpan, di sana juga sudah di jelaskan peratureannya melalui NOTE di bawah sendiri, saya harapkan bisa ada 20 player/ sampai 30 palyer seperti pada waktu NW keamrin/ yg member baru diharapkan juga bisa ikut berpartisipasi dalam acara yg di adakan 1x pada hari minggu jam 20.00 malam.")

    if message.content == "nyaa absen":
        await client.send_message(message.channel, "Sudah sekitar 4x kita WAR tapi #absensi-war JARANG YG ISI. saya harapkan setiap hari member selalu CEK di #absensi-war , absensi war selalu di perbarui setiap HARI SENIN di harapkan member langsung CEK & mulai update. & beberapa hari lalu ada yg Update pada saat HARI H/ pada jam waktu mulai NW, hemmm saya melihat terdapat kecurangan di sini wkwkww, Jadi Pengisian ABSENSI akan di batasi mulai dari hari SENIN - MINGGU jam 12 siang.")


client.run("NDUwODgwMzU4MjA1MDk1OTM2.De6Xew.1d0HMWJnNJypcliPle2KcT9ht0o")
