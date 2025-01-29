from scripts.config.app_configurations import DBConf
from scripts.db.psql.databases import get_assistant_db, get_event_db, get_unified_model_db
from scripts.logging.logging import logger
from scripts.utils.postgres_util import PostgresUtility
from sqlalchemy.orm import Session

session_db = {
    DBConf.ASSISTANT_DB: get_assistant_db(),
    # DBConf.ILENS_EVENT_DB: get_event_db(),
    # DBConf.UNIFIED_MODEL_DB: get_unified_model_db()
}


class CommonPSQL:
    def __init__(self, database=None):
        session: Session = session_db[database]
        self.postgres_utility_obj = PostgresUtility(session=session)

    def find_one_data_by_raw_query(self, raw_query):
        try:
            data = self.postgres_utility_obj.fetch_record_by_raw_query(
                raw_query=raw_query
            )
            return data
        except Exception as fetch_error:
            logger.error(f"Failed to fetch data: {fetch_error}")
            return None

    def find_all_data_by_raw_query(self, raw_query):
        try:
            data = self.postgres_utility_obj.fetch_records_by_raw_query(
                raw_query=raw_query
            )
            return data
        except Exception as fetch_error:
            logger.error(f"Failed to fetch data: {fetch_error}")
            return None

    def insert_data(self, table_name, data_to_insert):
        try:
            data = self.postgres_utility_obj.insert_records_by_raw_query(table_name=table_name, data_to_insert=data_to_insert)
            return data
        except Exception as insert_error:
            logger.error(f"Failed to insert data: {insert_error}")
            return None
