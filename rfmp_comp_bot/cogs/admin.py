from discord.utils import get
from discord.ext import commands
from utils import Config, embed_generator


class Admin(commands.Cog):
    """
    Admin cog for bot

    - Kick command
    - Ban command
    """

    def __init__(self, client):
        self.client = client
        self.config = Config("config.toml")

    async def log_change(self, adverb, ctx, user_action):
        """
        Log changes using an adverb to logging channel

        - adverb: string to use (kicked, banned) to add to "you have been 
          [kicked/banned/etc].
        - ctx: discord.Context, to use to send messages
        - user_action: discord.Member, to use as the subject
        """

        log_channel = get(ctx.guild.channels, id=self.config.LOG_CHANNEL)

        embed_template = {
            "main": {
                adverb.title(): (
                    f"**{ctx.author.name}** {adverb.lower()} "
                    f"**{user_action.name}**"
                ),
                "IDs": f"Admin: {ctx.author.id}, Victim: {user_action.id}",
                "Channel used": (
                    "The channel that the Admin used user was "
                    f"<#{ctx.channel.id}>."
                )
            }
        }

        await log_channel.send(embed=embed_generator(embed_template))

    @commands.command(
        name="kick",
        description=(
            "A simple `kick @user` command to kick them from the discord server"
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

                    await ctx.guild.kick(user_action)
                    await self.log_change("kicked", ctx, user_action)
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

    @commands.command(
        name="ban",
        description=(
            "A simple `ban @user` command to ban them from the discord server"
        ),
        aliases=["b", "hammer"],
    )
    async def ban_command(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            if ctx.message.mentions:
                embed_template = {"main": {}}

                for user_action in ctx.message.mentions:
                    embed_template["main"][f"Banning {user_action.name}.."] = (
                        f"Banning the user named '{user_action.name}' "
                        f"from {ctx.guild.name}!"
                    )

                    await ctx.guild.ban(user_action)
                    await self.log_change("banned", ctx, user_action)
            else:
                embed_template = {
                    "main": {
                        "No users mentioned!": (
                            "There where no users mentioned in your "
                            "message so I cannot ban anyone!"
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
