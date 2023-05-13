from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/13f5f96d55c33d9f1753e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0f8437481d1c90561e446.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_ALI", "https://t.me/boboboiol")
SUPPORT_CHANNEL = getenv("source_ali", "https://t.me/zrrrrrz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5196655078").split()))


FAILED = "https://telegra.ph/file/0f8437481d1c90561e446.jpg"
