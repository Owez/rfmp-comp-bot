import os
import toml


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

        self.PREFIXES = config_dict["settings"]["prefixes"]
        self.DESCRIPTION = config_dict["settings"]["desc"]
        self.OWNER_ID = config_dict["settings"]["creator_id"]
        self.CLIENT_TOKEN = self._get_env_var("CLIENT_TOKEN")


def get_cogs():
    """
    Gets all bot cogs from rfmp_comp_bot/cogs

    < Returns list of cog.x
    """

    out_list = []

    for cog_file in os.walk(f"{__package__}/cogs/"):
        cog_stringified = cog_file[2][0]

        if cog_stringified[-3:] == ".py":
            out_list.append(f"cog.{cog_stringified[:-3]}")

    return out_list
