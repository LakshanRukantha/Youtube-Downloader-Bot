from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Follow these three simple steps.\n\n1) Send URL of YouTube video do you want to download. 😃\n\n2) Select quality of video or audio do you want to download. 🤩\n\n3) Download ✅\n\nContact @Lakshan_Rukantha for report bugs and problems of this bot."
    await message.reply_text(helptxt)
