from discord.ext.commands import Context, check


def is_owner():
    async def predicate(ctx: Context):
        return ctx.author.id in ctx.bot.owner_ids

    return check(predicate)
