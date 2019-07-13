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

    # @commands.command
    # async def on_reaction_add(self, reaction, user):
    #     """
    #     Gets reaction data and user that posted it. If on right message and
    #     is the right emote for said role (taken from config.toml), add the user
    #     to role
    #     """

    #     if reaction.message.id == self.config.TEAM_MSG_ID:
    #         if reaction.emoji in self.config.BLUE_EMOTES:
    #             embed_template = {
    #                 "main": {
    #                     "Welcome to the Blue team!": (
    #                         "We are happy to welcome you to the "
    #                         f"{self.config.BLUE_EMOTES[0]} team!"
    #                     )
    #                 }
    #             }

    #             await user.add_roles(
    #                 await self._get_role(self.config.BLUE_ROLE_ID, reaction.guild)
    #             )
    #         elif reaction.emoji in self.config.RED_EMOTES:
    #             embed_template = {
    #                 "main": {
    #                     "Welcome to the Red team!": (
    #                         "We are happy to welcome you to the "
    #                         f"{self.config.RED_EMOTES[0]} team!"
    #                     )
    #                 }
    #             }

    #             await user.add_roles(
    #                 await self._get_role(self.config.RED_ROLE_ID, reaction.guild)
    #             )
    #         else:
    #             embed_template = {
    #                 "main": {
    #                     "Unrecognised emote!": (
    #                         "The emote that you added to the team picker was "
    #                         "not recognised! Please try again.."
    #                     )
    #                 }
    #             }

    #         await user.send(embed=embed_template)

    @commands.command(
        name="blue",
        description=(
            "Adds user to blue team & removes them from red if they "
            "are already in it"
        ),
        aliases=["team_blue", "blue_team", "blu"]
    )
    async def blue_command(self, ctx):
        red_role = get(ctx.author.roles, self.config.RED_ROLE_ID)
        blue_role = get(ctx.author.roles, self.config.BLUE_ROLE_ID)

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

            await ctx.author.send(embed=embed_generator(embed_template))
        else:
            # if user is not in blue


def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(TeamAdder(client))
    print("\tLoaded TeamAdder cog!")
