from discord.ext import commands
from utils import Config, embed_generator

class Faq(commands.Cog):
    """
    Faq Cog for bot

    - faq command
    """

    def __init__(self, client):
        self.client = client
        self.config = Config("config.toml")
    
    @commands.command(
        name="faq",
        description=(
            "An FAQ command, listing essential infomation for this "
            "Discord Server (RFMP Comp)"
        ),
        aliases=["frequently", "freq", "about", "rfmp", "comp", "bot"]
    )
    async def faq_command(self, ctx):
        embed_template = {
            "main": {
                "What is this?": (
                    "RFMP Comp is a Discord Server related to "
                    "Ravenfield Mutliplayer (RFMP). On this server, we host "
                    "organised ESports matches on special whitelisted servers "
                    "with scheduled events taking place often."
                ),
                "How do I join a Team?": (
                    "You can easily join one of two teams (The \'Reds\' and "
                    "the \'Blues\') by typing either **`?red`** or "
                    "**`?blue`** preferably info the <#599358137274990602> "
                    "channel to automatically be assigned a role!"
                ),
                "Who made this bot?": (
                    f"{self.client.user.name} was made by "
                    f"<@{self.config.OWNER_ID}> and is updated on it\'s GitLab "
                    "repository @ <https://gitlab.com/scOwez/rfmp-comp-bot>"
                )
            },
            "meta": {
                "should_footer": False
            }
        }

        await ctx.send(embed=embed_generator(embed_template))

def setup(client):
    """
    Adds the command to the client object
    """

    client.add_cog(Faq(client))
    print("\tLoaded Faq cog!")
