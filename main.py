import logging
from config import bot, dp
from aiogram.utils import executor
from handlers import client, admin

client.register_handlers_client(dp)
admin.register_admin_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


