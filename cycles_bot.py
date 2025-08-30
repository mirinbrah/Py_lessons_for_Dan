import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

TOKEN_CYCLES = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN_CYCLES)
