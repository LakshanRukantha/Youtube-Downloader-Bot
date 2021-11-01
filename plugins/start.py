from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    welcomed = f"Hello <b>{message.from_user.first_name} ☺️</b>\n\nUseful Commands\n\n💠 /help - How to use this bot\n\n💠 /ping - Check bot status\n\n💠 /report - Report any questions to admin"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
