import os
from config import Config

class Translation(object):
  START_TXT = """<b> ʜᴇɪ {}!!</b>
<i>ᴀᴍ ꜱɪᴍᴩʟᴇ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>🚶🏼ɴᴏᴛʜɪɴɢ ʜᴇʀᴇ ᴠʀᴏ</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <code>ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ</code>
<b>Credit :</b> <code>ᴩᴏɪꜱᴏɴ</code>
<b>Language :</b> <code>ᴩyᴛʜᴏɴ3</code>
<b>Lybrary :</b> <code>ᴩyʀᴏɢʀᴀᴍ ᴠ1.2.9</code>
<b>Server :</b> <code>ʜᴇʀᴏᴋᴜ</code>
<b>Build :</b><code>ᴠ0.1</code>"""
