import base64
import mimetypes
import os

from aiogram.types import User, Message, FSInputFile, InlineQuery, \
 InlineQueryResultCachedAudio

from bot.locale import get_text as _
from bot import log, downloader

VIDEO_FORMATS = [
    "mp4", "mov", "avi", "wmv", "flv", "mkv", "webm", "mpeg", "3gp", "ts",
    "m4v", "mpg", "vob", "ogv", "m2ts"
]

AUDIO_FORMATS = [
    "mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "alac"
]


def format_name(user: User) -> str:
    if user.username:
        return f"@{user.username}"
    return f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"

async def send_audio_inline(query: InlineQuery, file_path: str, title: str = None):
    bot = query.bot

    mime_type, _ = mimetypes.guess_type(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    user_id = query.from_user.id

    input_file = FSInputFile(file_path)

    if ext == '.mp3':
        msg = await bot.send_audio(user_id, input_file, title=title or os.path.basename(file_path))
        file_id = msg.audio.file_id
        result = InlineQueryResultCachedAudio(
            id="1",
            audio_file_id=file_id,
            title="ОТПРАВИТЬ",
            request_timeout=30
        )
        await query.answer(results=[result], cache_time=30, is_personal=True)
        os.remove(file_path)

async def answer(filename: str, message: Message, url: str):
    extension = filename.split(".")[-1]
    if extension in VIDEO_FORMATS:
        await message.answer_video(
            FSInputFile(filename),
            caption=_(
                message, "video_downloaded",
                url=url
            )
        )
    elif extension in AUDIO_FORMATS:
        await message.answer_audio(
            FSInputFile(filename),
            caption=_(
                message, "audio_downloaded",
                url=url
            )
        )
    os.remove(filename)

def encode_param(text: str) -> str:
    encoded = base64.urlsafe_b64encode(text.encode()).decode()
    return encoded.rstrip("=")

def decode_param(encoded: str) -> str:
    padding = '=' * (-len(encoded) % 4)
    decoded = base64.urlsafe_b64decode(encoded + padding).decode()
    return decoded

async def start_download(message: Message, link: str = None, audio_only: bool = False):
    url = link if link else message.text
    m = await message.answer(_(message, "wait_message", url=url))
    try:
        filename = downloader.download_media(url, audio_only=audio_only)
    except:
        await m.edit_text(_(message, "error_url"))
        return
    await answer(filename, m, url=url)
    await m.delete()
