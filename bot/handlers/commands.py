import json

import validators
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, FSInputFile

from bot.locale import get_text as _
from bot import utils

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    commands = [
        BotCommand(command="services", description=_(message, "services_description")),
        BotCommand(command="audio", description=_(message, "audio_description"))
    ]
    me = await message.bot.get_me()

    await message.bot.set_my_commands(commands)
    await message.answer_photo(
        photo=FSInputFile(f"media/hello_{message.from_user.language_code}.png"),
        caption=_(message, "start_message",
          user=utils.format_name(message.from_user),
          bot_username=me.username
        )
    )

@router.message(Command("services"))
async def services_cmd(message: Message):
    with open("services.json", "r", encoding="utf-8") as f:
        services = json.load(f)
    await message.answer_photo(
        photo=FSInputFile(f"media/services_{message.from_user.language_code}.png"),
        caption=_(message, "services_message", services=", ".join(services))
    )

@router.message(Command("audio"))
async def services_cmd(message: Message):
    if len(message.text.split()) != 2:
        await message.answer(text=_(message, "error_no_url_argument"))
        return
    link = message.text.split()[1]
    await utils.start_download(message, audio_only=True, link=link)

@router.message(lambda c: validators.url(c.text))
async def url_message_handle(message: Message):
    await utils.start_download(message)