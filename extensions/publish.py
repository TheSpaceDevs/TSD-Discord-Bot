from discord import Message
from discord.ext import commands
import logging

class Publish(commands.Cog):
    """
    Discord.py cog for publishing messages.
    """
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        """
        Listens for messages to publish.

        Parameters
        ----------
        message : Message
            Discord message object.
        """
        # Check that the author isn't the bot itself
        if message.author == self.bot.user:
            return

        # Check if the channel is a news channel
        if message.channel.is_news():
            # Attempt to publish
            try:
                await message.publish()
            except Exception as e:
                logging.warning(
                    f'Message {message.id} had an '
                    f'exception when trying to publish: {e}'
                )


async def setup(bot: commands.Bot):
    await bot.add_cog(Publish(bot))
