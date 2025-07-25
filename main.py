# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio
import logging
from config import Config
from pyrogram import Client as VJ, idle
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# Initialize bot client
VJBot = VJ(
    "VJ-Forward-Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=120,
    plugins=dict(root="plugins")
)

# Custom iter_messages helper (unchanged)
async def iter_messages(
    self,
    chat_id: Union[int, str],
    limit: int,
    offset: int = 0,
) -> Optional[AsyncGenerator["types.Message", None]]:
    """
    Iterate through a chat sequentially.
    Works same as repeatedly calling get_messages in a loop.
    """
    current = offset
    while True:
        new_diff = min(200, limit - current)
        if new_diff <= 0:
            return
        messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
        for message in messages:
            yield message
            current += 1

# Main async runner
async def main():
    # Start the bot
    await VJBot.start()
    bot_info = await VJBot.get_me()

    # Restart forwards (keeps existing feature)
    await restart_forwards(VJBot)

    print(f"✅ Bot Started as @{bot_info.username}")
    # Keep running until stopped
    await idle()

if __name__ == "__main__":
    # Use modern asyncio.run() (fixes DeprecationWarning)
    asyncio.run(main())

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
