from discord.ext import commands

class Admin(commands.Cog, name="Admin commands"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ban(self, ctx):
        '''Bans a user'''
        await ctx.channel.send("User banned.")

def setup(bot):
    bot.add_cog(Admin(bot))