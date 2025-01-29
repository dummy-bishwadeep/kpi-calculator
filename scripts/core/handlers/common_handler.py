from scripts.config.app_configurations import DatabaseConstants, DBConf, SchedulerConfig
from scripts.core.constants.app_constants import PSQLTableNames
from scripts.core.constants.kairos_query_constants import KairosQueryConstants
from scripts.db.psql.query_layer.common_psql import CommonPSQL
from scripts.utils.common_utils import CommonUtils
from scripts.utils.kairos_util import KairosDBUtility
import datetime


class CommonHandler:
    def __init__(
        self
    ):
        self.project_id = DatabaseConstants.project_id
        self.assistant_db_pg_obj = CommonPSQL(database=DBConf.ASSISTANT_DB)
        # self.unified_model_db_pg_obj = CommonPSQL(database=DBConf.UNIFIED_MODEL_DB)
        # self.events_db_pg_obj = CommonPSQL(database=DBConf.ILENS_EVENT_DB)
        self.kairos_obj = KairosDBUtility()
        self.common_utils = CommonUtils(self.project_id)

    def calc_and_update_daily_avg_aggregated_data(self):
        try:
            start_time, end_time, avg_val = self.fetch_daily_avg_aggregated_data()
            start_time = self.common_utils.convert_epoch_to_timezone(epoch_time_ms=start_time)
            end_time = self.common_utils.convert_epoch_to_timezone(epoch_time_ms=end_time)
            data_to_insert = {
                'start_time': start_time,
                'end_time': end_time,
                'average': avg_val,
            }
            self.assistant_db_pg_obj.insert_data(table_name=PSQLTableNames.daily_avg_aggregated_data,
                                                 data_to_insert=data_to_insert)
            return {
                    'status': 'success',
                    'message': 'Successfully calculated daily average aggregated data',
                    'start_time': start_time,
                    'end_time': end_time
            }
        except Exception as e:
            print(f"Error occurred while calculating and updating daily avg aggregated data: {e}")
            raise e

    def fetch_daily_avg_aggregated_data(self):
        try:
            current_time = datetime.datetime.now(datetime.timezone.utc)
            start_time = int((current_time - datetime.timedelta(days=1)).timestamp() * 1000) # previous date
            end_time = int(current_time.timestamp() * 1000) # current date

            query = KairosQueryConstants.daily_avg_query
            query["start_absolute"] = start_time
            query["end_absolute"] = end_time
            # query['metrics'][0]['aggregators'][0]['sampling']['value'] = str(interval)

            print(query)

            data = self.kairos_obj.read(query_json=query)
            values = data.get('queries', [{}])[0].get('results', [{}])[0].get('values', [])

            total_sum = 0
            for each in values:
                val = each[1]
                total_sum += val

            try:
                avg_val = round(total_sum / len(values), 2)
            except ZeroDivisionError:
                avg_val = 0
            print(avg_val)

            return start_time, end_time, avg_val
        except Exception as e:
            print(f"Error occurred while fetching hourly min aggregated data: {e}")
            raise e