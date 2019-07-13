from discord.ext import commands
from utils import embed_generator


class Ping(commands.Cog):
    """
    Ping cog for bot

    - Ping command
    """

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="ping",
        description="A ping command to check if the client is indeed online",
        aliases=["p", "pong"],
    )
    async def ping_command(self, ctx):
        RETURN_EMOTE = "🏓"

        await ctx.send(embed=embed_generator({"main": {"Ping": RETURN_EMOTE}}))


def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(Ping(client))
    print("\tLoaded Ping cog!")
