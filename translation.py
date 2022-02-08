import os
from config import Config

class Translation(object):
  START_TXT = """<b> ʜᴇɪ {}!!</b>
<i>ᴀᴍ ꜱɪᴍᴩʟᴇ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>🚶🏼ɴᴏᴛʜɪɴɢ ʜᴇʀᴇ ᴠʀᴏ</b>"""
  ABOUT_TXT = """

<b>ɴᴀᴍᴇ :</b> <code>ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ</code>
<b>ᴄʀᴇᴅɪᴛ :</b> <code>ᴩᴏɪꜱᴏɴ</code>
<b>ʟᴀɴɢᴜᴀɢᴇ :</b> <code>ᴩyᴛʜᴏɴ3</code>
<b>ʟyʙʀᴀʀy :</b> <code>ᴩyʀᴏɢʀᴀᴍ ᴠ1.2.9</code>
<b>ꜱᴇʀᴠᴇʀ :</b> <code>ʜᴇʀᴏᴋᴜ</code>
<b>ʙᴜɪʟᴅ :</b><code>ᴠ0.1</code>"""
