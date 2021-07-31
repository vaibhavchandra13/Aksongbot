import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1761581829:AAGHBvmEE4mlOH9HGKYVF7Tm2PeZOJ5UIFQ")

    APP_ID = int(os.environ.get("APP_ID", 3819739))

    API_HASH = os.environ.get("API_HASH", "a6406a4be8d831a0ca474a7834ae2e31")
