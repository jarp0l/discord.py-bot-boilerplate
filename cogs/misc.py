from discord.ext import commands
import libs.config as config

c_prefix = config.get_config("prefix")

class Misc(commands.Cog, name="Misc commands"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

        if msg.content.startswith("<@!"+str(self.bot.user.id)+">"):
            await msg.channel.send(f"Hi! My prefix here is: `{c_prefix}`")

    @commands.command()
    async def ping(self, ctx):
        '''Replies "pong!"'''
        await ctx.channel.send("pong!")
        
def setup(bot):
    bot.add_cog(Misc(bot))