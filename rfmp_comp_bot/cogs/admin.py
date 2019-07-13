from discord.ext import commands
from utils import embed_generator


class Admin(commands.Cog):
    """
    Admin cog for bot

    - Kick command
    - Ban command
    """

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="kick",
        description=(
            "A simple `kick @user` command to kick " "them from the discord server"
        ),
        aliases=["k", "boot", "tempban"],
    )
    async def kick_command(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            # If user has ban/kick rank

            for user_action in ctx.message.mentions:
                print(user_action.name)


def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(Admin(client))
    print("\tLoaded Admin cog!")
