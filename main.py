from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.filters import Command
import openai
from aiogram.utils.executor import start_polling

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment variables")

if not openai.api_key:
    raise ValueError("OpenAI_API_KEY is not set in the environment variables")


class Reference:
    """
    A class to store the previous response from the OpenAI API.
    """
    def __init__(self):
        self.response = ""

reference = Reference()
model_name = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

async def set_bot_commands():
    """
    Set commands for the bot in the Telegram UI.
    """
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/clear", description="Clear previous conversation"),
        BotCommand(command="/help", description="Get help information"),
    ]
    await bot.set_my_commands(commands)


@dispatcher.message_handler(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Hello! How can I assist you today?")


def clear_previous():
    """
    A function to clear the previous conversation and context.
    """
    reference.response = ""


@dispatcher.message_handler(Command("clear"))
async def clear_conversation(message: types.Message):
    """
    This handler clears the previous conversation and context.
    """
    clear_previous()
    await message.reply("I have cleared the previous conversation and context.")


@dispatcher.message_handler(Command("help"))
async def helper(message: types.Message):
    """
    This handler receives messages with `/help` command.
    """
    help_text = """
Hi, I am a Telegram bot created by Deepak! Here are the available commands:
- /start: Start the conversation
- /clear: Clear the previous conversation and context
- /help: Get help information
    """
    await message.reply(help_text)


@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the ChatGPT API.
    """
    print(f"User: {message.text}")
    
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text},
            ]
        )
        await message.answer(response.choices[0].message['content'])
    except Exception as e:
        await message.answer("Sorry, I couldn't process your request. Please try again later.")
        print(f"Error: {e}")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_bot_commands())
    start_polling(dispatcher, skip_updates=True)
