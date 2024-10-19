from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time

# Функция для выполнения задачи
def my_task():
    print("Задача выполнена!")

# Создаем планировщик
scheduler = BackgroundScheduler()

# Настраиваем задачу по расписанию (например, каждый понедельник в 10:30)
trigger = CronTrigger(day_of_week='sat', hour=10, minute=2)

# Добавляем задачу в планировщик
scheduler.add_job(my_task, trigger)

# Запуск планировщика
scheduler.start()

try:
    # Основной процесс
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Остановка планировщика
    scheduler.shutdown()
