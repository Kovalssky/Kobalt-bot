import os
import yt_dlp

def download_media(url: str, audio_only: bool = False, output_template='%(title)s.%(ext)s'):
    ydl_opts = {
        'cookies': "cookies.txt",
        'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
        'outtmpl': output_template,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'cachedir': False,
        'progress_hooks': [],
    }

    if audio_only:
        ydl_opts['postprocessors'] = [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename
