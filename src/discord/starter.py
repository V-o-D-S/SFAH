from os import getenv
import dotenv

from src.discord.utils import RPDBBot


if __name__ == '__main__':
    dotenv.load_dotenv()

    bot = RPDBBot()
    bot.load_cog('cogs')
    bot.run(getenv('TOKEN'))
