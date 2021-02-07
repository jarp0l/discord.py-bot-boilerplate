# discord.py-bot-boilerplate

This is a pretty basic boilerplate for discord.py bot. It features two example cogs as well.

The bot token should be placed in a `.env` file in this format: 

`BOT_TOKEN = <PLACE_TOKEN_HERE>`

Change the directory to `setup`. Execute the `setup.sh` script (first make it executable) to create a .env file and virtual environment. If the `virtualenv` command to create the environment is not found, it will install automatically.

```bash
$ ./setup.sh
```

Then activate the environment (assuming you haven't changed your directory):

```bash
$ source ../venv/bin/activate
```

Finally, install the required modules with `pip`:

```bash
$ pip3 install -r requirements.txt
```

---

To deactivate the virtual environment, just run the `deactivate` command:

```bash
$ deactivate
```

And to clear the virtual environment, execute the `clean.sh` script.

---

This template was heavily inspired by the neat and tidy code for [TryHackMe's discord bot](https://github.com/thm-community/thm-discord-bot/).