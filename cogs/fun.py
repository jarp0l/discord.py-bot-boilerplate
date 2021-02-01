from discord.ext import commands

class Fun(commands.Cog, name="Fun commands"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def ping(self, ctx):
        await ctx.channel.send("pong!")

def setup(bot):
    bot.add_cog(Fun(bot))