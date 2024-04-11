import nextcord
from nextcord.ext import commands
from nextcord import slash_command,Interaction

class test6(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    
   
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        channel = self.bot.get_channel(1206906213649096736)
        if channel is not None:
            embed = nextcord.Embed(
                title=f"Welcome {member.display_name}",
                description=f"Welcome {member.discriminator} to our server",
                color=nextcord.Colour.dark_gold()
            )
            embed.set_thumbnail(url=member.display_avatar)
            await channel.send(embed=embed)
    



def setup(bot):
    bot.add_cog(test6(bot))