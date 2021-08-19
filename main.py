import discord, asyncio, pyautogui
from discord.ext import commands

token = '(YOUR TOKEN)'
bot = commands.Bot("-", help_command = None)

@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user))

@bot.command()
async def help(ctx):
    await ctx.send("> **HELP COMMANDS**\n> \n> `type [string]` - Type out a string of text.\n> `move [direction] [amount]` - Moves the mouse a certain amount.\n>     (Directions = Up, Down, Left, Right)\n> `click [button] [amount]` - Clicks the mouse with a specific button a specific amount of times.\n>     (Buttons = Left, Right, Middle)\n> `scroll [direction] ['clicks']` - Scrolls a page up or down a specific amount\n\n> Prefix - `-`")

@bot.command()
async def type(ctx, *, string):
    pyautogui.write(string)
    pyautogui.press('enter')

@bot.command()
async def move(ctx, direction, amount):
    if direction.lower() == "up":
        movement = (0, -int(amount))
    if direction.lower() == "down":
        movement = (0, int(amount))
    if direction.lower() == "left":
        movement = (-int(amount), 0)
    if direction.lower() == "right":
        movement = (int(amount), 0)

    pyautogui.move(movement)

@bot.command()
async def click(ctx, button, *amount):
    if len(amount) == 0:
        amount = 1
    pyautogui.click(button=button.lower(), clicks=int(amount))

@bot.command()
async def scroll(ctx, direction, *clicks):
    if len(clicks) == 0:
        clicks = 1
    if direction.lower() == "down":
        clicks = clicks * -1
    pyautogui.scroll(int(clicks[0]))

@bot.command()
async def delete(ctx, amount):
    for i in range(int(amount)):
        pyautogui.press('backspace')

bot.run(token)
