import discord

from discord import ButtonStyle

from ..subclasses.bot import Geralt
from ..subclasses.embed import BaseEmbed
from ..subclasses.context import GeraltContext

# Sub - class for paginator using buttons. Button style and label has been inspired from RoboDanny [Discord.py Bot] by "Danny aka Rapptz" -> Github Profile
class Paginator(discord.ui.View):
    def __init__(self, bot: Geralt, ctx: GeraltContext, embeds: list[BaseEmbed]):
        super().__init__(timeout = 80)
        self.bot: Geralt = bot
        self.ctx: GeraltContext = ctx
        self.total = len(embeds)
        self.embeds: list[BaseEmbed] = embeds
        self.current = 0

        if self.total >= 1:
            self.left.disabled = True
            self.max_left.disabled = True
        if ctx.interaction:
            self.delete.disabled = True

    @discord.ui.button(label = "<<", style = ButtonStyle.gray)
    async def max_left(self, interaction: discord.Interaction, button: discord.ui.button):
        self.current = 0
        self.left.disabled = True
        button.disabled = True
        
        if self.total >= 1:
            self.right.disabled = False
            self.max_right.disabled = False
        else:
            self.right.disabled = True
            self.max_right.disabled = True

        await interaction.response.edit_message(embed = self.embeds[self.current], view = self)
    
    @discord.ui.button(label = "<", style = ButtonStyle.blurple)
    async def left(self, interaction: discord.Interaction, button: discord.ui.button):
        self.current -= 1
        
        if self.total >= 1:
            self.max_right.disabled = False
            self.right.disabled = False
        else:
            self.max_right.disabled = True
            self.right.disabled = True

        if self.current <= 0:
            self.current = 0
            self.max_left.disabled = True
            button.disabled = True
        else:
            self.max_left.disabled = False
            button.disabled = False

        await interaction.response.edit_message(embed = self.embeds[self.current], view = button.view)
    
    @discord.ui.button(label = ">", style = ButtonStyle.blurple)
    async def right(self, interaction: discord.Interaction, button: discord.ui.button):
        self.current += 1

        if self.current >= self.total - 1:
            self.current = self.total - 1
            button.disabled = True
            self.max_right.disabled = True

        if len(self.embeds) >= 1:
            self.max_left.disabled = False
            self.left.disabled = False
        else:
            self.left.disabled = True
            self.max_left.disabled = True

        await interaction.response.edit_message(embed = self.embeds[self.current], view = button.view)
    
    @discord.ui.button(label = ">>", style = ButtonStyle.gray)
    async def max_right(self, interaction: discord.Interaction, button: discord.ui.button):
        self.current = self.total - 1
        
        button.disabled = True
        self.right.disabled = True

        if self.total >= 1:
            self.max_left.disabled = False
            self.left.disabled = False
        else:
            self.max_left.disabled = True
            self.left.disabled = True
        
        await interaction.response.edit_message(embed = self.embeds[self.current], view = button.view)

    @discord.ui.button(label = "Exit", style = ButtonStyle.danger)
    async def delete(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.message.delete()     
    
    async def send(self, ctx):
        self.message = await ctx.reply(embed = self.embeds[0], view = self, mention_author = False)
        return self.message

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        pain = f"This view can't be handled by you at the moment, invoke for youself by running `{self.ctx.clean_prefix}{self.ctx.command}` for the `{self.ctx.command}` command <:SarahPray:920484222421045258>"
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message(content = f"{pain}", ephemeral = True)
    
    async def on_timeout(self) -> None:
        try:
            for view in self.children:
                view.disabled = True
                await self.message.edit(view = self)
        except discord.errors.NotFound:
            pass