import json
import random
from datetime import datetime
from operator import itemgetter

from scripts.core.constants.time_formats import AppTimeFormats
from scripts.core.schemas.response_models import (
    DefaultFailureResponse,
    DefaultSuccessResponse,
)
from scripts.db.mongo.ilens_configuration.collections.accessible_hierarchy import (
    AccessibleHierarchyCollection,
)
from scripts.db.mongo.ilens_configuration.collections.customer_projects import (
    CustomerProjectsCollection,
)
from scripts.db.mongo.ilens_configuration.collections.data_model_details import (
    DataModelDetailsCollection,
)
from scripts.logging.logging import logger
from scripts.utils.mongo_util import mongo_client




class CommonUtils:
    def __init__(self, project_id=None):
        self.project_id = project_id


    @staticmethod
    def generate_combined_hierarchy_query(hierarchy_data, column="hierarchy"):
        """ """
        hierarchy = "$".join(f"{value}" for value in hierarchy_data.values())
        query = f"WHERE {column} LIKE ('%{hierarchy}%')"
        return query, hierarchy
