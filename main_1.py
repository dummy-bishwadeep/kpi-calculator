from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import pytz
import time

# Function to perform the scheduled operation
def my_task():
    print(f"Task executed at {datetime.now()}")

# Optimized function for scheduling a task every 5 minutes in a specific timezone
def schedule_task_every_5_minutes(timezone):
    # Initialize the scheduler
    scheduler = BackgroundScheduler(timezone=pytz.timezone(timezone))

    # # Add the task with a 5-minute interval
    scheduler.add_job(
        my_task,
        trigger=IntervalTrigger(seconds=5),  # Every 5 minutes
        id="task_every_5_minutes",
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
    print(f"Scheduler started in timezone: {timezone}")

# Specify your timezone (e.g., "Asia/Kolkata", "America/New_York")
timezone = "Asia/Kolkata"
schedule_task_every_5_minutes(timezone)

# Keep the main thread alive to let the scheduler run
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    print("Shutting down the scheduler...")
