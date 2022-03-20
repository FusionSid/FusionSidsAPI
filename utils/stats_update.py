""" (module) stats_update

This contains the Stats class and it sets it up
This is from my package fast-api-stats
i had to copy it here cause heruku already uses something called apistats
"""

from fastapistats import Stats

Stats.file_name = "./files/stats.json"

update_stats = Stats.update_stats