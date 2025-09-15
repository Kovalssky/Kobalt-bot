start_message = 👋 Привет { $user }!
 Я бот для скачивания видео и аудио из сервисов. Так же, я могу скачивать музыку с Яндекс.Музыки!

 Полный список сервисов /services

  <i>- Музыку можно скачивать через инлайн-режим <code>@{ $bot_username } ссылка</code></i>

services_message = <b>Поддерживаемые сервисы:</b>
 <blockquote>{ $services }</blockquote>
 <i>Если какой-то сервис из этого списка не работает, обязательно сообщите разработчику @devKovalsky!</i>

video_downloaded = 🎉 Вот ваше <b><a href='{ $url }'>видео</a></b>
photo_downloaded = 🎉 Вот ваше <b><a href='{ $url }'>фото</a></b>
audio_downloaded = 🎉 Вот ваше <b><a href='{ $url }'>аудио</a></b>

wait_message = 🔄 Загрузка, ожидайте...

services_description = Список поддерживаемых сервисов
audio_description = Скачать только аудио