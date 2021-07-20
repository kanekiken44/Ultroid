import time
from datetime import datetime as dt
from platform import python_version as pyver

from git import Repo
from pyUltroid.version import __version__ as UltVer
from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from . import *


@ultroid_cmd(
    pattern="alive2$",
)
async def lol(ult):
    pic = udB.get("ALIVE_IMG")
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = udB.get("ALIVE_TEXT") if udB.get("ALIVE_TEXT") else "Hey,  I am alive."
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    als = (get_string("alive_2")).format(
        header,
        OWNER_NAME,
        ultroid_version,
        UltVer,
        uptime,
        pyver(),
        __version__,
        kk,
    )
    if pic is None:
        return await eor(ult, als)
    elif pic is not None and "telegra" in pic:
        try:
            await ult.reply(als, file=pic, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)
    else:
        try:
            await ult.reply(file=pic)
            await ult.reply(als, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)

