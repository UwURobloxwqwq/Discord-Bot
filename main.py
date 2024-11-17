import nextcord
from nextcord.ext import commands
import hashlib
from keep_alive import keep_alive
keep_alive()

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
  print("————————————————————————")
  print(f"{bot.user} is online :)")
  print("————————————————————————")

@bot.command(pass_context = True)
async def gen_fluxus(ctx):
  embed = nextcord.Embed(title="✅️ Key Generated Successfully! ✅️", color=nextcord.Color.green())
  embed.add_field(name="Gen key:", value="https://flux.li/android/external/start.php?HWID=" + 
hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())
  embed.set_footer(text=f"Sent by: {ctx.author.name}")
  await ctx.reply(embed=embed)

@bot.command(pass_context = True)
async def gen_delta(ctx):
  embed = nextcord.Embed(title="✅️ Key Generated Successfully! ✅️", color=nextcord.Color.green())
  embed.add_field(name="Gen key:", value="https://gateway.platoboost.com/a/8?id=" + 
hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())
  embed.set_footer(text=f"Sent by: {ctx.author.name}")
  await ctx.reply(embed=embed)

@bot.command(pass_context = True)
async def gen_deltaios(ctx):
  embed = nextcord.Embed(title="✅️ Key Generated Successfully! ✅️", color=nextcord.Color.green())
  embed.add_field(name="Gen key:", value="https://gateway.platoboost.com/a/2?id=" + 
hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())
  embed.set_footer(text=f"Sent by: {ctx.author.name}")
  await ctx.reply(embed=embed)

bot.run('MTE2NzY4MjE0ODExMTc0OTIwMA.G7Q9_4.8QXNbDg47ZIajNaxfyRvcyMGN3m3-fPjHt7NBw')
