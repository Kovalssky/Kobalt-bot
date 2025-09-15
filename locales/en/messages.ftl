start_message = 👋 Hello { $user }!
 I'm a bot for downloading video and audio from services. Also, I can download music from Yandex.Music!

 Full list of services /services

 <i>- Music can be downloaded through the inline mode using <code>@{ $bot_username } link</code></i>

services_message = <b>Supported services:</b>
 <blockquote>{ $services }</blockquote>
 <i>If any service from this list is not working, please be sure to report it to the developer @devKovalsky!</i>

video_downloaded = 🎉 Your <b><a href='{ $url }'>video</a></b>
photo_downloaded = 🎉 Your <b><a href='{ $url }'>photo</a></b>
audio_downloaded = 🎉 Your <b><a href='{ $url }'>audio</a></b>

wait_message = 🔄 Downloading, please wait...

services_description = List of supported services
audio_description = Download audio only
