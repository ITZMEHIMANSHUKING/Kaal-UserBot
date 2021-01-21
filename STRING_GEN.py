#TERA_KAAL_BOT

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("""
██╗░░██╗░█████╗░░█████╗░██╗░░░░░
██║░██╔╝██╔══██╗██╔══██╗██║░░░░░
█████═╝░███████║███████║██║░░░░░
██╔═██╗░██╔══██║██╔══██║██║░░░░░
██║░╚██╗██║░░██║██║░░██║███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝""")

print("Welcome To KaalBot String Generator By @ITZ_ME_HIMANSHU_KING")
print("""Kindly Enter Your Details To Continue ! """)
print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
For KaalBot""")

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as KAAL:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(KAAL.session.save())
    print("")
    print("STRING_SESSION Generate Secessfuly Now Check On Telegram Save_Message Inbox,Support Us.")
    omk = KAAL.send_message("me", f"`{KAAL.session.save()}`")
    omk.reply("THIS IS YOUR `STRING_SESSION`.")