from rfmp_comp_bot import client, CONFIG_PATH
from rfmp_comp_bot.utils import Config

config = Config(CONFIG_PATH)

if __name__ == "__main__":
    client.run(config.CLIENT_TOKEN)
