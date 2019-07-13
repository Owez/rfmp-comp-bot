from discord.ext import commands
from utils import embed_generator


class Ping(commands.Cog):
    """
    Ping command

    > Detects \'ping\'
    < Returns an emote of a ping-pong racket
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

        print(
            embed_generator(
                {
                    "main": {"Hello": "Test body", "Other": "Last test I promise!"},
                    "meta": {"should_footer": False},
                }
            )
        )

        await ctx.send(
            RETURN_EMOTE
        )

def setup(client):
    """
    Adds the command to the client object
    """
    
    client.add_cog(Ping(client))
