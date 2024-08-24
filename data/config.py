from environs import Env

env = Env()
env.read_env()


# Bot credentials
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

# Redis credentials
REDIS_IP = env.str("REDIS_IP")
