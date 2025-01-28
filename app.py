from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import pytz
import time
from scripts.config.app_configurations import TimezoneConf
from scripts.core.kpi.sample import calc_daily_avg_aggregated_data


def task_schedular():
    # Initialize the scheduler
    scheduler = BackgroundScheduler(timezone=pytz.timezone(TimezoneConf.desired_time_zone))

    # # Add the task with a provided interval
    scheduler.add_job(
        calc_daily_avg_aggregated_data,
        trigger=IntervalTrigger(minutes=5),
        id="batch_job_kpi_calculator",
        replace_existing=True
    )

    # Add the task everyday at 7am
    # scheduler.add_job(
    #     my_task,
    #     trigger=CronTrigger(hour=7, minute=0),  # Every day at 7:00 AM
    #     id="daily_task_7am",
    #     replace_existing=True
    # )

    # Start the scheduler
    scheduler.start()
    print(f"Scheduler started")

task_schedular()

# Keep the main thread alive to let the scheduler run
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    print("Shutting down the scheduler...")
