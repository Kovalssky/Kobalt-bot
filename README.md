[![version](https://img.shields.io/badge/Version-0.1.1-red?style=flat&logo=github&logoColor=white)]()

# Hi, I'm Kobalt!

A telegram bot for downloading video or audio from sources: TikTok, YouTube, Pinterest etc.

TODO: Make restrictions. Add support and add logging

## How to install and run Kobalt Bot with Docker
**Step 1: Download the latest Docker image**
```
docker pull registry.gitlab.com/kovalssky/kobalt-bot:latest
```
**Step 2: Run the container with your bot token**
Replace your_token_here with your actual bot token:
```
docker run -e TOKEN=your_token_here registry.gitlab.com/kovalssky/kobalt-bot:latest
```
That’s it!

**Optional: run container in the background (detached mode)**
```
docker run -d -e TOKEN=your_token_here registry.gitlab.com/kovalssky/kobalt-bot:latest
```
---
### If you have multiple environment variables, you can use an .env file:

```
# .env file content
TOKEN=your_token_here
```

Start the container using the env file:

```
docker run --env-file .env registry.gitlab.com/kovalssky/kobalt-bot:latest
```
This is a quick and easy way to get the bot running using Docker.

---
## Language Support

Currently, the bot supports only **Russian** and **English** languages.

The bot uses automatic localization selection, meaning it adapts to the user's device language automatically by leveraging Telegram's built-in features.

Localization is implemented using the **Fluent** framework, providing flexible and convenient translation management.

New languages can be added by creating translation files inside the `locales` folder.

Examples of translation files can be copied and adapted from existing completed translations.

---
> The bot is currently in alpha version and will receive frequent updates.
