from datetime import datetime

from scripts.config.app_configurations import TimezoneConf
from scripts.logging.logging import logger
import pytz


class CommonUtils:
    def __init__(self, project_id=None):
        self.project_id = project_id

    @staticmethod
    def generate_combined_hierarchy_query(hierarchy_data, column="hierarchy"):
        """ """
        hierarchy = "$".join(f"{value}" for value in hierarchy_data.values())
        query = f"WHERE {column} LIKE ('%{hierarchy}%')"
        return query, hierarchy

    @staticmethod
    def convert_epoch_to_timezone(epoch_time_ms: int):
        try:
            local_timezone = pytz.timezone(TimezoneConf.desired_time_zone)

            # Directly create the datetime object and convert to the local timezone
            dt_local = datetime.fromtimestamp(epoch_time_ms / 1000, tz=pytz.utc).astimezone(local_timezone)

            # Return formatted string directly
            return dt_local.strftime('%Y-%m-%d %H:%M:%S%z')

        except (ValueError, TypeError, pytz.UnknownTimeZoneError) as e:
            # Handle errors such as invalid epoch time or timezone
            logger.error(f"Error converting epoch time: {e}")
            return "Invalid input or timezone"
