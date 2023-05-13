from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("12421436"))
API_HASH = getenv("fbe8061f1148eabbacdf9e0713e8b74a")

BOT_TOKEN = getenv("5617535290:AAF-jVB0riU_Bgn_CqIjBZy9SwM5m95uWD0", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5401732523"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/13f5f96d55c33d9f1753e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0f8437481d1c90561e446.jpg")

SESSION = getenv("AgBPT79HFELGtvQMntGa9WOavnBZhWJBIi1Ip3Ab0hNgGIldkeoX3Glowp6l0FR3_1K9OQHG5CMPS-S-A0ts07kpmZCgH1Xj5X-oR00VPtTeAEr2PEeYZHqdCuQZdtsdCEOc5M14ZBG2ZMdbw0uDvYnU_xNP1Vetf1AONCL7PO7F29XS7QHsmpu_wT4hAGFtEO-ce6cohrPXB3WFZXISnZcgXRKkhdAdoWuTB-AzGYkyHLgZK9vG3yHPIZS_UefZBBhB10mmCL2kEpaBTRwdgcX2PLRWsmR-6okdAjLyx9-aO6m3J8vhrNHdPZgjQOZ1tBn5fam9QhpJ1YyzfbOLC7qCAAAAATW-qeYA", None)

SUPPORT_CHAT = getenv("source_ali", "https://t.me/zrrrrrz")
SUPPORT_CHANNEL = getenv("ALI_BOT", "https://t.me/lA_l_Al")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1001955431592").split()))


FAILED = "https://telegra.ph/file/0f8437481d1c90561e446.jpg"
