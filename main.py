import schedule
import time
from datetime import datetime
import pytz

# Function to perform the scheduled operation
def my_task():
    print(f"Task is running at {datetime.now()}")

# Function to run the task every 5 minutes in a specific timezone
def schedule_task_every_5_minutes(timezone):
    tz = pytz.timezone(timezone)

    def task_wrapper():
        current_time = datetime.now(tz)
        print(f"Running task in timezone {timezone}: {current_time}")
        my_task()

    # Schedule the task every 5 minutes
    schedule.every(5).minutes.do(task_wrapper)

# Specify the timezone (e.g., "America/New_York", "Asia/Kolkata")
timezone = "Asia/Kolkata"
schedule_task_every_5_minutes(timezone)

# Keep the scheduler running
print(f"Scheduler is running for timezone: {timezone}")
while True:
    schedule.run_pending()
    time.sleep(1)
