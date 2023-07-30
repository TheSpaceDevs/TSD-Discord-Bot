import aiohttp
from discord.ext import commands, tasks
import logging
from os import getenv

class MonitorPulse(commands.Cog):
    """
    Discord.py cog for pulsing the monitor of TSD.
    """
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.monitor_pulse_url = getenv('MONITOR_PULSE_URL')
        # Start loop
        self.pulse.start()

    @tasks.loop(seconds=40)
    async def pulse(self):
        """
        Discord task for pulsing the TSD monitor
        endpoint indicating the bot being alive.
        """
        async with aiohttp.ClientSession() as client:
            try:
                await client.get(
                    self.monitor_pulse_url,
                    raise_for_status=True
                )
            except Exception as e:
                logging.warning(
                    'There was an exception when trying '
                    f'to pulse the monitoring endpoint: {e}'
                )


async def setup(bot: commands.Bot):
    await bot.add_cog(MonitorPulse(bot))
