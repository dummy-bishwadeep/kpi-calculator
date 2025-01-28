from scripts.config.app_configurations import DatabaseConstants


class DatabaseNames:
    ilens_configuration = DatabaseConstants.metadata_db
    ilens_assistant = DatabaseConstants.ilens_assistant_db
    diageo_db = DatabaseConstants.diageo_db


class CollectionNames:
    hierarchy_details = "dynamic_hierarchy_details"
    accessible_hierarchy = "accessible_hierarchy"
    customer_projects = "customer_projects"
    data_model_details = "DataModelDetails"


class PSQLTableNames:
    daily_avg_aggregated_data = "daily_avg_aggregated_data"


class MongoQueryConstants:
    match = "$match"
    lookup = "$lookup"
    unwind = "$unwind"
    replace_root = "$replaceRoot"
    add_fields = "$addFields"


class CommonConstants:
    date_formats = [
        "%Y-%m-%d %H:%M:%S",  # Format with time
        "%Y-%m-%dT%H:%M:%S%z",  # ISO 8601 format with timezone
        "%Y-%m-%dT%H:%M:%S.%fZ",  # ISO 8601 format with fractional seconds and 'Z'
        "%Y-%m-%d",  # Date only
    ]


class KairosConstants:
    start_absolute = "start_absolute"
    end_absolute = "end_absolute"
    metrics = "metrics"
    name = "name"
    tags = "tags"
    plugins = "plugins"
    cache_time = "cache_time"
    time_zone = "time_zone"
    group_by = "group_by"
    aggregators = "aggregators"
    queries = "queries"
    results = "results"


class StopsConstants:
    short_stops = "Short Stops"
    long_stops = "Long Stops"
    count_label = "Count"
    duration_label = "Total Duration"


class EquipmentStatusConstants:
    series_values = ["Running", "Build Back", "Starved", "Stopped"]
    series_colors = {
        "Running": "#89E04F",
        "Stopped": "#FF664F",
        "Starved": "#FF8B00",
        "Build Back": "#5487FF",
    }


class EquipmentStopStatusConstants:
    series_values = ["Short Stop", "Long Stop"]
    series_colors = {"Short Stop": "#FFB966", "Long Stop": "#FF664F"}
