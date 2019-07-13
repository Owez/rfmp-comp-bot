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
            if ctx.message.mentions:
                embed_template = {"main": {}}

                for user_action in ctx.message.mentions:
                    embed_template["main"][f"Kicking {user_action.name}.."] = (
                        f"Kicking the user named '{user_action.name}' "
                        f"from {ctx.guild.name}!"
                    )
            else:
                embed_template = {
                    "main": {
                        "No users mentioned!": (
                            "There where no users mentioned in your "
                            "message so I cannot kick anyone!"
                        )
                    }
                }
        else:
            embed_template = {
                "main": {
                    "Invalid permissions!": (
                        "You have not got the sufficant permissions "
                        f"to use this command, {ctx.message.author.name}"
                    )
                }
            }

        await ctx.send(embed=embed_generator(embed_template))


def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(Admin(client))
    print("\tLoaded Admin cog!")
