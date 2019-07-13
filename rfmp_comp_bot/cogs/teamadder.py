from discord.utils import get
from discord.ext import commands
from utils import Config, embed_generator


class TeamAdder(commands.Cog):
    """
    TeamAdder Cog for bot. Allows to react to a message and be assigned a role
    automatically
    """

    def __init__(self, client):
        self.client = client
        self.config = Config("config.toml")

    async def _get_role(self, role_id, guild):
        """
        Gets role from guild with the id of an int from role_id

        - role_id: int of the id of the role (usually from the Config object)
        - guild: discord.Guild object
        < Returns discord.Role objects
        """

        return get(guild.roles, id=role_id)

    @commands.command(
        name="blue",
        description=(
            "Adds user to blue team & removes them from red if they "
            "are already in it"
        ),
        aliases=["team_blue", "blue_team", "blu"],
    )
    async def blue_command(self, ctx):
        red_role = get(ctx.author.roles, id=self.config.RED_ROLE_ID)
        blue_role = get(ctx.author.roles, id=self.config.BLUE_ROLE_ID)

        if red_role:
            embed_template = {
                "main": {
                    "Moving Teams!": (
                        "You have been transfared from the Reds to the Blues"
                    )
                }
            }

            await ctx.author.send(embed=embed_generator(embed_template))
            await ctx.author.remove_roles(red_role)

        if blue_role:
            embed_template = {
                "main": {
                    "Already in the Blues!": (
                        "You are already inside of the Blue Team so nothing "
                        "will happen!"
                    )
                }
            }
        else:
            embed_template = {
                "main": {
                    "Welcome to the Blue team!": (
                        "We are happy to welcome you to the "
                        ":large_blue_circle: team!"
                    )
                }
            }

            try:
                await ctx.author.add_roles(
                    await self._get_role(self.config.BLUE_ROLE_ID, ctx.guild)
                )
            except AttributeError:
                embed_template = {
                    "main": {
                        "Failed to add to Blue Team!": (
                            "The Blue's role does not exist so I could not "
                            "add you to it!"
                        )
                    }
                }

        await ctx.author.send(embed=embed_generator(embed_template))

    @commands.command(
        name="red",
        description=(
            "Adds user to red team & removes them from blue if they "
            "are already in it"
        ),
        aliases=["team_red", "red_team"],
    )
    async def red_command(self, ctx):
        red_role = get(ctx.author.roles, id=self.config.RED_ROLE_ID)
        blue_role = get(ctx.author.roles, id=self.config.BLUE_ROLE_ID)

        if blue_role:
            embed_template = {
                "main": {
                    "Moving Teams!": (
                        "You have been transfared from the Blues to the Reds"
                    )
                }
            }

            await ctx.author.send(embed=embed_generator(embed_template))
            await ctx.author.remove_roles(blue_role)

        if red_role:
            embed_template = {
                "main": {
                    "Already in the Reds!": (
                        "You are already inside of the Red Team so nothing "
                        "will happen!"
                    )
                }
            }
        else:
            embed_template = {
                "main": {
                    "Welcome to the Red team!": (
                        "We are happy to welcome you to the "
                        ":red_circle: team!"
                    )
                }
            }

            try:
                await ctx.author.add_roles(
                    await self._get_role(self.config.RED_ROLE_ID, ctx.guild)
                )
            except AttributeError:
                embed_template = {
                    "main": {
                        "Failed to add to Red Team!": (
                            "The Red's role does not exist so I could not "
                            "add you to it!"
                        )
                    }
                }

        await ctx.author.send(embed=embed_generator(embed_template))


def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(TeamAdder(client))
    print("\tLoaded TeamAdder cog!")
