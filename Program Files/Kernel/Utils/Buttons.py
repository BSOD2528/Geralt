import io
from typing import Tuple
import discord
import asyncio
import traceback
from discord import interactions
from discord import client
from discord.components import Button
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ui.button import button
from discord.user import BU

class SelfStop(discord.ui.View):
        @discord.ui.button(label = 'Delete', style = ButtonStyle.blurple, emoji = '\U0001f5d1')
        async def close(self, button : discord.ui.button, interaction : discord.Interaction, *args) -> bool:
            await interaction.message.delete()

class ExceptionButton(discord.ui.View):

        @discord.ui.button(label = 'Exception', style = ButtonStyle.danger)
        async def exception(self, button : discord.ui.button, interaction : discord.Interaction, *args) -> bool:
            await interaction.response.send_message(f'```py\n{Exception.__class__.__name__} --> {Exception}\n```', ephemeral = True)

        @discord.ui.button(label = 'Delete', style = ButtonStyle.blurple)
        async def close(self, button : discord.ui.Button, interaction : discord.Interaction, *args) -> bool:
            await interaction.response.send_message('Deleting', ephemeral = True)
            await interaction.message.delete()

        @discord.ui.button(label = 'Traceback', style = ButtonStyle.danger)
        async def traceback(self, button : discord.ui.button, interaction : discord.Interaction, *args) -> bool:
            stdout = io.StringIO()
            value = stdout.getvalue()
            await interaction.response.send_message(f'```py\n{value}{traceback.format_exc()}\n```', ephemeral = True)

class Die(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @discord.ui.button(style = ButtonStyle.green, emoji = '<:WinSuccess:898571689623978054>')
    async def yes(self, button : discord.ui.button, interaction : discord.Interaction, *args) -> bool:
        await interaction.response.send_message('Okay, Ill die FFS!')
        await self.bot.close()

    @discord.ui.button(style = ButtonStyle.red, emoji = '<:WinCritical:898571769114406942>')
    async def no(self, button : discord.ui.button, interaction : discord.Interaction):
        await interaction.response.send_message('Thank you for sparing me!')
        self.stop()

class Nitro(discord.ui.View):
    
    @discord.ui.button(label = '\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001Claim\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001', style = ButtonStyle.green)
    async def nitro(self, button : discord.ui.button, interaction : discord.Interaction, *args) -> bool:
        await interaction.response.send_message(content = 'https://imgur.com/NQinKJB', ephemeral = True)

