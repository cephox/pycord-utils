from discord.ext.commands import Bot
import os


def load_cog(bot: Bot, cog: str) -> bool:
    try:
        bot.load_extension(cog)
        return True
    except Exception:
        pass
    return False


def unload_cog(bot: Bot, cog: str) -> bool:
    try:
        bot.unload_extension(cog)
        return True
    except Exception:
        pass
    return False


def reload_cog(bot: Bot, cog: str) -> bool:
    try:
        bot.reload_extension(cog)
        return True
    except Exception:
        pass
    return False


def reload_all_cogs(bot: Bot, directory: str = "cogs") -> dict:
    d = dict()
    for ext in set([i[len(directory) + 1:] + ".py" for i in bot.extensions] + os.listdir(directory)):
        if ext.endswith(".py") and not ext.startswith("_"):
            try:

                unloaded = False
                loaded = False

                try:
                    bot.unload_extension(f"{directory}.{ext[:-3]}")
                    unloaded = True
                except Exception:
                    pass
                try:
                    bot.load_extension(f"{directory}.{ext[:-3]}")
                    loaded = True
                except Exception:
                    pass

                if unloaded and loaded:
                    d[ext] = "reloaded"
                elif unloaded:
                    d[ext] = "unloaded"
                elif loaded:
                    d[ext] = "loaded"
                else:
                    d[ext] = "error"

            except Exception:
                return {}
    return d
