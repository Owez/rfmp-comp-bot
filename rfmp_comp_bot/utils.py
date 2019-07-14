import os
import toml
import datetime
from discord import Embed


class Config:
    def __init__(self, config_path):
        """
        Initiation function, loading variables for project
        """

        CONFIG_DICT = self._load_toml(config_path)
        self._load_vars(CONFIG_DICT)

    def _load_toml(self, config_path):
        """
        Loads config toml and returns dict

        - config_path: stringified path to config.toml
        < Returns dict from config_path
        """

        return toml.load(open(config_path, "r"))

    def _get_env_var(self, var_name):
        """
        Gets an enviroment variable

        - var_name: string name to use to find
        < Returns value of env var
        x Raises standard `os` lib errors
        """

        return os.environ[var_name]

    def _load_vars(self, config_dict):
        """
        Adds variables to class from the config.toml file that
        has been made into a dict

        - config_dict: dict object from config
        """

        self.CLIENT_TOKEN = self._get_env_var("CLIENT_TOKEN")
        self.PREFIXES = config_dict["settings"]["prefixes"]
        self.DESCRIPTION = config_dict["settings"]["desc"]
        self.OWNER_ID = config_dict["settings"]["creator_id"]
        self.BLUE_ROLE_ID = config_dict["team"]["blue_role_id"]
        self.RED_ROLE_ID = config_dict["team"]["red_role_id"]
        self.LOG_CHANNEL = config_dict["settings"]["log_channel"]


def get_cogs():
    """
    Gets all bot cogs from rfmp_comp_bot/cogs

    < Returns list of cog.x
    """

    out_list = []

    for cog_file in os.walk(os.path.dirname(os.path.abspath(__file__)) + "/cogs/"):
        for cog in cog_file[2]:
            if cog[-3:] == ".py":
                out_list.append(f"cogs.{cog[:-3]}")

    return out_list


def embed_generator(gen_text):
    """
    Discord embed generator, using a small templating system

    - gen_text: a dict following the following syntax:
        INGRESS SPEC
        {
            [BODY]: {
                [FIELD NAME]: [FIELD TEXT],
                [FIELD NAME]: [FIELD TEXT]
            },
            [META (optional)]: {
                [SHOULD FOOTER (optional)]: [BOOL (default yes)]
            }
        }
    < Returns embed object from discord
    """

    embed = Embed()

    for field in gen_text["main"].items():
        embed.add_field(name=field[0], value=field[1])

    if "meta" in gen_text:
        if "should_footer" in gen_text["meta"]:
            _add_footer_embed(embed)
    else:
        _add_footer_embed(embed)

    return embed


def _add_footer_embed(embed):
    """
    Adds footer to embed

    - embed: discord.Embed()
    """

    embed.set_footer(text="RFMP Comp Bot made by scOwez.")
