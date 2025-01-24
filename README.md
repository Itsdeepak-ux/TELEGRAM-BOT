# Telegram Bot with AI Integration

This project contains two Telegram bot implementations using the `aiogram` library:
1. `man.py`: A ChatGPT-integrated bot that responds to user input using the OpenAI API.
2. `echobot.py`: A basic echo bot for testing purposes.

## Features

### `man.py`
- **ChatGPT Integration**: Uses OpenAI's `gpt-3.5-turbo` model to generate responses.
- **Command Handlers**:
  - `/start`: Starts the bot and greets the user.
  - `/clear`: Clears the previous conversation context.
  - `/help`: Displays available commands and usage instructions.
- **Environment Variables**:
  - `TELEGRAM_BOT_TOKEN`: The bot token from Telegram.
  - `OpenAI_API_KEY`: The API key for OpenAI's GPT.

### `echobot.py`
- A simple bot that responds with a static message to `/start` and `/help` commands.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher installed.
- [Telegram Bot Token](https://core.telegram.org/bots#botfather) from BotFather.
- [OpenAI API Key](https://platform.openai.com/signup/) for `man.py`.

### Installation
1. Clone this repository:
   `
