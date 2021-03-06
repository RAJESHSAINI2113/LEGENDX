"""
(((((((((((((((((((((((@rajeshsaini2113)))))))))))))))))))))))))))
(((((((((((((((((((((((@rajeshsaini2113)))))))))))))))))))))))))))
(((((((((((((((((((((((@rajeshsaini2113)))))))))))))))))))))))))))
(((((((((((((((((((((((@rajeshsaini2113)))))))))))))))))))))))))))
                 MADE BY Rajesh
                   CREDITS TEAMRAJESH 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import tbot
from LEGEND import tbot as tgbot
PHOTO = "https://telegra.ph/file/1c1cc4eccbdfc737e2f58.jpg"
@register(pattern=("/alive|/start"))
async def awake(event):
  LEGENDX = "HELLO THIS IS RAJESH OFFICIAL \n\n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.0 LATEST\n\n"
  LEGENDX += "NEW UPDATE SOON\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/rajeshsaini2113"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by rajeshsaini2113 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/LEGENDXOP/LEGEND-BOT"), Button.url("REPO-ULTROID X", "https://github.com/ULTROID-OP/ULTROID-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flegendxop%2Flegend-bot&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-BOTP%2FLE"), Button.url("DEPLOY-ULTROID", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT&template=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
# inline by rajeshsaini2113 🔥
  LEGENDX = "HELLO THIS IS RAJESH OFFICIAL \n\n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.0 LATEST\n\n"
  LEGENDX += "NEW UPDATE SOON\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/rajeshsaini2113"), Button.url("DEVLOPER", "https://t.me/Anahita999")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)
