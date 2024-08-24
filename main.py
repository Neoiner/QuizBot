from aiogram import executor
from data.config import TIMEZONE
from loader import dp, scheduler
from utils.db_api import db_gino
from utils.scheduled_jobs import send_schedule_to_subscribed_users
from utils.set_bot_commands import set_default_commands
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):

    print("Подключаем БД")
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = RedisStorage(config.REDIS_IP, 6379, db=1)
    print("Готово")

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Настраиваем команды
    await set_default_commands(dp)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)