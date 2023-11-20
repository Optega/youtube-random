# YouTube Random video from channel

Telegram bot to fetch random videos from a YouTube channel.

## Tech Stack

**Client:** Telegram

**Server:** Docker

## Installation

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BOT_TOKEN` - You can get it from @BotFather in Telegram

`ADMIN_CHAT_ID` - optional, is not yet used in the project

`YOUTUBE_API_KEY` - Can be obtained by following this instruction ["Step 1" ](https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials)

## Deployment

The project runs in the Docker container, so first make sure that the Docker is installed. If not, install the [Docker](https://docs.docker.com/desktop/)

Build project

```bash
  docker compose build youtube-random
```

Start project

```bash
  docker compose up -d youtube-random
```

## Requirements

| Library                  | Version |
| ------------------------ | ------- |
| aiogram                  | 3.1.1   |
| google-api-python-client | 2.108.0 |

## Usage

To work with the bot, send it a link to any YouTube channel, and it will return a random video from that channel.

But note that the bot only checks the last 50 playlists and the last 50 videos in them. These are the limitations of the YouTube API
