from __future__ import annotations

from .help import Help

async def setup(bot):
    await bot.add_cog(Help(bot))