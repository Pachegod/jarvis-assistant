"""
Scheduler for running Jarvis Assistant at configured times
"""

import os
import time
import schedule
import logging
from datetime import datetime
from .main import main as run_assistant

logger = logging.getLogger(__name__)


class AssistantScheduler:
    """Scheduler for Jarvis Assistant"""

    def __init__(self):
        """Initialize the scheduler"""
        self.schedule_time = os.getenv("SCHEDULE_TIME", "08:30")
        self.is_running = False

    def schedule_job(self) -> None:
        """Schedule the daily job"""
        try:
            schedule.every().day.at(self.schedule_time).do(self.run_job)
            logger.info(f"Scheduled daily job at {self.schedule_time}")
        except Exception as e:
            logger.error(f"Failed to schedule job: {e}")

    def run_job(self) -> None:
        """Run the assistant job"""
        try:
            logger.info(f"Starting job at {datetime.now().isoformat()}")
            run_assistant()
            logger.info(f"Job completed at {datetime.now().isoformat()}")
        except Exception as e:
            logger.error(f"Job failed with error: {e}")

    def start(self) -> None:
        """Start the scheduler"""
        try:
            self.is_running = True
            self.schedule_job()
            logger.info("Scheduler started")

            # Run once immediately (optional)
            run_assistant()

            # Keep the scheduler running
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute

        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user")
            self.is_running = False
        except Exception as e:
            logger.error(f"Scheduler error: {e}")
            self.is_running = False

    def stop(self) -> None:
        """Stop the scheduler"""
        self.is_running = False
        logger.info("Scheduler stopped")


def run_scheduler():
    """Entry point for running the scheduler"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    scheduler = AssistantScheduler()
    scheduler.start()


if __name__ == "__main__":
    run_scheduler()
