from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def say(self, ctx: commands.Context, content:str):
        await ctx.send(f"{content}")

async def setup(bot):
    await bot.add_cog(owner(bot))