import discord

from discord import Forbidden
from discord import app_commands
from discord.ext import commands
from typing import Dict, Optional

from ...kernel.subclasses.bot import Geralt
from ...kernel.subclasses.embed import BaseEmbed
from ...kernel.utilities.crucial import fetch_webhook
from ...kernel.subclasses.context import GeraltContext
from ...kernel.views.fun import Pop, Nitro, ClickGame, PopSize, ClickSize, ClickLeaderboard

class Fun(commands.Cog):
    """Simple commands that induce Fun"""
    def __init__(self, bot: Geralt):
        self.bot: Geralt = bot
        self.delete: Dict = {} # -------
        self.pre_edit: Dict = {} #     |-- > Snipe command related dictionaries
        self.post_edit: Dict = {} # --=)

    @property
    def emote(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name = "Fun", id = 905754435379163176, animated = True)

    # Listeners for "snipe" command
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.delete[message.channel.id] = (message.content, message.author, message.channel.id, message.created_at)

    @commands.Cog.listener()
    async def on_message_edit(self, pre_edit: discord.Message, post_edit: discord.Message):
        self.pre_edit[pre_edit.channel.id] = (pre_edit.jump_url, pre_edit.content, pre_edit.author, pre_edit.channel.id, pre_edit.created_at)
        self.post_edit[post_edit.channel.id] = (post_edit.content, post_edit.author, post_edit.channel.id, post_edit.edited_at)

    # Mimics a user by sending a webhook as them.
    @commands.hybrid_command(
        name = "as", 
        brief = "Send a Webhook",
        with_app_command = True)
    @commands.guild_only()
    @app_commands.guild_only()
    @commands.cooldown(3, 5, commands.BucketType.user)
    @app_commands.describe(user = "Select a user to mimic")    
    @app_commands.describe(message = "Type out the message you want to send.")
    @commands.bot_has_guild_permissions(manage_webhooks = True)
    async def echo(self, ctx: GeraltContext, user: discord.Member, *, message: str) -> Optional[discord.Message]:
        """Send a webhook message as the user you mentioned"""
        try:
            if ctx.interaction:
                await ctx.interaction.response.defer(thinking = True, ephemeral = True)
                wbhk = await fetch_webhook(ctx.channel)
                thread = discord.utils.MISSING
                if isinstance(ctx.channel, discord.Thread):
                    thread = ctx.channel
                await wbhk.send(message, avatar_url = user.display_avatar.url, username = user.display_name, thread = thread)
                await ctx.send("Successfully sent <:NanoTick:925271358735257651>", ephemeral = True)
            else:
                wbhk = await fetch_webhook(ctx.channel)
                thread = discord.utils.MISSING
                if isinstance(ctx.channel, discord.Thread):
                    thread = ctx.channel
                await wbhk.send(message, avatar_url = user.display_avatar.url, username = user.display_name, thread = thread)
                await ctx.message.delete(delay = 0)
        except Exception:
            if ctx.interaction:
                await ctx.send(content = "I don't have `Manage Webhooks` Permissions <:NanoCross:965845144307912754>", ephemeral = True)
            else:
                try:
                    await ctx.author.send(content = "I don't have `Manage Webhooks` Permissions <:NanoCross:965845144307912754>")
                except:
                    await ctx.send(content = "I don't have `Manage Webhooks` Permissions <:NanoCross:965845144307912754>")
    
    # Snipe command as a group
    @commands.group(
        name = "snipe",
        aliases = ["s"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    @commands.guild_only()
    async def snipe(self, ctx: GeraltContext) -> Optional[discord.Message]:
        """Get edited / deleted messages"""
        if ctx.invoked_subcommand is None:
            await ctx.command_help()
 
    # Snipes for deleted messages
    @snipe.command(
        name = "delete",
        brief = "Snipe Deleted Messages",
        aliases = ["del", "d"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def snipe_delete(self, ctx: GeraltContext) -> Optional[discord.Message]:
        """Get the details of the recently deleted message"""
        try:    
            message, author, channel, time = self.delete[ctx.channel.id]    
            delete_emb = BaseEmbed(
                title = "Sniped Deleted Message",
                description = f"**<:ReplyContinued:930634770004725821> - [Message Author :]({author.display_avatar.url})** {author.mention} (`{author.id}`)\n**<:ReplyContinued:930634770004725821> - In Channel :** <#{channel}> (`{channel}`)\n**<:Reply:930634822865547294> - Message Created At :** {self.bot.timestamp(time)}")
            delete_emb.add_field(
                name = "Message Content",
                value = f"{message}")
            await ctx.reply(embed = delete_emb, allowed_mentions = self.bot.mentions)
        except:
            await ctx.reply("No one has deleted. any messages as of now <a:HumanBro:905748764432662549>", allowed_mentions = self.bot.mentions)
 
    # Snipes for edited messages
    @snipe.command(
        name = "edit",
        brief = "Snipe Edited Messages",
        aliases = ["ed", "e"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def snipe_edit(self, ctx: GeraltContext) -> Optional[discord.Message]:
        """Get the details of the recently edited message"""
        try:    
            url, message, author, channel, pre_time = self.pre_edit[ctx.channel.id]    
            post_message, author, channel, post_time = self.post_edit[ctx.channel.id]    
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label = "Jump to Message", style = discord.ButtonStyle.link, url = url, emoji = "<a:ChainLink:936158619030941706>"))
            edit_emb = BaseEmbed(
                title = "Sniped Edited Message",
                description = f"**<:ReplyContinued:930634770004725821> - [Message Author :]({author.display_avatar.url})** {author.mention} (`{author.id}`)\n**<:ReplyContinued:930634770004725821> - In Channel :** <#{channel}> (`{channel}`)\n**<:Reply:930634822865547294> - Message Sent At :** {self.bot.timestamp(pre_time)}")
            edit_emb.add_field(
                name = "Before Edit",
                value = f"{message}")
            edit_emb.add_field(
                name = "After Edit",
                value = f"**<:Reply:930634822865547294> - Message Edited at :** {self.bot.timestamp(post_time)}\n{post_message}",
                inline = False)
            await ctx.reply(embed = edit_emb, allowed_mentions = self.bot.mentions, view = view)
        except:
            await ctx.reply("No one has edited any messages as of now <a:BotLurk:905749164355379241>", allowed_mentions = self.bot.mentions)
    
    @commands.command(
        name = "nitro",
        brief = "Gift Nitro")
    @commands.cooldown(3, 3, commands.BucketType.user)
    async def nitro(self, ctx: GeraltContext, *, user: discord.Member = None) -> Optional[discord.Message]:
        """Gift a user free nitro!"""
        try:
            nitro_emb = BaseEmbed(
                title = "<a:Nitro:905661661191479326> Nitro Has Been Gifted!",
                colour = 0x2F3136)
            nitro_emb.set_thumbnail(url = "https://i.imgur.com/w9aiD6F.png")

            if user is None:
                nitro_emb.description = f">>> {ctx.author.mention} has been gifted nitro classic by {ctx.guild.me.mention} <a:WumpusHypesquad:905661121501990923>.\n<:Reply:930634822865547294> **{ctx.author}** click on the button below to avail the nitro."
                await ctx.send(embed = nitro_emb, view = Nitro(user))
            else:
                nitro_emb.description = f">>> <@{user.id}> has been gifted nitro classic by {ctx.author.mention} <a:WumpusHypesquad:905661121501990923>.\n<:Reply:930634822865547294> **{user}** click on the button below to avail the nitro."
                await ctx.send(embed = nitro_emb, view = Nitro(user))
        
        except Forbidden as F:
            raise commands.errors(F)

    @commands.command(
        name = "pop",
        brief = "Pop Buttons!")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def pop(self, ctx: GeraltContext, *, flag: Optional[PopSize]) -> Optional[discord.Message]:
        """Fidget with the buttons by popping them!
        ????????????
        **Flags Present :**
        `--size` : Sends that many number of buttons to pop.
        **Example :**
        `.gpop [--size 10]` Max size is `25` \U0001f44d
        ????????????"""
        if not flag:
            await Pop(ctx, size = 1).send()
        if flag:
            await Pop(ctx, size = flag.size).send()

    
    @commands.group(
        name = "click",
        brief = "Click and Win",
        aliases = ["cl", "clock"])
    @commands.guild_only()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def click(self, ctx: GeraltContext) -> Optional[discord.Message]:
        """Enjoy a nice satisfying game by clicking on the button!"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)
    
    @click.command(
        name = "start",
        brief = "Start a game of click")
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def click_start(self, ctx: GeraltContext, *, flag: Optional[ClickSize]) -> Optional[discord.Message]:
        """Start a game of click.
        ????????????
        **Flags Present :**
        `--size` : Sends that many number of buttons to click.
        **Example :**
        `.gclick start [--size 10]` Max size is `10` \U0001f44d
        ????????????"""
        if not flag:
            await ClickGame(self.bot, ctx, size = 1).send(ctx)
        if flag:
            await ClickGame(self.bot, ctx, size = flag.size).send(ctx)

    @click.command(
        name = "leaderboard",
        brief = "Check your rank",
        aliases = ["lb", "rank"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def click_score(self, ctx : GeraltContext) -> Optional[discord.Message]:
        await ClickLeaderboard(self.bot, ctx).send()