from discord.ext import commands
from .utils import Config, get_cogs

CONFIG_PATH = "config.toml"  # change for custom config path

config = Config(CONFIG_PATH)

client = commands.Bot(
    command_prefix=config.PREFIXES,
    description=config.DESCRIPTION,
    owner_id=config.OWNER_ID,
    case_insensitive=True,
)


@client.event
async def on_ready():
    """
    When client starts up display online message in CLI
    """

    print(f"'{client.user.name}' is online with the id '{client.user.id}'!")

    for cog in get_cogs():
        client.load_extension(cog)
