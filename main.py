import os, dotenv, discord
from discord.ext import commands

dotenv.load_dotenv(verbose=True)

token=os.environ['token']

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
os.environ["JISHAKU_RETAIN"] = "True"

class harm(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=";", owner_ids=[214753146512080907], 
                       intents=discord.Intents.all())

bot = harm()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.load_extension('jishaku')

bot.run(token)