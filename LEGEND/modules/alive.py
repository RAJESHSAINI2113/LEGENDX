"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOY
                   CREDITS TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
from LEGEND.events import register
from LEGEND import tbot
PHOTO = "https://telegra.ph/file/42f05b10e4a417eb9e623.jpg"
@register(pattern="/alive")
async def awake(event):
  LEGENDX = "HELLO THIS IS GRAND OFFICIAL \n\n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.0 LATEST\n\n"
  LEGENDX += "NEW UPDATE SOON\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/LEGENDX22"), Button.url("ADD ME", "https://t.me/grand50_bot?startgroup=true")]]
  BUTTON += [[Button.url("DEVLOPER", "https://t.me/proboyx"), Button.switch_inline("REPO", query="repo", same_peer=True)]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)
