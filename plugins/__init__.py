
# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio
import time

from pyUltroid import *
from pyUltroid.dB import *
from pyUltroid.functions.all import *
from pyUltroid.functions.sudos import *
from pyUltroid.version import ultroid_version
from telethon import Button
from telethon.tl import functions, types

from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id

List = []
Dict = {}
N = 0

NOSPAM_CHAT = [
    -1001387666944,  # @PyrogramChat
    -1001109500936,  # @TelethonChat
    -1001050982793,  # @Python
    -1001256902287,  # @DurovsChat
]

KANGING_STR = [
    "Blood thirsty...",
    "Kaneki takes your sticker...",
    "Do you know kagune?...",
    "Hey that's a nice sticker!\nimma will take it!..",
    "Kaneki will steal ur Stiker hehe...",
    "Ay look over there (☉｡☉)!→\nimma Will take it...",
    "Kaneki's pack will look cool now",
    "imma is Imprisoning this sticker...",
    "Mr.Kaneki is stealing this sticker... ",
]
