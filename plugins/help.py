from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Follow these three simple steps.\n

1) Send URL of YouTube video do you want to download. 😃\n

2) Select quality of video or audio do you want to download. 🤩\n

3) Download ✅\n

Contact @Lakshan_Rukantha for report bugs and problems of this bot."
    await message.reply_text(helptxt)
