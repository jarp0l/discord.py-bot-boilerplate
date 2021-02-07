import os
import json

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingRequiredArgument

import libs.config as config

####################
# Config variables #
####################
c_prefix = config.get_config("prefix")
c_extensions = config.get_config("cogs")
c_disabled_extensions = config.get_config("disabled_cogs")

####################
# String variables #
####################
s_status = config.get_string("status")

# Prefix
bot = commands.Bot(command_prefix=c_prefix)


# Logging the starting point of bot into the console
@bot.event
async def on_ready():
    print(f"\n### Logged in as {bot.user}\n")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{s_status}'))

# Removes the "command not found" error from the console
@bot.event
async def on_command_error(ctx, error):
    errors_to_skip = [CommandNotFound, MissingRequiredArgument]

    for error_type in errors_to_skip:
        if isinstance(error, error_type):
            return

    raise error

def main():
    # Logging the unlodead cogs into the console
    if len(c_disabled_extensions) != 0:
        print("\nFollowing cogs are disabled:")
        for extension in c_disabled_extensions:
            print(f"[Disabled]\t{extension} has been disabled.")

    # Logging the loaded cogs into the console
    if len(c_extensions) != 0:
        print("\nLoading the COGS:")
        for extension in c_extensions:
            try:
                bot.load_extension(extension)
                print(f"[Success]\t{extension} loaded successfully.")
            except Exception as e:
                print(f"[ERROR]\tAn error occurred while loading {extension}\n-->" + str(e) + "\n")

if __name__ == "__main__":
    main()

bot.run(os.getenv("BOT_TOKEN"))