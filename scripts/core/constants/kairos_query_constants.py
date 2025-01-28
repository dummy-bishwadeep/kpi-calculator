from scripts.config.app_configurations import TimezoneConf, DatabaseConstants


class KairosQueryConstants:
    daily_avg_query = {
  "metrics": [
    {
      "tags": {
        "P": [
          "project_103"
        ]
      },
      "name": f"{DatabaseConstants.project_id}__ilens.live_data.raw",
      "aggregators": [
        {
          "name": "avg",
          "sampling": {
            "value": "5",
            "unit": "minutes",
          },
          "align_sampling": True
        }
      ]
    }
  ],
  "plugins": [],
  "cache_time": 0,
  "time_zone": TimezoneConf.desired_time_zone,
  "start_absolute": 0,
  "end_absolute": 0
}
