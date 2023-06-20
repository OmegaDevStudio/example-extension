import selfcord
from selfcord import Extender, Bot

class Ext(Extender, name="Guild", description="Guild related commands here"):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @Extender.cmd(description="Deletes all messages in channel", aliases=['wipe'])
    async def purge(self, ctx, amount: int):
      await ctx.purge(amount)

