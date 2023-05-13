from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("هنا شع ايبي ايدي "))
API_HASH = getenv("هنا ضع ايبي هاش ")

BOT_TOKEN = getenv("هنا توكن البوت", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("هنا ايدي المطور"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/13f5f96d55c33d9f1753e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0f8437481d1c90561e446.jpg")

SESSION = getenv("هنا ضع كود بايرجرام", None)

SUPPORT_CHAT = getenv("source_ali", "https://t.me/zrrrrrz")
SUPPORT_CHANNEL = getenv("Source_CHANNEL", "https://t.me/lA_l_Al")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "-1001955431592").split()))


FAILED = "https://telegra.ph/file/0f8437481d1c90561e446.jpg"
