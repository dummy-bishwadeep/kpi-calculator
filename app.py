import time
import logging
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from scripts.config.app_configurations import TimezoneConf
from scripts.core.kpi.sample import calc_daily_avg_aggregated_data

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Scheduler Configuration
INTERVAL_MINUTES = 1
CRON_HOUR = 7
CRON_MINUTE = 0


class TaskScheduler:
    """Class to manage scheduled tasks."""

    def __init__(self):
        self.scheduler = BackgroundScheduler(timezone=pytz.timezone(TimezoneConf.desired_time_zone))
        self._setup_jobs()

    def _setup_jobs(self):
        """Add scheduled jobs to the scheduler."""
        self.scheduler.add_job(
            calc_daily_avg_aggregated_data,
            trigger=IntervalTrigger(minutes=INTERVAL_MINUTES),
            id="batch_job_kpi_calculator",
            replace_existing=True
        )

        # Uncomment to enable a daily job at 7:00 AM
        # self.scheduler.add_job(
        #     my_task,
        #     trigger=CronTrigger(hour=CRON_HOUR, minute=CRON_MINUTE),
        #     id="daily_task_7am",
        #     replace_existing=True
        # )

    def start(self):
        """Start the scheduler."""
        try:
            self.scheduler.start()
            logging.info("Scheduler started successfully.")
        except Exception as e:
            logging.error(f"Failed to start the scheduler: {e}")
            raise

    def stop(self):
        """Gracefully shut down the scheduler."""
        logging.info("Shutting down the scheduler...")
        self.scheduler.shutdown()
        logging.info("Scheduler shut down successfully.")


if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Start the scheduler
    scheduler.start()

    # Gracefully handle termination signals (Ctrl+C or system exit)
    # signal.signal(signal.SIGINT, scheduler.stop)
    # signal.signal(signal.SIGTERM, scheduler.stop)

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.stop()
