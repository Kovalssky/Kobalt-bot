import validators
from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from bot.downloader import download_media
from bot.locale import get_text as _
from bot import utils

router = Router()

@router.inline_query()
async def inline_handler(query: InlineQuery):
    user_input = query.query

    if not validators.url(user_input):
        results = [
            InlineQueryResultArticle(
                id="1",
                title=_(query, "error_invalid_url"),
                input_message_content=InputTextMessageContent(
                    message_text=_(query, "inline_alert")
                )
            )
        ]
        await query.answer(results=results, cache_time=30, is_personal=True)
    else:
        if "music.yandex" in user_input:
            filename = download_media(user_input)
            await utils.send_audio_inline(query, filename)
        else:
            results = [
                InlineQueryResultArticle(
                    id="1",
                    title=_(query, "error_invalid_url"),
                    input_message_content=InputTextMessageContent(
                        message_text=_(query, "inline_alert")
                    )
                )
            ]
            await query.answer(results=results, cache_time=30, is_personal=True)