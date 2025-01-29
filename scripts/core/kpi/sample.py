from scripts.core.handlers.common_handler import CommonHandler
from scripts.logging.logging import logger

common_handler = CommonHandler()


def calc_daily_avg_aggregated_data():
    try:
        data = common_handler.calc_and_update_daily_avg_aggregated_data()
        logger.info(data)
    except Exception as error:
        logger.error(f"Failed to calculate daily average aggregated data: {error}")
        raise error


calc_daily_avg_aggregated_data()